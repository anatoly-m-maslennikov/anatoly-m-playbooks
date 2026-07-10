#!/usr/bin/env python3
"""Template scraper for one-page 81_REFERENCES web/source imports.

Copy this file to /tmp or 51_DEV/10_PROD/obsidian_vault_python/scripts/, then customize selectors and metadata for the source. Run through the vault Python project:

    uv --project 51_DEV/10_PROD/obsidian_vault_python run python /tmp/reference_web_scraper.py --url URL --output '81_REFERENCES/AREA/Author - Title (domain, YYYY-MM-DD).md' --title 'Author - Title (domain, YYYY-MM-DD)' --authors 'Author' --published YYYY-MM-DD --topics 'topic; another-topic' --dry-run

Then rerun without --dry-run after checking the planned output.
"""

from __future__ import annotations

import argparse
import mimetypes
import re
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Iterable
from urllib.parse import urljoin, urlparse

USER_AGENT = "Mozilla/5.0 (compatible; ObsidianReferenceDoc/1.0; personal archival use)"
UNWANTED_SELECTORS = [
    "script",
    "style",
    "noscript",
    "nav",
    "header",
    "footer",
    "aside",
    "form",
    "iframe",
    "button",
    "svg",
    "[role='navigation']",
    "[role='banner']",
    "[role='contentinfo']",
    ".nav",
    ".navbar",
    ".menu",
    ".sidebar",
    ".footer",
    ".header",
    ".comments",
    ".comment",
    ".share",
    ".sharing",
    ".newsletter",
    ".subscribe",
    ".promo",
    ".advertisement",
    ".ads",
]
MAIN_SELECTORS = [
    "article",
    "main",
    "[role='main']",
    ".post-content",
    ".entry-content",
    ".article-content",
    ".content",
]
IMAGE_EXT_BY_CONTENT_TYPE = {
    "image/jpeg": ".jpg",
    "image/png": ".png",
    "image/webp": ".webp",
    "image/gif": ".gif",
    "image/svg+xml": ".svg",
}


@dataclass
class ScrapeResult:
    markdown: str
    downloaded_images: list[Path]
    skipped_images: list[str]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Scrape one accessible web page into an 81_REFERENCES note.")
    parser.add_argument("--url", required=True, help="Source page URL.")
    parser.add_argument("--output", required=True, help="Target Markdown note path, relative to vault root or absolute.")
    parser.add_argument("--title", required=True, help="Reference title / filename stem / H1.")
    parser.add_argument("--authors", default="", help="Semicolon-separated author names.")
    parser.add_argument("--published", default="", help="Published date as YYYY-MM-DD or year when known.")
    parser.add_argument("--topics", default="", help="Semicolon-separated English topics.")
    parser.add_argument("--subtype", default="article", help="Source subtype; default: article.")
    parser.add_argument("--attachments-dir", default="82_ASSETS/51_attachments", help="Attachment directory relative to vault root.")
    parser.add_argument("--download-images", action="store_true", help="Download meaningful in-content images and replace URLs with Obsidian embeds.")
    parser.add_argument("--overwrite", action="store_true", help="Allow overwriting output note if it already exists.")
    parser.add_argument("--dry-run", action="store_true", help="Print plan and counts without writing the note or images.")
    return parser.parse_args()


def repo_root_from_output(output: Path) -> Path:
    if output.is_absolute():
        parts = output.parts
        if "Obsidian_AM_V1" in parts:
            idx = parts.index("Obsidian_AM_V1")
            return Path(*parts[: idx + 1])
        return Path.cwd()
    return Path.cwd()


def split_semicolon(value: str) -> list[str]:
    return [part.strip() for part in value.split(";") if part.strip()]


def yaml_scalar(value: str) -> str:
    escaped = value.replace('"', '\\"')
    return f'"{escaped}"'


def yaml_list(name: str, values: Iterable[str]) -> str:
    values = list(values)
    if not values:
        return ""
    lines = [f"{name}:"]
    lines.extend(f"  - {yaml_scalar(v)}" for v in values)
    return "\n".join(lines) + "\n"


def year_from_published(published: str) -> str:
    match = re.search(r"\b(\d{4})\b", published)
    return match.group(1) if match else ""


def slugify(value: str, fallback: str = "image") -> str:
    value = re.sub(r"[^\w\-.]+", "-", value.lower(), flags=re.UNICODE).strip("-._")
    return value[:80] or fallback


def fetch_html(url: str) -> str:
    import requests

    response = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=30)
    response.raise_for_status()
    return response.text


def choose_main_node(html: str):
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(html, "lxml")
    for selector in UNWANTED_SELECTORS:
        for tag in soup.select(selector):
            tag.decompose()
    for selector in MAIN_SELECTORS:
        node = soup.select_one(selector)
        if node and len(node.get_text(" ", strip=True)) > 400:
            return node
    body = soup.body or soup
    return body


def extension_from_response(url: str, content_type: str) -> str:
    content_type = content_type.split(";", 1)[0].strip().lower()
    if content_type in IMAGE_EXT_BY_CONTENT_TYPE:
        return IMAGE_EXT_BY_CONTENT_TYPE[content_type]
    guessed = mimetypes.guess_extension(content_type)
    if guessed:
        return guessed
    path_ext = Path(urlparse(url).path).suffix.lower()
    return path_ext if path_ext in {".jpg", ".jpeg", ".png", ".webp", ".gif", ".svg"} else ".jpg"


def download_image(url: str, dest_dir: Path, basename: str, index: int) -> Path | None:
    import requests

    response = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=30)
    response.raise_for_status()
    content_type = response.headers.get("content-type", "")
    if not content_type.startswith("image/"):
        return None
    if len(response.content) < 4096 and content_type != "image/svg+xml":
        return None
    ext = extension_from_response(url, content_type)
    dest_dir.mkdir(parents=True, exist_ok=True)
    candidate = dest_dir / f"{slugify(basename)}-{index:02d}{ext}"
    suffix = 2
    while candidate.exists():
        candidate = dest_dir / f"{slugify(basename)}-{index:02d}-{suffix}{ext}"
        suffix += 1
    candidate.write_bytes(response.content)
    return candidate


def rewrite_images(node, page_url: str, vault_root: Path, attachments_dir: Path, title: str, dry_run: bool) -> tuple[list[Path], list[str]]:
    downloaded: list[Path] = []
    skipped: list[str] = []
    images = list(node.find_all("img"))
    for index, img in enumerate(images, start=1):
        src = img.get("src") or img.get("data-src") or img.get("data-original")
        if not src:
            skipped.append("img-without-src")
            img.decompose()
            continue
        url = urljoin(page_url, src)
        if any(token in url.lower() for token in ["avatar", "logo", "icon", "tracking", "pixel", "spinner"]):
            skipped.append(url)
            img.decompose()
            continue
        if dry_run:
            skipped.append(f"dry-run:{url}")
            continue
        try:
            path = download_image(url, vault_root / attachments_dir, title, index)
        except Exception as exc:  # noqa: BLE001 - template should keep scraping even if one image fails.
            skipped.append(f"{url} ({exc})")
            img.decompose()
            continue
        if path is None:
            skipped.append(url)
            img.decompose()
            continue
        downloaded.append(path)
        rel = path.relative_to(vault_root).as_posix()
        img["src"] = f"__LOCAL_IMAGE__{rel}__"
    return downloaded, skipped


def html_to_markdown(node) -> str:
    from markdownify import markdownify as md

    markdown = md(str(node), heading_style="ATX")
    markdown = re.sub(r"!\[[^\]]*\]\(__LOCAL_IMAGE__(.*?)__\)", r"![[\1]]", markdown)
    markdown = markdown.replace("82\\_ASSETS", "82_ASSETS")
    markdown = re.sub(r"\n{3,}", "\n\n", markdown).strip()
    return markdown


def scrape(url: str, vault_root: Path, attachments_dir: Path, title: str, download_images: bool, dry_run: bool) -> ScrapeResult:
    html = fetch_html(url)
    node = choose_main_node(html)
    downloaded: list[Path] = []
    skipped: list[str] = []
    if download_images:
        downloaded, skipped = rewrite_images(node, url, vault_root, attachments_dir, title, dry_run)
    markdown = html_to_markdown(node)
    return ScrapeResult(markdown=markdown, downloaded_images=downloaded, skipped_images=skipped)


def build_note(args: argparse.Namespace, body_markdown: str) -> str:
    authors = split_semicolon(args.authors)
    topics = split_semicolon(args.topics)
    year = year_from_published(args.published)
    frontmatter = "---\n"
    frontmatter += "type: source\n"
    frontmatter += f"subtype: {yaml_scalar(args.subtype)}\n"
    frontmatter += f"title: {yaml_scalar(args.title)}\n"
    frontmatter += yaml_list("authors", authors)
    if year:
        frontmatter += f"year: {year}\n"
    if args.published:
        frontmatter += f"published: {yaml_scalar(args.published)}\n"
    frontmatter += f"source: {yaml_scalar(args.url)}\n"
    frontmatter += yaml_list("topics", topics)
    frontmatter += f"date: {date.today().isoformat()}\n"
    frontmatter += "authorship: external\n"
    frontmatter += "---\n"
    return f"{frontmatter}# {args.title}\n\nSource: {args.url}\n\nSaved for personal use on {date.today().isoformat()}.\n\n## Original text\n\n{body_markdown}\n"


def main() -> int:
    args = parse_args()
    output = Path(args.output)
    vault_root = repo_root_from_output(output)
    if not output.is_absolute():
        output = vault_root / output
    attachments_dir = Path(args.attachments_dir)
    result = scrape(args.url, vault_root, attachments_dir, args.title, args.download_images, args.dry_run)
    note = build_note(args, result.markdown)
    print(f"source: {args.url}")
    print(f"output: {output}")
    print(f"body_chars: {len(result.markdown)}")
    print(f"downloaded_images: {len(result.downloaded_images)}")
    print(f"skipped_images: {len(result.skipped_images)}")
    if args.dry_run:
        print("dry_run: true")
        return 0
    if output.exists() and not args.overwrite:
        print(f"Refusing to overwrite existing output without --overwrite: {output}", file=sys.stderr)
        return 2
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(note, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

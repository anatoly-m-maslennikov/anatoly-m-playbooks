---
name: obsidian-reference-doc
description: Create or update Obsidian source/reference records for third-party material. Use when saving articles, web posts, site/page collections, and docs pages into 81_REFERENCES as full personal-use local copies with meaningful images downloaded into 82_ASSETS/51_attachments; for websites use a deterministic Python scraper through 51_DEV/10_PROD/obsidian_vault_python. Also use for cloning/downloading repository references into $HOME/Documents/Repos, placing book/PDF/EPUB references in Google Drive, creating source notes, following `00_META/40_Operations/10_81_REFERENCES authoring rules/00_81_REFERENCES authoring rules HUB.md`, using the reference-title format "author(s) - title (source domain, published)", or cleaning reference-note metadata/templates.
---

# Obsidian Reference Doc

## Core rule

Create one canonical Markdown record under `81_REFERENCES/` for external/not-mine material. Choose the exact flat area folder, metadata, and topic language from the live vault rule note `00_META/40_Operations/10_81_REFERENCES authoring rules/00_81_REFERENCES authoring rules HUB.md`, then route the durable local copy by source type.

- Article, web post, forum post, or docs page: save the full accessible text in the `81_REFERENCES/` note for Anatoly's personal use. If the page has meaningful images, download them into `82_ASSETS/51_attachments/` and replace external image URLs with Obsidian embeds. Skip decorative, tracking, avatar, logo, ad, share-button, and unrelated images. Do not paste the full text in chat. Keep the original source URL and metadata. Do not bypass paywalls, logins, DRM, or other access controls; if full text or images are unavailable, save what is accessible and state the limitation.
- Repository or code template: ensure a local copy exists under `$HOME/Documents/Repos/`. First scan for an existing clone or name collision. If absent, clone or download the repo there using current directory conventions; for GitHub repos prefer `$HOME/Documents/Repos/<owner>/<repo>` unless the live folder structure suggests another established convention. Create/update the `81_REFERENCES/` note as a source record pointing to both the URL and the local path.
- Book, PDF, EPUB, or book pointer: keep the actual book file in Google Drive, not in the vault. Discover the current Google Drive root and books folder from live filesystem/vault docs before writing. If only a book page is available and no legitimate file is supplied or downloadable, create the reference note with the source URL and report that the book file still needs to be added to Drive. Record the Drive path with `gdrive_path` only when the file/folder exists.

Use live vault rules when uncertain. Read `00_META/40_Operations/10_81_REFERENCES authoring rules/00_81_REFERENCES authoring rules HUB.md` first for reference placement, naming, frontmatter, topics, source-type routing, and verification. Then consult `00_META/00_Vault structure/00_Vault structure HUB.md`, `00_META/20_Writing workflows/00_Writing workflows HUB.md`, `00_META/10_Property schema/00_Property schema HUB.md`, and `82_ASSETS/53_templates/Reference - web post (template).md` if the task involves Templater.

## Web/site scraping rule

For article, docs, web post, or site/page-collection imports, default to a deterministic Python scraper instead of manual copy/paste, fragile shell scraping, or LLM-only extraction.

- Run scrapers with the canonical vault Python environment: `uv --project 51_DEV/10_PROD/obsidian_vault_python run python <script.py>`.
- Prefer the stack already available there: `requests`, `beautifulsoup4`, `markdownify`, `lxml`, and `pyyaml`. If a needed package is missing, add it with `uv --project 51_DEV/10_PROD/obsidian_vault_python add <package>` and then verify/sync the environment.
- For one-off single-page imports, a `/tmp` scraper is acceptable. For repeatable, brittle, or multi-page site imports, save a descriptive script under `51_DEV/10_PROD/obsidian_vault_python/scripts/`. Use `scripts/reference_web_scraper_template.py` as the starting template for single-page article/web imports; copy it first, customize selectors/metadata, and run `--dry-run` before writing.
- For multi-page site imports, do a dry-run or manifest first: source URL, discovered target URLs, grouping/folders, intended note paths, page counts, skipped URL patterns, and duplicate checks. Do not start broad crawling without a bounded manifest.
- Extract main article/body content only. Exclude navigation, sidebar, footer, comments, author bio, email/signup forms, booking CTAs, ads, share widgets, and unrelated promo blocks unless the user explicitly wants them.
- Download meaningful in-article images through the scraper into `82_ASSETS/51_attachments/` with deterministic descriptive filenames. Replace image HTML/URLs with local Obsidian embeds.
- When using `markdownify`, verify it did not escape Obsidian embed paths such as `82\_ASSETS`; normalize them back to `![[82_ASSETS/51_attachments/file.ext]]` and keep embeds separated from adjacent prose/headings.
- Keep scraper logs and final chat reports path/count focused; do not print full copied article text in chat or logs.


## Reference title

Use this exact title/file stem pattern unless the user overrides it:

`author(s) - title (source domain, published)`

Example:

`Юрий Е. - Человек рабочего продукта (systemsworld.club, 2025-08-29)`

Rules:

- Use the human-visible author name(s), not usernames, when available. For repositories, use the profile/display name when available; otherwise use the owner/login.
- Use the source domain without `www.`.
- Use `published` as `YYYY-MM-DD` when known. For repositories, use the repo creation date when no publication/release date is more appropriate. For books, use the original publication date/year when known.
- If the date is unknown, ask only when the date is important; otherwise use `unknown-date` when the user wants to proceed.
- Use the same string for the filename stem, frontmatter `title`, and H1.
- Sanitize filename-forbidden characters only when necessary.

## Frontmatter

Default minimal frontmatter for article/web references:

```yaml
type: source
subtype: article
title: Author - Title (domain, YYYY-MM-DD)
authors:
  - Author
year: YYYY
published: YYYY-MM-DD
source: https://example.com/path
topics:
  - topic-in-english
date: YYYY-MM-DD
authorship: external
```

For repositories, use `subtype: repo` and add `local_copy` only after the clone/download exists:

```yaml
local_copy: $HOME/Documents/Repos/owner/repo
```

For books or book files, use `subtype: book` and add `gdrive_path` only after the Drive file/folder exists:

```yaml
gdrive_path: /path/to/Google Drive/books/file.pdf
```

Topics in `81_REFERENCES/` must be in English, following `00_META/40_Operations/10_81_REFERENCES authoring rules/00_81_REFERENCES authoring rules HUB.md`. Prefer specific retrieval terms over container repeats.

Do not add these fields by default:

- `status`
- `local_copy` unless a repo/local artifact actually exists
- `gdrive_path` unless a Google Drive artifact actually exists
- `yandex_disk` for new references unless the user explicitly asks for an older Yandex Disk path to be recorded

## Body shape

For article/web references, store the full accessible copy in the note:

```markdown
# Author - Title (domain, YYYY-MM-DD)

Source: https://example.com/path

Saved for personal use on YYYY-MM-DD.

## Original text

Cleaned Markdown copy of the accessible article/post text, with meaningful images embedded as `![[82_ASSETS/51_attachments/descriptive-filename.ext]]`.
```

For repositories, keep the note as a pointer to the source plus local clone/download:

```markdown
# Author - Title (github.com, YYYY-MM-DD)

Source repo: https://github.com/owner/repo

Local copy: $HOME/Documents/Repos/owner/repo
```

For books, keep the note as a bibliographic/source pointer plus Drive location when available:

```markdown
# Author - Title (domain, YYYY-MM-DD)

Source/book page: https://example.com/book

Google Drive copy: /path/to/Google Drive/books/file.pdf
```

Do not retell, summarize, or add interpretation unless the user asks.

## Workflow

1. Identify source type first: article/web text, repository/code template, book/file, or generic source pointer.
2. Read `00_META/40_Operations/10_81_REFERENCES authoring rules/00_81_REFERENCES authoring rules HUB.md`, then identify source URL, author(s), title, published/created date, domain, subtype, English topics, and the correct flat `81_REFERENCES/` area folder from user input, selected text, current note, repository metadata, book metadata, or the live web page.
3. Fetch/verify live metadata when the user gave a URL and the current content matters. For current web/GitHub/book pages, prefer live verification over memory.
4. For article/web text, follow the web/site scraping rule: use a Python scraper, extract the full accessible main text, convert it to clean Markdown, download meaningful images into `82_ASSETS/51_attachments/`, and create/update the `81_REFERENCES/` note with `## Original text` plus local `![[...]]` image embeds where the images belong. Use descriptive image filenames based on the reference title/source; avoid overwriting existing attachments.
5. For repositories, scan `$HOME/Documents/Repos/` for an existing copy, clone/download if needed, then record the local path in `local_copy` and the body. Ask for approval when required for network or writes outside the vault.
6. For books, discover the current Google Drive/book storage path before moving/downloading. Put the file there only when it is supplied or legitimately downloadable, then record the path in `gdrive_path` and the body. Ask/report if no file is available.
7. Build the title using `author(s) - title (source domain, published)`.
8. Create or update the note under the correct flat area folder in `81_REFERENCES/` according to `00_META/40_Operations/10_81_REFERENCES authoring rules/00_81_REFERENCES authoring rules HUB.md` (for example `81_REFERENCES/242_TAROT/`, `81_REFERENCES/32_LEARNING/`, `81_REFERENCES/51_DEV/`, or `81_REFERENCES/53_RESEARCH/`). Leave notes at `81_REFERENCES/` root only when intentionally unclassified. Prefer Obsidian CLI for vault-aware moves/renames; if it aborts, use a filesystem fallback only after checking the destination does not already exist.
9. Keep Markdown prose unwrapped; do not insert manual prose line wraps.
10. Verify the final note and any off-vault artifact paths.

## Completion check

Before replying, verify:

- File path is under the correct flat area folder in `81_REFERENCES/`, or at the `81_REFERENCES/` root only when intentionally unclassified.
- `title` and H1 match the filename stem.
- `source` contains the original URL.
- `authorship: external` is present.
- `topics` are in English and follow `00_META/40_Operations/10_81_REFERENCES authoring rules/00_81_REFERENCES authoring rules HUB.md`.
- For articles/web posts, the note contains the full accessible text or explicitly states why only partial text/metadata was saved.
- For article/site imports, a Python scraper was used through `51_DEV/10_PROD/obsidian_vault_python`, or the note/report states why a scraper was unnecessary or unavailable.
- For multi-page site imports, a dry-run/manifest verified page scope, groups/folders, counts, duplicates, and skipped unrelated links before final writes.
- For article/web images, meaningful images are downloaded into `82_ASSETS/51_attachments/`, embedded locally in the note, and verified to exist; irrelevant/decorative images are skipped.
- For repos, the local repo/download path exists and `local_copy` matches it.
- For books, `gdrive_path` is present only when the Google Drive file/folder exists; otherwise the note/body and final reply state that the Drive copy is pending.
- `status` and `yandex_disk` are absent unless explicitly requested.
- `local_copy` and `gdrive_path` are absent unless their corresponding artifacts exist.
- No stale nested reference paths such as `81_REFERENCES/20_PROJECTS/...`, `81_REFERENCES/32_LEARNING/11_SOFT_SKILLS/...`, or `81_REFERENCES/53_RESEARCH/32_Knowledge Systems/...` were introduced.

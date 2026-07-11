#!/usr/bin/env python3
"""Read-only audit helper for refactoring Codex/Claude/Obsidian skill folders."""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from typing import Any

LOCAL_PATTERNS = (".local.",)
CACHE_NAMES = {"__pycache__", ".DS_Store"}
RESOURCE_DIRS = ("agents", "scripts", "references", "assets")


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        return {}, text
    end_index = next((index for index, line in enumerate(lines[1:], start=1) if line.strip() == "---"), None)
    if end_index is None:
        return {}, text
    raw = "".join(lines[1:end_index])
    body = "".join(lines[end_index + 1 :])
    data: dict[str, str] = {}
    for line in raw.splitlines():
        if not line.strip() or line.lstrip().startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"\'')
    return data, body


def iter_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in {".git", ".obsidian", "node_modules"}]
        for filename in filenames:
            files.append(Path(dirpath) / filename)
    return sorted(files)


def line_count(path: Path) -> int:
    try:
        return len(path.read_text(encoding="utf-8", errors="replace").splitlines())
    except OSError:
        return 0


def detect_code_fences(text: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("```"):
            lang = stripped[3:].strip() or "plain"
            counts[lang] = counts.get(lang, 0) + 1
    return counts


def audit(target: Path) -> dict[str, Any]:
    target = target.expanduser().resolve()
    skill_file = target if target.name == "SKILL.md" else target / "SKILL.md"
    root = skill_file.parent
    result: dict[str, Any] = {
        "target": str(target),
        "root": str(root),
        "skill_file": str(skill_file),
        "exists": skill_file.exists(),
    }
    if not skill_file.exists():
        return result

    text = skill_file.read_text(encoding="utf-8", errors="replace")
    frontmatter, body = parse_frontmatter(text)
    files = iter_files(root)
    rel_files = [str(p.relative_to(root)) for p in files]
    local_state = [f for f in rel_files if any(part in CACHE_NAMES for part in Path(f).parts) or any(pat in f for pat in LOCAL_PATTERNS)]
    markdown_files = [p for p in files if p.suffix.lower() == ".md"]
    scripts = [p for p in files if p.suffix.lower() in {".py", ".sh", ".mjs", ".js", ".ts"}]

    result.update(
        {
            "frontmatter": frontmatter,
            "skill_md_lines": len(text.splitlines()),
            "body_lines": len(body.splitlines()),
            "body_chars": len(body),
            "code_fences": detect_code_fences(text),
            "resource_dirs": {name: (root / name).is_dir() for name in RESOURCE_DIRS},
            "file_count": len(files),
            "files": rel_files,
            "local_state_candidates": local_state,
            "large_markdown_files": [
                {"path": str(p.relative_to(root)), "lines": line_count(p)} for p in markdown_files if line_count(p) >= 120
            ],
            "script_files": [str(p.relative_to(root)) for p in scripts],
            "suggested_checks": suggested_checks(root, scripts),
        }
    )
    return result


def suggested_checks(root: Path, scripts: list[Path]) -> list[str]:
    checks: list[str] = []
    py_files = [p for p in scripts if p.suffix.lower() == ".py"]
    sh_files = [p for p in scripts if p.suffix.lower() == ".sh"]
    if py_files:
        checks.append("python3 -m py_compile " + " ".join(str(p) for p in py_files))
    if sh_files:
        checks.append("bash -n " + " ".join(str(p) for p in sh_files))
    checks.append(f"python3 {quick_validate_path_hint()} {root}")
    checks.append(f"git diff --check -- {root}")
    return checks


def quick_validate_path_hint() -> str:
    codex_home = os.environ.get("CODEX_HOME")
    if codex_home:
        base = Path(codex_home)
    else:
        base = Path.home() / ".codex"
    return str(base / "skills" / ".system" / "skill-creator" / "scripts" / "quick_validate.py")


def to_markdown(data: dict[str, Any]) -> str:
    if not data.get("exists"):
        return f"# Skill refactor audit\n\nMissing SKILL.md: `{data['skill_file']}`\n"
    fm = data.get("frontmatter", {})
    lines = [
        "# Skill refactor audit",
        "",
        f"- Root: `{data['root']}`",
        f"- Name: `{fm.get('name', '')}`",
        f"- Description present: {'yes' if fm.get('description') else 'no'}",
        f"- SKILL.md lines: {data['skill_md_lines']}",
        f"- Files: {data['file_count']}",
        f"- Scripts: {', '.join(data['script_files']) if data['script_files'] else 'none'}",
        f"- Local-state candidates: {', '.join(data['local_state_candidates']) if data['local_state_candidates'] else 'none'}",
        "",
        "## Resource dirs",
    ]
    for name, exists in data["resource_dirs"].items():
        lines.append(f"- `{name}/`: {'yes' if exists else 'no'}")
    if data["large_markdown_files"]:
        lines.extend(["", "## Large Markdown files"])
        for item in data["large_markdown_files"]:
            lines.append(f"- `{item['path']}` — {item['lines']} lines")
    if data["code_fences"]:
        lines.extend(["", "## Code fences"])
        for lang, count in sorted(data["code_fences"].items()):
            lines.append(f"- `{lang}`: {count}")
    lines.extend(["", "## Suggested checks"])
    for check in data["suggested_checks"]:
        lines.append(f"- `{check}`")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Read-only audit for a skill folder before refactoring.")
    parser.add_argument("target", help="Skill folder or SKILL.md path")
    parser.add_argument("--format", choices=("json", "markdown"), default="json")
    args = parser.parse_args()

    data = audit(Path(args.target))
    if args.format == "json":
        print(json.dumps(data, ensure_ascii=False, indent=2))
    else:
        print(to_markdown(data), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

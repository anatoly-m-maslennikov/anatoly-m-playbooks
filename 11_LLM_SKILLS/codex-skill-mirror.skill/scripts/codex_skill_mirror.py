#!/usr/bin/env python3
"""Keep custom ~/.codex skills symlinked to vault sources."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


EXCLUDED_NAMES = {".system", ".backups", ".DS_Store"}
IGNORE_COPY = shutil.ignore_patterns("__pycache__", "*.pyc", ".DS_Store")
SPECIAL_SOURCES = {
    "codex-opencode-orchestration": "52_LLM/00_UTILITIES/codex-ocg-orchestration.package/skill",
}


@dataclass(frozen=True)
class InstalledEntry:
    name: str
    path: Path
    kind: str
    target: str | None = None


def default_vault_root() -> Path:
    here = Path(__file__).resolve()
    for parent in here.parents:
        if (parent / "00_META").is_dir() and (parent / "52_LLM").is_dir():
            return parent
    return here.parents[4]


def read_skill_name(skill_dir: Path) -> str | None:
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.exists():
        return None
    text = skill_file.read_text(encoding="utf-8", errors="replace")
    match = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not match:
        return None
    for line in match.group(1).splitlines():
        if line.strip().startswith("name:"):
            return line.split(":", 1)[1].strip().strip("'\"")
    return None


def discover_vault_sources(vault_root: Path) -> dict[str, Path]:
    sources: dict[str, Path] = {}
    candidates: list[Path] = []
    llm = vault_root / "52_LLM"
    if llm.exists():
        candidates.extend(
            sorted(
                p
                for p in llm.rglob("*.skill")
                if ".git" not in p.parts and "__pycache__" not in p.parts
            )
        )
    if llm.exists():
        candidates.extend(
            sorted(
                p
                for p in llm.rglob("*.package/skill")
                if ".git" not in p.parts and "__pycache__" not in p.parts
            )
        )
    legacy_external_llm = vault_root / "81_REFERENCES" / "52_LLM"
    if legacy_external_llm.exists():
        candidates.extend(
            sorted(
                p
                for p in legacy_external_llm.rglob("*.skill")
                if ".git" not in p.parts and "__pycache__" not in p.parts
            )
        )
    for name, rel in SPECIAL_SOURCES.items():
        path = vault_root / rel
        if path.exists():
            sources[name] = path
    for candidate in candidates:
        if not candidate.is_dir():
            continue
        name = read_skill_name(candidate)
        if name and name not in sources:
            sources[name] = candidate
    return sources


def installed_entries(root: Path, include_hidden: bool) -> list[InstalledEntry]:
    entries: list[InstalledEntry] = []
    if not root.exists():
        return entries
    for path in sorted(root.iterdir(), key=lambda p: p.name):
        if path.name in EXCLUDED_NAMES:
            continue
        if path.name.startswith(".") and not include_hidden:
            continue
        if path.is_symlink():
            entries.append(
                InstalledEntry(path.name, path, "symlink", str(path.readlink()))
            )
        elif path.is_dir():
            entries.append(InstalledEntry(path.name, path, "dir"))
        elif path.is_file():
            entries.append(InstalledEntry(path.name, path, "file"))
        else:
            entries.append(InstalledEntry(path.name, path, "other"))
    return entries


def entry_status(entry: InstalledEntry, source: Path | None) -> dict[str, object]:
    correct = False
    resolved_target = None
    if entry.kind == "symlink":
        try:
            resolved_target = str(entry.path.resolve(strict=True))
        except FileNotFoundError:
            resolved_target = None
        if source is not None:
            correct = resolved_target == str(source.resolve())
    if source is None:
        action = "import-needed" if entry.kind == "dir" else "no-vault-source"
    elif correct:
        action = "ok"
    else:
        action = "relink"
    return {
        "name": entry.name,
        "installed_kind": entry.kind,
        "installed_target": entry.target,
        "resolved_target": resolved_target,
        "vault_source": str(source) if source else None,
        "action": action,
    }


def audit(args: argparse.Namespace) -> list[dict[str, object]]:
    sources = discover_vault_sources(args.vault_root)
    entries = installed_entries(args.installed_root, args.include_hidden)
    seen = {e.name for e in entries}
    rows = [entry_status(e, sources.get(e.name)) for e in entries]
    for name, source in sorted(sources.items()):
        if name not in seen:
            rows.append(
                {
                    "name": name,
                    "installed_kind": "missing",
                    "installed_target": None,
                    "resolved_target": None,
                    "vault_source": str(source),
                    "action": "install-symlink",
                }
            )
    return sorted(rows, key=lambda r: str(r["name"]))


def import_missing(args: argparse.Namespace) -> list[str]:
    sources = discover_vault_sources(args.vault_root)
    actions: list[str] = []
    dest_root = args.vault_root / args.import_root
    for entry in installed_entries(args.installed_root, args.include_hidden):
        if entry.kind != "dir" or entry.name in sources:
            continue
        if read_skill_name(entry.path) != entry.name:
            actions.append(f"skip non-skill or name mismatch: {entry.name}")
            continue
        dest = dest_root / f"{entry.name}.skill"
        actions.append(f"copy {entry.path} -> {dest}")
        if args.execute:
            dest_root.mkdir(parents=True, exist_ok=True)
            if dest.exists():
                raise FileExistsError(dest)
            shutil.copytree(entry.path, dest, ignore=IGNORE_COPY, symlinks=True)
    return actions


def backup_path(args: argparse.Namespace, name: str) -> Path:
    stamp = args.backup_stamp or datetime.now().strftime("%Y%m%d-%H%M%S")
    return args.installed_root / ".backups" / stamp / name


def relink(args: argparse.Namespace) -> list[str]:
    sources = discover_vault_sources(args.vault_root)
    actions: list[str] = []
    names = sorted(set(sources) | {e.name for e in installed_entries(args.installed_root, args.include_hidden)})
    wanted = set(args.skill or names)
    for name in names:
        if name not in wanted:
            continue
        source = sources.get(name)
        if source is None:
            actions.append(f"skip no vault source: {name}")
            continue
        installed = args.installed_root / name
        if installed.is_symlink() and installed.exists():
            if installed.resolve() == source.resolve():
                actions.append(f"ok {name} -> {source}")
                continue
        if installed.exists() or installed.is_symlink():
            if installed.is_symlink():
                actions.append(f"unlink wrong symlink {installed}")
                if args.execute:
                    installed.unlink()
            else:
                backup = backup_path(args, name)
                actions.append(f"backup {installed} -> {backup}")
                if args.execute:
                    backup.parent.mkdir(parents=True, exist_ok=True)
                    installed.rename(backup)
        actions.append(f"symlink {installed} -> {source}")
        if args.execute:
            args.installed_root.mkdir(parents=True, exist_ok=True)
            installed.symlink_to(source.resolve(), target_is_directory=True)
    return actions


def check(args: argparse.Namespace) -> int:
    rows = audit(args)
    failures = [
        r for r in rows
        if r["action"] not in {"ok"} and r["installed_kind"] != "missing"
    ]
    print(json.dumps(rows, indent=2, ensure_ascii=False))
    if failures:
        print(f"FAIL: {len(failures)} installed custom skill(s) need action", file=sys.stderr)
        return 1
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "command",
        choices=["audit", "import", "relink", "reconcile", "check"],
    )
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--include-hidden", action="store_true")
    parser.add_argument("--skill", action="append", help="limit relink to one skill")
    parser.add_argument("--backup-stamp")
    parser.add_argument(
        "--vault-root",
        type=Path,
        default=default_vault_root(),
    )
    parser.add_argument(
        "--installed-root",
        type=Path,
        default=Path.home() / ".codex" / "skills",
    )
    parser.add_argument(
        "--import-root",
        type=Path,
        default=Path("52_LLM/00_UTILITIES/codex-skills"),
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    args.vault_root = args.vault_root.expanduser().resolve()
    args.installed_root = args.installed_root.expanduser()
    if args.command == "audit":
        print(json.dumps(audit(args), indent=2, ensure_ascii=False))
        return 0
    if args.command == "import":
        print("\n".join(import_missing(args)))
        return 0
    if args.command == "relink":
        print("\n".join(relink(args)))
        return 0
    if args.command == "reconcile":
        print("\n".join(import_missing(args)))
        args.backup_stamp = args.backup_stamp or datetime.now().strftime("%Y%m%d-%H%M%S")
        print("\n".join(relink(args)))
        return 0
    if args.command == "check":
        return check(args)
    raise AssertionError(args.command)


if __name__ == "__main__":
    raise SystemExit(main())

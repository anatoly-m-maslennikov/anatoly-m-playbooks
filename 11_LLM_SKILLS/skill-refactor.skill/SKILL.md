---
name: skill-refactor
description: Create or refactor Codex, Claude, OpenCode, and Obsidian-vault skill packages to be lean, token-cheap, script-backed where useful, and portable across Linux, macOS, and Windows without changing their behavior. Use when the user asks to create, update, refactor, trim, clean up, slim down, make token-cheap, modernize, scriptify, validate, mirror, or reorganize a `SKILL.md` or skill folder under `52_LLM`, `~/.codex/skills`, `~/.claude/skills`, or a repo-local agent/skill package.
---

# Skill Refactor

Use this skill to create or improve a skill package while preserving its contract. This is usually refactoring, not redesign: keep what the skill does, remove weight, move mechanical work out of `SKILL.md`, make the result work on Linux, macOS, and Windows, and verify before trusting changes.

## Source reference

This skill is adapted from a private local reference, but the public package is self-contained: use this `SKILL.md` plus `scripts/skill_refactor_audit.py` as the runtime contract. Historical source-specific material is intentionally not mirrored to the public repo; do not require it at runtime or import private rules unless the current target explicitly requires them.

## Target discovery

1. Resolve the target from the user request, current note, wikilink, or path. Prefer vault-relative paths for vault files.
2. Read the target `SKILL.md` and its adjacent files before proposing edits.
3. Identify the target shape:
   - Dedicated vault skill: `52_LLM/<domain>/<name>.skill/`.
   - External/not-mine imported skill bucket: `81_REFERENCES/52_LLM/caveman-skills/<name>.skill/`.
   - Package-owned skill: `52_LLM/<domain>/<name>.package/skill/`.
   - Installed global skill: `<codex-home>/skills/<name>` or `<claude-home>/skills/<name>`.
4. If an installed global skill has a vault source, edit the vault source and keep/install the global path as a symlink. Use `52_LLM/00_UTILITIES/codex-skill-mirror.skill/` for generic Codex mirror audits, or the package's own installer when it has one.
5. Do not edit generated caches, `__pycache__`, `.DS_Store`, action logs, or machine-local settings unless the user explicitly asks.

## Naming

For owned vault skills, follow `52_LLM/00_Methodology.md`: prefer action-last names shaped as `<domain>-<entity>-<action>`, with the unambiguous short form `<domain>-<action>` when an entity adds no information. When renaming, update the source folder, `name`, agent metadata and `$trigger`, live HUB references, installed mirrors, public-repo mappings/exports, and current documentation. Preserve historical logs and completed task records as history.

## Cross-platform requirement

Every skill created or updated by this workflow must be usable on Linux, macOS, and Windows unless the user explicitly says the skill is OS-specific. Treat cross-platform portability as part of the skill contract, not as a nice-to-have.

- Prefer portable Python helpers using the standard library: `pathlib`, `subprocess` with argument lists, `shutil`, `tempfile`, `json`, `tomllib` with fallback when needed, and explicit UTF-8 reads/writes.
- Avoid requiring Bash, zsh, PowerShell, GNU-only `sed`/`awk`/`grep`, `chmod`, symlinks, `/tmp`, `~`, `/Users/...`, drive-letter paths, Homebrew paths, or platform-specific shell quoting in the skill's core workflow.
- If shell commands are only examples, label them as examples and provide a Python or platform-neutral alternative for the actual workflow.
- If the target genuinely needs OS-specific behavior, isolate it behind platform detection and document separate Linux/macOS/Windows commands or fallbacks. Do not leave an implicit single-OS happy path.
- Store local paths, executable names, and operator preferences in settings or clearly marked placeholders, not hardcoded into reusable instructions. Use `<vault-root>`, `<skill-root>`, or environment-derived paths in portable skill text.
- Do not rely on symlinks as the only install strategy. Symlinks are fine for this vault's local mirrors, but portable skills must also work when copied as real folders.
- Keep bundled scripts dependency-light. If third-party packages are unavoidable, state installation requirements and provide a graceful error when they are missing.
- Validate scripts with a cross-platform review: no POSIX-only path assumptions, no shell-only quoting assumptions, no case-sensitive filesystem assumptions unless required, no newline-sensitive behavior that breaks on CRLF, and no reliance on executable permission bits.

## Refactor workflow

1. **Audit first.** Run the helper when useful:

```bash
python3 52_LLM/00_UTILITIES/skill-refactor.skill/scripts/skill_refactor_audit.py <skill-folder-or-SKILL.md> --format markdown
```

2. **Inventory load-bearing behavior.** List triggers, required inputs, side effects, safety gates, scripts, templates, references, validation commands, and install/mirror rules.
3. **Delete only non-load-bearing weight.** Remove duplicated prose, stale paths, contradicted rules, repeated checklists, obsolete examples, and long explanations that do not change execution. Ask before deleting anything that might remove behavior.
4. **Move mechanics out of `SKILL.md`.** Prefer scripts for deterministic parsing, hashing, JSON/YAML/frontmatter handling, table generation, diffs, renames, filesystem inventories, and repeatable validation. Default to portable Python for reusable helpers. Use shell only when the target skill is explicitly shell-specific or when you provide equivalent Linux/macOS/Windows paths.
5. **Move static bulk to resources.** Long templates, examples, schemas, prompts, and reference docs belong in `references/`, `assets/`, or a script template, loaded only when needed. Keep `SKILL.md` as routing, judgment, and safety instructions.
6. **Smooth the happy path.** The common path should be one clear command or one ordered sequence. Prefer dry-run/default-read-only behavior and require an explicit `--execute`, `--apply`, or user approval for writes when the operation can damage data.
7. **Preserve vault conventions without hardcoding this machine.** Use Obsidian wiki-links in final reports for vault files, keep Markdown prose unwrapped, use vault-relative paths inside the vault, and update the relevant HUB only when the new or moved skill is a navigation-level entry. When writing reusable skill instructions, avoid absolute vault paths unless the skill is intentionally local to Anatoly's vault.
8. **Preserve behavior.** Refactoring must not weaken safety gates, overwrite policies, symlink checks, dirty-file gates, validation, or provenance rules. If the user wants a behavior change, separate it from the refactor and document it.

## Settings, logs, and local state

- Do not copy `settings.local.toml`, `action_log.local.ndjson`, or other `*.local.*` files as reusable skill state. They are operator/machine-local.
- If the target truly needs tunable knobs, keep defaults in a small helper script and create/backfill a local settings file without overwriting operator edits. Prefer adapting a local copy of the settings-helper pattern from the reference, not referencing another skill by absolute path.
- Add action logs only when the target workflow has real side effects and the log will be used. Keep logs append-only, machine-local, and excluded from mirror/reference copies unless the user explicitly wants the log preserved.
- Do not rely on private assistant memory for portable skill behavior. If a fact matters for future runs, write it into `SKILL.md`, a direct reference file, or the relevant vault rule note.

## Ask before changing

Ask the user before proceeding when:

- the target skill or bundle scope is unclear;
- a deletion might remove real behavior;
- there are multiple plausible homes for shared code or resources;
- a global install should be relinked, overwritten, or backed up;
- validation would require network, dependency installation, or destructive writes;
- the requested change is redesign, not refactoring.

State your best read and the safest proposed path; do not present a long menu unless the user asks.

## Verification

Before replying, run the smallest useful checks for the changed files. Resolve `<skill-creator-quick-validate.py>` from the active Codex install instead of baking a machine path into reusable docs:

```bash
python3 -m py_compile <changed-python-scripts>
bash -n <changed-shell-scripts>
python3 <skill-creator-quick-validate.py> <skill-folder>
git diff --check -- <changed-files>
```

If `quick_validate.py` lacks PyYAML in the active Python, run it through the vault Python environment when available:

```bash
uv --project 51_DEV/50_MAINTENANCE/obsidian_vault_python run python <skill-creator-quick-validate.py> <skill-folder>
```

For scripts that write files, run their read-only or dry-run mode against real target data before any apply/execute mode. For skill text refactors, compare before/after line counts and confirm the trigger description still covers the same user intents.

Also run a portability gate for created or changed skills:

- Read `SKILL.md` and bundled scripts for hardcoded Linux/macOS/Windows-only assumptions.
- Confirm all core write paths use placeholders, settings, environment discovery, or `pathlib`-style path handling.
- Confirm any shell examples have a portable alternative or an explicit OS label.
- Confirm local vault install/mirror instructions are separated from the reusable skill contract.
- If you cannot test on all OSes, state that you performed a static cross-platform review and list any remaining OS-specific assumptions.

## Final report

Report compactly:

- target skill;
- files changed;
- before/after `SKILL.md` line count;
- what was deleted, moved to scripts/resources, or kept;
- validation commands and results;
- any remaining uncertainty or follow-up such as relinking `<codex-home>/skills` / `<claude-home>/skills`.

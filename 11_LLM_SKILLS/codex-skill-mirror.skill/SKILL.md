---
name: codex-skill-mirror
description: Maintain Codex custom skill sources in the Obsidian vault and keep per-skill entries under `~/.codex/skills` as symlinks to those vault sources. Use when auditing installed Codex skills, importing real installed skill folders into the vault, relinking broken or copied global skill installs, creating/updating the vault-to-`~/.codex` mirror, or checking that custom skills are symlinked from `52_LLM` rather than copied into `~/.codex`.
---

# Codex Skill Mirror

Use this skill to keep the vault as the source of truth for custom Codex skills. The installed global entries under `~/.codex/skills` should be symlinks to vault skill folders, not copied mirrors.

## Local contract

This is intentionally local to Anatoly's vault/global Codex mirror. These paths are load-bearing unless Anatoly changes the mirror policy:

- Installed custom skills live under `~/.codex/skills`.
- Vault sources are discovered recursively under `52_LLM/`. Imported custom Codex skills that do not have a dedicated domain home live under `52_LLM/00_UTILITIES/codex-skills/<name>.skill/`; keep `81_REFERENCES/` for source/reference records, not installed skill source-of-truth folders.
- Runtime/system entries stay excluded by default: `.system`, `.backups`, `.DS_Store`, and hidden entries.
- Never edit or replace `.system` unless Anatoly explicitly asks.
- Use `references/default-policy.md` as the compact policy table when checking scope, backups, or source/destination rules.

## Workflow

Stop after the read-only audit unless the user asked for import, relink, or reconcile.

```bash
# Read-only state and planned actions
python3 52_LLM/00_UTILITIES/codex-skill-mirror.skill/scripts/codex_skill_mirror.py audit

# Import custom installed directories that have no vault source yet
python3 52_LLM/00_UTILITIES/codex-skill-mirror.skill/scripts/codex_skill_mirror.py import --execute

# Relink installed custom skills to vault sources
python3 52_LLM/00_UTILITIES/codex-skill-mirror.skill/scripts/codex_skill_mirror.py relink --execute

# Or import then relink in one run
python3 52_LLM/00_UTILITIES/codex-skill-mirror.skill/scripts/codex_skill_mirror.py reconcile --execute

# Verify mirror state
python3 52_LLM/00_UTILITIES/codex-skill-mirror.skill/scripts/codex_skill_mirror.py check

# Validate the skill package; use the uv fallback if python3 lacks yaml
python3 <codex-home>/skills/.system/skill-creator/scripts/quick_validate.py 52_LLM/00_UTILITIES/codex-skill-mirror.skill
UV_CACHE_DIR=/tmp/uv-cache uv --project 51_DEV/10_PROD/obsidian_vault_python run python <codex-home>/skills/.system/skill-creator/scripts/quick_validate.py 52_LLM/00_UTILITIES/codex-skill-mirror.skill
```

## Safety rules

- Default mode is dry-run. Mutations require `--execute`.
- Real installed folders are moved into `~/.codex/skills/.backups/<timestamp>/` before the symlink is created.
- Broken or wrong installed symlinks are replaced directly.
- Source discovery is name-based from `SKILL.md` frontmatter.
- Do not commit, push, or run plugin installers from this skill.
- After relinking installed skills, restart Codex to reload the skill list.
- For non-default environments, pass `--vault-root` and `--installed-root`; do not rewrite the local contract paths just to run one audit.

## Script

Use `scripts/codex_skill_mirror.py`.

| Command | Behavior |
|---|---|
| `audit` | Print JSON state and planned actions. |
| `import` | Copy global-only real skill folders into `52_LLM/00_UTILITIES/codex-skills/`. |
| `relink` | Make installed custom skill entries symlinks to vault sources. |
| `reconcile` | Import then relink. |
| `check` | Fail if any custom installed skill is not a symlink to a vault source. |

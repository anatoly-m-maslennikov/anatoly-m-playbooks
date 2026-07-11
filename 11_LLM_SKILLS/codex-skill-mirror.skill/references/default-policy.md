# Codex skill mirror default policy

| Category | Policy |
|---|---|
| Source of truth | Vault skill folder |
| Installed location | `~/.codex/skills/<skill>` symlink |
| Existing named vault source | `52_LLM/<domain>/<name>.skill/` or package `skill/` folder |
| Imported custom Codex source | `52_LLM/00_UTILITIES/codex-skills/<name>.skill/` |
| Excluded by default | `.system`, `.backups`, `.DS_Store`, hidden runtime entries |
| Backup before relink | `~/.codex/skills/.backups/<timestamp>/<skill>` |
| Default action mode | Dry-run |

Do not use this workflow for Codex system skills unless Anatoly explicitly asks.

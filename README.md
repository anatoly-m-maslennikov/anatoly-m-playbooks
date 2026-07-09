# Anatoly Maslennikov Best Practices Public

Public LLM prompts, workflows, and Codex-style skills that I use or have used as reusable best-practice patterns.

## Structure

`11_LLM_SKILLS/` contains skill packages. Each `*.skill/` folder has a required `SKILL.md`, recommended `agents/openai.yaml`, and optional `references/` or `examples/` folders.

## Skills

| Skill | What it does | Folder |
|---|---|---|
| HH CV to Good Resume | Converts Russian hh.ru/HeadHunter CV material into a concise target-role resume. | `11_LLM_SKILLS/hh-cv-to-good-resume.skill/` |
| CNG Podcast to Post | Turns a raw CNG podcast transcript into a first-person Obsidian Markdown post draft; updated from the current CNG v2 prompt chain. | `11_LLM_SKILLS/cng-podcast-to-post.skill/` |
| CNG Post Packaging | Generates CNG-style title, subtitle, and short promo variants from a finished post; updated from the current CNG v2 prompt chain. | `11_LLM_SKILLS/cng-post-to-title-subtitle-promo.skill/` |
| Refine Article Prompt | Infers abstract prompt improvements from source material, an original prompt, and a redacted target article. | `11_LLM_SKILLS/refine-article-prompt-from-redacted-example.skill/` |
| General Answer Prompt | Preserves and applies a compact general-purpose answer system prompt. | `11_LLM_SKILLS/general-answer-system-prompt.skill/` |
| System Prompt Generator | Generates production-ready system prompts from structured inputs and defaults. | `11_LLM_SKILLS/system-prompt-generator.skill/` |

## Update notes

The old root folders `applied_prompts`, `meta_prompts`, and `system_prompts` were converted into `11_LLM_SKILLS/*.skill` packages. The mini-podcast/article workflow was split into two CNG skills because the current workflow separates post drafting from title/subtitle/promo generation.

Original prompt files and examples were preserved under each skill's `references/` and `examples/` folders where applicable.

## License

This project is licensed under the Creative Commons Attribution–NonCommercial 4.0 International License. See the [LICENSE](./LICENSE.txt) file for details.

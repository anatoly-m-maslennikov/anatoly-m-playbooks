---
name: refine-article-prompt-from-redacted-example
description: Rewrite an article-generation prompt by comparing source material, an original prompt, and a redacted target article. Use when the user wants generalized style and structure instructions inferred from an edited article without copying lexical replacements.
---

# Refine Article Prompt from Redacted Example

Use this skill when the user has source material, an original article-generation prompt, and a redacted article that represents the desired final quality.

When triggered, read `references/original_prompt.md`; it is the method/rule reference, not a substitute for the user's runtime original prompt. Then compare the user-provided materials, normally ordered as source material, original prompt, redacted article. If required material is missing and the task cannot proceed, ask only for the missing item.

Preserve the reference safety contract: infer reusable abstract patterns; do not output explicit word substitutions, synonym lists, lexical replacement tables, or long/private source or redacted-article excerpts.

Return only an improved reusable article-generation prompt in a Markdown code block plus a brief 3-7 bullet rationale about generalized style, structure, and process changes, not word swaps.

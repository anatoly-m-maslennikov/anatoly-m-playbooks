---
name: refine-article-prompt-from-redacted-example
description: Rewrite an article-generation prompt by comparing source material, an original prompt, and a redacted target article. Use when the user wants generalized style and structure instructions inferred from an edited article without copying lexical replacements.
---

# Refine Article Prompt from Redacted Example

Use this skill when the user has source material, an original article-generation prompt, and a redacted article that represents the desired final quality.

Read `references/original_prompt.md` before producing the improved prompt. Follow its restrictions: infer reusable abstract patterns, do not provide explicit word substitutions, do not quote long passages from the redacted article, and do not rely on lexical replacement tables.

## Input contract

Expect materials in this order when available: source material, original prompt, redacted article. If one is missing and the task cannot proceed, ask only for the missing item.

## Output contract

Return an improved reusable prompt in a Markdown code block plus a brief rationale with 3-7 bullets. Keep the rationale about generalized style, structure, and process changes, not word swaps.

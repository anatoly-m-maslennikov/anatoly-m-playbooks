---
name: cng-post-to-title-subtitle-promo
description: Generate CNG-style title variants, subtitle variants, and short promo texts from a finished Colleagues, not guys post. Use when the user provides a CNG post and wants current-post-only packaging options without generic marketing tone or old-context leakage.
---

# CNG Post to Title, Subtitle, Promo

Use this skill after a CNG post draft is finished and the user wants title, subtitle, and promotional text options.

## Source of truth

- `references/cng_post_to_title_subtitle_promo_prompt_v2.md` — active v2 prompt contract, exported from the CNG prompt chain on 2026-06-29. Read it completely before generating options.
- `references/cng_post_to_title_subtitle_promo_prompt_v2_meta.md` — rationale and ADRs; read only when checking why the prompt is shaped this way.

## Workflow

1. Treat the provided finished post as the `## THE POST` input for the v2 prompt.
2. Follow the prompt exactly: Russian only; current-post-only; no analysis or commentary; 10 titles, 10 subtitles, and 10 short promo texts.
3. Do not substitute older examples, prior CNG context, or generic marketing conventions for the current prompt instructions.

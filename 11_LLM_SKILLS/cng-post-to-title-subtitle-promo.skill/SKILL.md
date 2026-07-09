---
name: cng-post-to-title-subtitle-promo
description: Generate CNG-style title variants, subtitle variants, and short promo texts from a finished Colleagues, not guys post. Use when the user provides a CNG post and wants current-post-only packaging options without generic marketing tone or old-context leakage.
---

# CNG Post to Title, Subtitle, Promo

Use this skill after a CNG post draft is finished and the user wants title, subtitle, and promotional text options.

The current source of truth is `references/cng_post_to_title_subtitle_promo_prompt_v2.md`, exported from the active CNG prompt chain dated 2026-06-29. Read it completely before generating options.

## Workflow

1. Read the current v2 prompt in `references/cng_post_to_title_subtitle_promo_prompt_v2.md`.
2. Use only the current post as source material. Do not reuse old hooks, concepts, or contexts unless they are present in the post.
3. Generate exactly the output groups requested by the prompt: 10 titles, 10 subtitles, and 10 short promo texts.
4. Keep the result practical, specific, CNG-shaped, and non-marketing. Preserve roughness or personal angle when the post supports it.

## References

- `references/cng_post_to_title_subtitle_promo_prompt_v2.md` — current updated prompt.
- `references/cng_post_to_title_subtitle_promo_prompt_v2_meta.md` — update rationale and ADRs.
- `references/original/` — archived earlier title/subtitle prompt from this repo.
- `examples/original/` — preserved previous title example output.

---
name: cng-podcast-to-post
description: Transform raw Russian Colleagues, not guys podcast transcripts into publishable first-person Obsidian Markdown post drafts in Anatoly/CNG voice. Use when the user provides a CNG transcript or outline and wants a textified-speech article, not a generic summary or retelling.
---

# CNG Podcast to Post

Use this skill to turn a raw Russian **Colleagues, not guys** oral transcript into a publishable first-person post draft.

The current source of truth is `references/cng_podcast_to_post_prompt_v2.md`, exported from the active CNG prompt chain dated 2026-06-29. Read it completely before drafting and follow it over the older archived prompt.

## Workflow

1. Read the current v2 prompt in `references/cng_podcast_to_post_prompt_v2.md`.
2. Use only the current transcript, outline, and user-provided context. Do not reuse old examples, old episode hooks, or outside frameworks unless the user explicitly provides them.
3. Work as textified speech: preserve Anatoly's first-person stance, rough specificity, causal chain, home vocabulary, jokes, irritation, and self-criticism while removing oral noise.
4. Build the article structure from the transcript's own pattern. Prefer model-first only when the transcript contains a model; otherwise follow the natural story or advice path.
5. Return a complete Obsidian Markdown draft exactly as requested by the current v2 prompt.

## References

- `references/cng_podcast_to_post_prompt_v2.md` — current updated prompt.
- `references/cng_podcast_to_post_prompt_v2_meta.md` — update rationale and ADRs.
- `references/original/` — archived earlier generic mini-podcast prompt materials from this repo.
- `examples/original/` — preserved previous example artifacts; use for historical comparison only, not as source content.

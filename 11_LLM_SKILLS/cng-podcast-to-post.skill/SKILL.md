---
name: cng-podcast-to-post
description: Transform raw Russian Colleagues, not guys podcast transcripts into publishable first-person Obsidian Markdown post drafts in Anatoly/CNG voice. Use when the user provides a CNG transcript or outline and wants a textified-speech article, not a generic summary or retelling.
---

# CNG Podcast to Post

Use this skill to turn a raw Russian **Colleagues, not guys** transcript or outline into a publishable first-person post draft.

Load `references/cng_podcast_to_post_prompt_v2.md` completely before drafting; it is the active 2026-06-29 prompt contract. Consult `references/cng_podcast_to_post_prompt_v2_meta.md` only when rationale or ADR context is needed.

## Workflow

1. Use only the current transcript, outline, and user-provided context; do not reuse old examples, episode hooks, or outside frameworks unless explicitly provided.
2. Follow the v2 prompt workflow: raw speech cleanup → structure discovery → restructuring → deduplication → light polish.
3. Preserve Anatoly's first-person stance, rough specificity, causal chain, home vocabulary, jokes, irritation, and self-criticism while removing oral noise.
4. Build structure from the transcript: model-first only when the transcript contains a model; otherwise follow the natural story or advice path.
5. Return the complete Obsidian Markdown draft exactly as the v2 prompt requires.

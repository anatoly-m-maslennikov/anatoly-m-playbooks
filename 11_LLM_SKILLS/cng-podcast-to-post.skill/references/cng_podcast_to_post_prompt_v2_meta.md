---
type: meta
subtype: prompt
project: Colleagues, not guys
prompt: [[05_CNG_Podcast_to_Post_Prompt]]
date: 2026-06-29
status: active
authorship: llm
---

Previous version: [[CNG - Podcast to post - prompt v1]]

# CNG - Podcast to post - prompt - meta

## Goal

Create a stable prompt that turns a raw podcast transcript into a publishable CNG post while preserving Anatoly's voice, original phrasing, lived experience, and current-episode context. The prompt should make the model clean oral speech into written text, restructure the article where useful, remove repetition, and produce an Obsidian-ready draft with the correct YAML frontmatter.

## Rationale

The first version over-optimized for a generic structured article and could drift into retelling, presentation, or outside-editor prose. The current version is designed to keep the output closer to a cleaned-up text version of the original speech: less neutralization, less invented framing, more transcript-native wording and logic.

The prompt deliberately avoids concrete examples from earlier CNG posts because those examples can leak old context, old phrasing, or old structures into new drafts. Style is described abstractly instead: text style, structure style, headings style, blockquote usage, and metadata rules.

The prompt also separates post creation from title/subtitle/promo generation. The post draft keeps `subtitle`, `date_finished`, and `public_urls` empty; title/subtitle/promo work happens later with the dedicated prompt.

## ADRs

### ADR-001 — Treat transcript conversion as textified speech, not retelling

Status: accepted

Decision: The prompt instructs the model to write as if the oral transcript became a cleaned written text, not as if an editor summarized or presented the content from outside.

Reason: CNG posts should preserve Anatoly's internal logic, pressure, roughness, uncertainty, and practical conclusions. Retelling makes the result too polished, generic, and less recognizably authored.

### ADR-002 — Remove concrete examples from prompt instructions

Status: accepted

Decision: The prompt must not include concrete old-post examples, fixed skeletons from prior episodes, or reusable sample phrases.

Reason: Embedded examples can contaminate new outputs by pulling in context, wording, or structure from previous posts. Style should be represented through abstract rules and current-input-only constraints.

### ADR-003 — Use blockquotes as callouts for side material

Status: accepted

Decision: Markdown blockquotes are allowed for lyrical digressions, useful off-topic branches, and personal-experience asides that are real transcript material but would interrupt the main flow.

Reason: This keeps the main argument readable while preserving the authorial flavor and personal credibility of the transcript.

### ADR-004 — Build structure from the current transcript

Status: accepted

Decision: The prompt should describe structure patterns abstractly but must not impose a fixed prior-post skeleton.

Reason: Some episodes are model-first, some story-first, and some advice-first. Reusing a previous structure can distort the episode and leak old context.

### ADR-005 — Output a complete Obsidian note

Status: accepted

Decision: The prompt returns YAML frontmatter plus article body, using the agreed post metadata shape.

Reason: The result should be directly usable as a vault note and should keep publishing metadata consistent across CNG posts.

## Changelog

### 2026-06-29

- Reworked prompt into v2 for podcast-transcript-to-post workflow.
- Added multi-pass workflow: raw speech cleanup, structure discovery, restructuring, deduplication, light polish.
- Added detailed abstract `Text style`, `Structure style`, and `Headings style` sections.
- Added rule that output should be a textified version of the original speech, not retelling or presentation.
- Added blockquote/callout guidance for lyrical digressions, off-topic branches, and personal-experience asides.
- Updated result YAML template with `source_outline`, `source_transcript`, `prompt`, empty `subtitle`, empty `date_finished`, `status: draft`, and empty `public_urls`.
- Renamed publication URL property convention to `public_urls`.
- Removed all concrete old-post examples and fixed prior-episode skeletons to prevent context leakage.

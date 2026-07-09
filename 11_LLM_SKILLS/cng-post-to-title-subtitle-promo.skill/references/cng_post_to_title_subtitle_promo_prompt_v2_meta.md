---
type: meta
subtype: prompt
project: Colleagues, not guys
prompt: [[CNG - Post to title, subtitiles - prompt]]
date: 2026-06-29
status: active
authorship: llm
---

# CNG - Post to title, subtitiles - prompt - meta

## Goal

Create a stable prompt that takes one finished CNG post and generates 10 title variants, 10 subtitle variants, and 10 short promo text variants. The output should stay grounded in the current post's vocabulary, tension, claims, and personal angle, while avoiding generic media copy and old-post context leakage.

## Rationale

Title/subtitle/promo generation is a separate editorial step from drafting the article. The post draft should first exist on its own; only then should the title, subtitle, and social promo options be generated from the finished text.

The prompt is intentionally current-post-only. Earlier versions included concrete reference titles, subtitles, and promo samples, but those can bias the model toward reusing old vocabulary, old hooks, or old episode structures. The current version describes style abstractly and requires the model to extract material only from the supplied post.

The promo style is now pain/hook oriented. It should still avoid generic advertising, but it should be more explicitly promotional: reaching readers through current or past workplace pain, promising orientation and practical next steps for current issues, explanation and system for past issues, and the emotional message that the reader is okay and not alone.

## ADRs

### ADR-001 — Generate title, subtitle, and promo separately from article drafting

Status: accepted

Decision: The prompt is only for finished posts and should not rewrite the article itself.

Reason: Titles, subtitles, and promo texts depend on the final shape of the post. Generating them too early can lock the post into the wrong hook or encourage the article prompt to optimize for packaging rather than clarity.

### ADR-002 — Produce 10 variants for each output type

Status: accepted

Decision: The prompt must generate exactly 10 titles, exactly 10 subtitles, and exactly 10 short promo texts.

Reason: The goal is selection and comparison, not a single best guess. Multiple variants make it easier to choose between concept, warning, question, consequence, personal, and practical-use angles.

### ADR-003 — Use only current-post source material

Status: accepted

Decision: The prompt explicitly forbids carrying over wording, hooks, contexts, or concepts from any other text unless they are present in the current post.

Reason: Title and promo generation is especially vulnerable to catchy old phrases. Current-post-only grounding prevents accidental leakage from previous CNG episodes.

### ADR-004 — Describe style abstractly instead of by examples

Status: accepted

Decision: The prompt uses `Title style`, `Subtitle style`, and `Promo style (TBD)` sections rather than concrete examples.

Reason: Abstract style descriptions are less likely to contaminate output while still giving the model enough direction to avoid generic marketing or media headlines.

### ADR-005 — Make promo texts pain/hook oriented

Status: accepted

Decision: Promo text guidance should explicitly target reader pains: current pains get orientation and practical next-step promise; past pains get explanation and system. Across both, the emotional message is that the reader is okay and not alone.

Reason: Promo texts need to work harder than titles and subtitles. They should create recognition and relevance without becoming generic advertising or overpromising.

## Changelog

### 2026-06-29

- Reworked prompt to generate three output groups: 10 titles, 10 subtitles, and 10 short promo texts.
- Added abstract `Title style`, `Subtitle style`, and `Promo style` sections.
- Removed concrete old title/subtitle/promo examples to prevent context leakage.
- Added current-post-only grounding rule.
- Added output format with separate `Titles`, `Subtitles`, and `Short promo texts` sections.
- Added final self-check for exact counts, no invented details, no reused context, and CNG-style fit.
- Updated promo guidance to be more promotional through current/past reader pains, practical orientation, explanation/system, and the message that the reader is okay and not alone.
- Added promo variant distribution across current-pain, past-pain, bridge, personal-authorial, and system/model angles.

# Assets page template

Use this shape, replacing placeholders with actual wikilinks, filenames, prompts, and QA notes:

```markdown
---
type: assets
subtype: image set
context:
  - Colleagues, not guys
topics:
  - editorial illustration
  - image generation
source: "[[<source post basename>]]"
prompt: "[[07_Image Assets Orchestrator - prompt]]"
images:
  - "[[<source post basename> - post banner.jpg]]"
  - "[[<source post basename> - podcast preview.jpg]]"
date: <today>
status: draft
---

# <source post basename> Assets

## Source

- Post: [[<source post basename>]]
- Prompt: [[07_Image Assets Orchestrator - prompt]]

## Post banner

![[<source post basename> - post banner.jpg]]

### Final image prompt

<the exact prompt used to generate the post banner>

### QA notes

<short useful QA summary, or `Passed QA.`>

## Podcast episode preview

![[<source post basename> - podcast preview.jpg]]

### Final image prompt

<the exact prompt used to generate the podcast preview>

### QA notes

<short useful QA summary, or `Passed QA.`>
```

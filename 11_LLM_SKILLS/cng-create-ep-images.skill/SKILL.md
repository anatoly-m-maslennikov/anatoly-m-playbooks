---
name: cng-create-ep-images
description: Create persistent Obsidian image asset sets for Colleagues, not guys posts. Use when Codex or Claudian is asked to turn a finished CNG post note into exactly two generated editorial images, a wide post banner and square podcast preview, saved under 82_ASSETS/51_attachments and embedded in a sibling Assets note using the live CNG image prompt chain.
---

# CNG create episode images

Use this skill inside Anatoly's current Obsidian vault when a user gives one finished **Colleagues, not guys** post note and wants companion image assets. Use vault-relative paths in reports and instructions.

Default input rule: if Claudian provides a `<current_note>` context and the user does not give an explicit different path or wikilink, use that current note as the source post. If the user gives a short episode/title phrase and `<current_note>` is present, treat the current note as authoritative unless the phrase clearly points to another note.

The canonical source prompt is `references/07_Image Assets Orchestrator - prompt.md`. Treat that note and its linked prompt chain as the source of truth; reopen them at task time because prompt versions may change.

## Live prompt chain

Read these notes before generating assets:

1. `references/03_Style guide - prompt.md` for the fixed **Workplace Field Notes** visual identity.
2. `references/04_Editorial Analysis - prompt.md` to extract the current post's organizational mechanism.
3. `references/05_Art Direction - prompt.md` to turn the style guide, episode brief, and target format into image-generation prompts.
4. `references/06_Creative Director QA prompt.md` to review generated images.
5. `references/07_Image Assets Orchestrator - prompt.md` for the current exact file, YAML, body, and final-response contract.

## Required output

Create or update one sibling note next to the source post:

```text
<source post basename> Assets.md
```

Generate exactly two final web-ready image files under `82_ASSETS/51_attachments/`:

```text
82_ASSETS/51_attachments/<source post basename> - post banner.jpg
82_ASSETS/51_attachments/<source post basename> - podcast preview.jpg
```

Each final persisted image must be under 1 MB. Prefer small web-ready generation from the start when the image-generation surface supports parameters: request JPEG/WebP output, web/medium quality, and dimensions near 1600×900 for the banner and 1200×1200 for the podcast preview. If the available tool only returns PNGs or ignores size/format parameters, do not persist those PNGs in the vault; immediately downscale if needed and convert/compress to `.jpg` before creating the assets page. If an attachment filename already exists, append a short suffix such as `-v2`; do not overwrite existing images unless the user explicitly asks.

Embed both images in the assets page with Obsidian wiki embeds:

```markdown
![[<source post basename> - post banner.jpg]]
![[<source post basename> - podcast preview.jpg]]
```

Do not leave generated images only in chat or temporary tool output. Persist the selected final `.jpg` files in `82_ASSETS/51_attachments/` and embed those files in the assets page. Do not leave oversized generated PNGs in the vault.

## Workflow

1. Resolve the source post. Prefer an explicit path or wikilink from the user; otherwise use Claudian's `<current_note>` as the default source post. Read the full source post, including YAML and body. Use only this current post as source material; do not reuse older-post concepts, metaphors, wording, or visual hooks unless they are explicitly present in the current post.
2. Extract season, episode, title, central mechanism, key tension, author stance, distinctive vocabulary, and any explicit visualizable objects or metaphors. If metadata is missing, infer conservatively from filename and H1; do not invent content.
3. Apply the Editorial Analysis prompt and produce a compact Episode Brief that describes the organizational mechanism rather than merely summarizing the post.
4. Create exactly two directions from the same Episode Brief: `Post banner — Situation scheme + hook questions` and `Podcast episode preview — Thumbnail mechanism`. Hook questions must be specific to this episode's mechanism and vocabulary. Do not reuse generic series hooks, recurring advice phrases, or wording from earlier assets unless that exact wording is explicit and central in the current post.
5. Apply the Art Direction prompt to produce two final English image-generation prompts. Require all visible handwriting inside the artwork to be in Russian. Keep the **Workplace Field Notes** notebook identity. Avoid literal bosses, employees, office scenes, portraits, logos, dashboards, stock art, motivational posters, and polished vector style.
6. For the responsive wide post banner, specify close-to-16:9 landscape composition, one clear situation scheme, 2-4 reader-facing hook-question cards grounded in the post, important text inside the central 55-60% width and central 70% height, quiet unmarked center for a Play button, side areas used mostly for texture and negative space, and light natural edge mess only. Do not draw a visible oval, circle, target mark, play-button placeholder, or empty outline in the center. Do not use repeated generic hook cards; derive fresh 1-3 word Russian questions from this post only.
7. For the small square podcast episode preview, specify 1:1 composition, one bold thumbnail-readable mechanism, 3-5 major physical objects, large short Russian labels, at most one episode-specific hook-question or warning card, sparse edge mess, low clutter, flat natural contact shadows, and quiet unmarked center for a small Play button. Do not draw a visible oval, circle, target mark, play-button placeholder, or empty outline in the center. Omit the hook card if the only available option is a generic recurring phrase.
8. Generate exactly two final images with the available image-generation tool. If the tool exposes output parameters, set a web-sized output from the start: banner near 1600×900, podcast preview near 1200×1200, JPEG/WebP if supported, web/medium quality. If an image clearly fails QA, revise its prompt once and regenerate that image once. If the tool returns larger PNGs, immediately downscale if needed and convert/compress the selected finals to JPEG under 1 MB each before persisting them in the vault. Keep only the final banner and final preview as persisted deliverables.
9. Apply the Creative Director QA prompt to each final image. Check series identity, editorial strength, composition, physicality, readability, brand identity, image-generation quality, and format fitness. Keep QA notes short.
10. Create the assets page with YAML and body matching the canonical orchestrator prompt. Use the current local date in `YYYY-MM-DD` format for the run date, not the prompt note's frontmatter date.
11. Verify before replying: source post exists; assets page exists; both `.jpg` image files exist under `82_ASSETS/51_attachments/`; each image is under 1 MB; the assets page embeds both images; YAML parses; no unrelated notes were modified.

## Assets page template

Before writing the sibling assets page, read `references/assets-page-template.md` and fill it with actual wikilinks, filenames, prompts, and QA notes. Keep the template shape unless the canonical orchestrator prompt has changed.

## Final response

Reply compactly and do not paste full prompts unless the user asks:

```markdown
Done.

Created: [[<source post basename> Assets]]
Images:
- Post banner: ![[<source post basename> - post banner.jpg]]
- Podcast preview: ![[<source post basename> - podcast preview.jpg]]

Verified: assets page + two attachment files.
```

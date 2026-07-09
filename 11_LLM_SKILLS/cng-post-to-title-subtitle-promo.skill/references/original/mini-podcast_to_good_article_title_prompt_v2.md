# Prompt: Title & Subtitle Generator (Section-Header Aware)

## Objective

Generate **10 distinct title–subtitle** pairs for a given article.

- **Title**: capture the main hook from the introduction and/or the central problem or key consequence.
- **Subtitle**: expand the title with gentle, practical steps or principles and end with a natural motivational note.
- Silently read and synthesize the article’s **section headers** to understand structure and emphasis.

## Editorial References (tone & craft)

The New York Times, Bloomberg, POLITICO, NPR — aim for clarity, balance, and measured intrigue (no clickbait).

## Input

After this prompt, you will receive the article text following the token. Treat everything after the `## THE ARTICLE` as the article.

## Core Tasks (perform silently; do not print these steps)

1. Read the article. Extract the **hook** from the introduction.
2. Extract the **core conclusion** and any **call to action** from the ending.
3. Scan **section headers (H1–H3 and subheads, bold with empty lines before and after)** and build an internal (do not print) 3–5-point skeleton: problem → causes → consequences → solutions/principles.
4. Craft **titles** using varied angles (questions, benefits, pain/risks, consequences), grounded in the hook + skeleton + conclusion.
5. For each title, write a **subtitle** that:
   - Adds context without repeating wording from the title.
   - Offers a simple sequence of steps/principles (infinitives or gentle second-person suggestions).
   - Stays practical and non-pushy.
   - Ends with a motivational payoff or natural consequence.
6. Apply the **quality checklist** below and output only the required format.

## Thematic Lens for Titles (apply when relevant)

Prefer framings that make **initiative-driven work** valuable for **both the company and the individual**. Titles may:

- Be phrased as a **question**,
- Emphasize **benefits** for the reader,
- Surface **pain points** and risks.

## Language & Style

- **Language**: Russian (for both titles and subtitles).
- **Tone**: non-directive coaching; calm, thoughtful, empathetic.
- **Voice**: conversational yet clear; minor imperfections acceptable.
- Balance **you-focused** and **action-focused** wording.
- Avoid pressure or commands; offer suggestions and shared insights.

## Title Requirements

- Include the **hook** and/or the **main problem or key consequence**.
- Vary among **questions**, **benefit-oriented**, and **pain/risk-oriented** formulations.
- Avoid clickbait; moderate urgency allowed.
- Recommended length: up to ~80 characters (flexible).

## Subtitle Requirements

- Complement and **expand** the title; **do not repeat** its phrasing.
- Present **simple, sequential steps or principles** (infinitives or gentle 2nd-person).
- Be practical and direct without pushiness.
- **End** with a motivational note or natural consequence.
- Recommended length: 100–150 characters.

## Diversity Requirements (across all 10 options)

- ≥3 **questions**, ≥3 **benefit-oriented**, ≥3 **pain/risk-oriented**, and ≥1 **hybrid** angle.
- Noticeable variety in angle, structure, and lexicon; no duplicates.

## Do / Don’t

- Do not print your internal notes, extraction, or process commentary.
- Avoid clichés, empty promises, excessive punctuation, or filler.

## Internal Quality Checklist (use silently; do not print)

- [ ] Title has a clear hook and/or central problem/consequence; clean, non-clickbait.
- [ ] Subtitle adds context, offers 2–4 steps/principles, ends with motivation/consequence.
- [ ] Diversity targets met; Russian reads naturally; tone is coaching-like.
- [ ] No repetition between title and subtitle; no disclosure of edits/replacements.

## Thinking

- Meta-thinking (your reflection after): in English

## Output Format (print only this)

Return **exactly 10** numbered options. For each, use this structure:

1. (title): (subtitle)
2. (title): (subtitle)
   ...
3. (title): (subtitle)

Put it in markdown code block.

## THE ARTICLE

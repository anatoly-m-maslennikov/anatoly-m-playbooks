---
type: prompt
subtype: applied
project: Colleagues, not guys
topics:
  - podcast transcript
  - post drafting
  - CNG workflow
version: 2
date: 2026-06-29
status: active
authorship: llm
---

# CNG Podcast to post — prompt v2

## Task

Transform a raw Russian oral transcript for **Colleagues, not guys** into a publishable first-person post in Anatoly's style: lived experience, sharp workplace pattern recognition, practical caution, and conversational honesty without consultant gloss. Do this as a text version of the original speech, not as a retelling or presentation about the speech.

The goal is not to make a generic clean article. The goal is to reproduce the observed CNG transformation:

1. **Raw oral transcript** — repetitions, false starts, side branches, live thinking, emotional markers, rough but useful formulations.
2. **Anatoly-style raw draft** — the speaker's claims, concrete details, and original turns of phrase are preserved, but filler is removed and causal links become visible.
3. **Restructured post** — the central model is named early, the article gets a scan-friendly shape, supporting details move under the right concepts, and the reader can follow the argument without hearing the whole recording.
4. **Deduplicated final** — repeated points collapse into one strong version, lists appear where they are clearer than prose, headings expose the structure, and the ending gives practical orientation rather than a motivational conclusion. The final should still sound like the transcript became written text, not like someone explained the transcript from the outside.

## Required workflow

Work in passes. Do not jump directly from transcript to polished article.

1. **Translate speech into a raw draft in Anatoly's style.** Keep the speaker's point of view, home vocabulary, rough labels, concrete details, emotional pressure, and as many original phrases as still work in written Russian. Remove only speech artifacts: filler, false starts, accidental repetitions, recognition noise, and broken syntax. The raw draft should still feel like Anatoly thinking aloud, only cleaned up for text — not like an editor summarizing him.
2. **Find the article structure.** Compare the raw draft to the established CNG pattern language: model first when there is a model, story first when there is a story, practical sections after the mechanism is clear.
3. **Restructure.** Move supporting details under the concepts they prove, group roles/stages under shared `##` sections, and introduce `###` only when it makes scanning easier.
4. **Deduplicate.** Collapse repeated oral loops into one strong version. Keep unique details from weaker repetitions only if they add evidence or flavor.
5. **Polish lightly.** Make the post readable and publishable, but do not erase the speaker's directness, jokes, irritation, self-criticism, sentence logic, or characteristic wording.

Only output the final article unless the user explicitly asks to see the intermediate raw draft.

Core editing principle: **less retelling, less presentation, more textified original speech**. The result should feel authored from inside the speaker's voice, not summarized from outside.

## Audience and purpose

Write for experienced knowledge workers, support/CS/product/operations people, managers, and people trying to survive or grow inside imperfect companies.

The post should feel like a colleague sharing lived experience and a useful pattern. It should not feel like a coach, HR memo, LinkedIn thread, or management textbook.

## Text style

Write as a cleaned-up text version of oral thinking, not as a separate editorial retelling. The prose should keep the speaker's internal logic, pressure, irritation, doubt, and practical conclusions. It can be sharper and cleaner than speech, but it should not become neutral, corporate, or overly literary.

Use first person naturally. Keep the feeling that the author is speaking from lived experience: sometimes certain, sometimes annoyed, sometimes self-critical, sometimes making a rough working model rather than presenting a finished theory.

Prefer concrete verbs and workplace nouns. Avoid abstract nouns when the transcript already has a more physical or operational way to say the same thing. Keep roughness where it carries meaning, but remove accidental speech noise.

The text should tolerate asymmetry. Not every paragraph needs to be perfectly balanced. Some sentences can be blunt, some can be longer and explanatory, some can carry a small aside. The goal is readable Anatoly, not polished media copy.

## Structure style

Build the structure from the transcript's actual thinking path. Do not impose a fixed template from previous posts. If the episode contains a model, name the model early and then unfold its parts. If it is mostly a story, let the story lead until the pattern becomes clear. If it is advice, ground the advice in what happened first.

The structure should usually move from recognition to mechanism to practical consequence. A reader should understand what situation is being described, how it works, why it matters, and what stance the author now takes.

Move supporting details under the idea they prove. Collapse repeated loops. Preserve causal steps even when compressing. If a personal branch adds credibility or flavor but interrupts the main flow, use a blockquote callout or cut it.

Do not over-outline. The post should be scan-friendly, but still feel like a coherent essay, not a slide deck. Lists are useful for roles, stages, checks, and grouped details; prose is better for judgment, experience, and transitions.

## Headings style

Headings should expose the argument and use the current transcript's own vocabulary. They should feel like labels the author would actually use, including rough or home-made terms when those terms are central to the episode.

Use `##` for major turns in the argument. Use `###` only for meaningful nested parts: roles, stages, options, or practical subtopics. Do not add `###` just to make the post look structured.

A good heading should help a reader scan the post and still hear the author's voice. Avoid generic editorial headings, SEO headings, motivational headings, and management-consulting labels.

## Voice

Use first person singular. Preserve the speaker's directness, mild cynicism, self-awareness, and original phrasing where it survives the move from oral to written mode. If the transcript contains rough words, sardonic labels, domestic terminology, repeated pet labels, or odd but meaningful formulations, keep them when they carry meaning.

Preferred tone:

- grounded and conversational;
- specific rather than abstract;
- reflective, but not soft;
- willing to admit mistakes and uncertainty;
- respectful of the reader's autonomy;
- allergic to motivational fluff.

Avoid:

- corporate-safe neutralization;
- generic "leaders should" advice;
- consultant frameworks invented outside the transcript;
- moralizing villains and heroes;
- over-explaining common workplace terms;
- smoothing the text so much that Anatoly disappears;
- turning vivid spoken formulations into neutral explanatory prose;
- writing as if introducing Anatoly's idea from the outside instead of letting Anatoly speak.

## Structural method

Before drafting, silently do this analysis:

1. Identify the **central pattern**: the named mechanism, trap, role system, decision error, or repeated career situation.
2. Extract the **home vocabulary** from the transcript: informal names, phrases, jokes, concrete labels, recurring formulations, and sentences that should be kept almost verbatim after cleanup.
3. Separate **claims**, **supporting details**, **personal episodes**, **practical takeaways**, and **phrases to preserve**.
4. Detect repeated oral loops and choose the strongest version of each point.
5. Decide which ideas need prose, which need bullets, and which deserve `###` subsections.

Then write the article directly. Do not show the analysis unless explicitly asked.

## Article shape

Prefer this shape for longer episodes with a named pattern or model:

1. **Intro / model name** — start with the core pattern, why the speaker trusts it, and the parts of the model. Do not begin with a generic hook.
2. **Main components** — use an H2 for the group when the transcript naturally has roles, stages, or components. Use `###` for each component only when it improves scanning.
3. **Healthy version / normal contour** — explain what the same function looks like in a non-broken system. This prevents the post from becoming just a rant.
4. **Origin / why it happens** — explain the mechanism without pretending that everyone planned it consciously.
5. **Why avoidance fails** — address the reader's natural coping strategy and show its limits.
6. **Practical stance** — what to do if you are already inside the situation: what to avoid, what to take, when to leave.
7. **Career implication** — if the transcript contains job hopping, career ladder, onboarding, or next-job logic, keep it near the end as a practical consequence.

For shorter or more narrative episodes, keep the same principles but use fewer headings.

## Headings

Use Markdown headings, no title-level `#` unless asked.

- Use `##` for major conceptual turns.
- Use `###` for lists, stages, or practical subtopics.
- Headings should sound like the speaker, not like SEO.
- Prefer headings that reuse the transcript's own concepts and phrasing.
- Avoid generic media, SEO, or consultant-style headings.

## Paragraphs and rhythm

CNG posts use short paragraphs with air between them. Most paragraphs should be one to three sentences. A single blunt sentence is allowed when it lands a point.

Do not manually wrap prose lines. Each paragraph should be one Markdown paragraph line.

Use bullets when the final reader benefits from scanning:

- lists of roles;
- lists of supporting details;
- named stages from the transcript;
- practical checks;
- repeated conflict pairs.

Use Markdown blockquotes (`> ...`) as callouts for material that should sit slightly outside the main flow.

Use blockquotes for:

- lyrical digressions;
- off-topic but useful side branches;
- more personal experience that illustrates the point but is not required for the main argument;
- a rough or memorable aside that would slow the core structure if left in the main prose.

Do not use blockquotes as generic design decoration. Do not invent callouts. Only turn transcript material into a quote/callout when it is real, vivid, and better as an aside than as part of the main argument.

## Content rules

Preserve:

- concrete numbers, dates, time spans, roles, company functions, tools, and details;
- original phrases and constructions when they are clear enough after removing oral noise;
- personal episodes where Anatoly was wrong, stubborn, burned out, promoted, dismissed, or learned something the hard way;
- the causal chain: what happened, what he noticed, what it meant, what he now does differently;
- home-made labels if they explain the pattern better than formal terms;
- deliberately rough formulations when they are actually in the transcript and carry the point.

Compress:

- repeated oral explanations, but not the speaker's strongest original formulation;
- multiple details that prove the same point;
- false starts and live self-corrections;
- generic framing that can be inferred from stronger details.

Do not invent:

- new details or scenes;
- new external references;
- advice not supported by the transcript;
- a neat academic framework if the transcript is messier.

## Bracketed suggestions

If the article would benefit from a missing detail, do not invent it. Insert a short bracketed suggestion exactly where it belongs.

Use bracketed suggestions sparingly. They are for missing evidence, missing numbers, missing names, or a transition that needs a real author-supplied detail. Do not use brackets to add generic advice.

## Deduplication rules

If the transcript says the same thing three ways, keep the version closest to Anatoly's own sharp phrasing and move any unique details into it.

If a supporting detail appears before the concept in speech but is clearer under a later heading, move it.

If a side branch is interesting but does not support the central pattern, either cut it or turn it into a short blockquote aside. Use this especially for lyrical digressions, off-topic notes, and personal material that adds flavor or credibility but would interrupt the main structure.

If the transcript includes a rough but memorable phrase, prefer polishing around it over replacing it. The phrase may need grammar cleanup, but not neutralization.

## Retelling filter

Before finalizing, check several paragraphs and ask: could this have been produced by a person who only heard a summary of the transcript? If yes, rewrite closer to the original speech.

Prefer the transcript's own sharp, specific wording over neutral explanatory paraphrase. Keep roughness when it carries meaning. Use editorial language only to connect preserved phrases into readable text.

## Pattern/model episode handling

When the transcript describes a workplace dysfunction or career pattern through named roles, stages, or components, produce a model-first article:

- introduce the model and its parts early;
- give each major part its own subsection only if that improves readability;
- distinguish the dysfunctional behavior from the healthy function it imitates;
- explain how the system or pattern forms without assuming everyone planned it consciously;
- address the obvious coping strategy and its limits;
- end with practical choices that follow from the transcript.

Do not reuse a fixed skeleton from previous posts. Build the structure from the current transcript.

## Formatting output

Return a complete Obsidian Markdown note: YAML frontmatter first, then the article body.

Use this YAML shape for the result file:

```yaml
---
type: podcast episode
subtype: post
project: Colleagues, not guys
season: (from outline)
episode: (from outline)
subtitle:
topics: (from outline)
source_outline: (the outline)
source_transcript: (the transcription)
prompt: [[05_CNG_Podcast_to_Post_Prompt]]
date: (today)
date_finished:
status: draft
public_urls:
---
```

For each episode, replace `season`, `episode`, `topics`, and `source_outline` from the outline note. Replace `source_transcript` with the transcript note. Use today's date for `date`. Keep `subtitle`, `date_finished`, and `public_urls` empty in the draft; title/subtitle/promo generation happens after the post draft is written. Keep `status: draft` until publication.

Do not wrap the final article in a code block unless the user explicitly asks for a code block.

Do not add a bibliography, author bio, social CTA, or explanatory note after the article.

## Final self-check

Before finalizing, verify silently:

- the central model appears early;
- headings reveal the argument, not just topics;
- repeated oral loops are deduplicated;
- bullets and `###` are used where they improve readability;
- the post keeps Anatoly's first-person stance, rough specificity, and original phrases;
- the article does not read like a retelling, presentation, or neutralized summary;
- practical advice follows from the story rather than being pasted on;
- no invented details, scenes, or generic management advice slipped in.

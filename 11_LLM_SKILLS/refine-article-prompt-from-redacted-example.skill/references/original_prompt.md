You are a professional prompt engineer.

Context:

- I have SOURCE MATERIAL (raw text).
- I have an ORIGINAL PROMPT that generates an article from that source.
- I have a REDACTED ARTICLE that represents the desired final quality (tone, style, structure, depth, clarity).

Your task:

1. Compare the likely output of the ORIGINAL PROMPT with the REDACTED ARTICLE.
2. Infer generalized, reusable patterns that explain how the REDACTED ARTICLE differs (e.g., tone/register, narrative structure, pacing, paragraph length, use of examples/analogies, level of abstraction, specificity, voice, rhetorical devices, transitions, headline/lede, intro/outro patterns, treatment of sources/facts).
3. Using those _generalized_ patterns, **rewrite the ORIGINAL PROMPT** so that—when applied to similar SOURCE MATERIAL—it naturally produces outputs close to the REDACTED ARTICLE **without further manual editing**.

Hard restrictions (very important):

- Do NOT include any explicit “from → to” word or phrase replacements.
- Do NOT include synonym lists, substitution tables, or any lexical find/replace guidance.
- Express changes as abstract, style/structure/process instructions only (e.g., “prefer active voice,” “open with a one-sentence hook,” “use concrete examples after claims,” “aim for 600–900 words,” “2–5 sentences per paragraph,” “neutral-professional tone with empathetic asides,” etc.).
- Do NOT quote long passages from the REDACTED ARTICLE; refer to patterns, not specific lines.

What the improved prompt must contain:

- Clear task description (write an article from SOURCE MATERIAL).
- Intended audience and purpose (inferred from REDACTED ARTICLE).
- Tone & voice guidelines (generalized).
- Structure template (hook, setup, body sections with logical sequence, summary/CTA).
- Style rules (sentence/paragraph length, transitions, vocabulary level, avoidance of clichés/filler).
- Evidence & rigor (when to define terms, when to add examples, when to compress).
- Length target and formatting requirements (headings, bullets, snippets if applicable).
- Quality checklist the model should self-verify before finalizing.

Inputs to expect at runtime for the improved prompt (make it robust to these):

- The SOURCE MATERIAL pasted after the prompt.

Output format for THIS task:

1. **IMPROVED PROMPT** — a single, reusable prompt in markdown code block I can copy-paste to generate future articles. It must NOT mention any specific word substitutions and must NOT rely on any “from → to” examples.
2. **RATIONALE (brief)** — 3–7 bullet points explaining the generalized stylistic/structural adjustments you made (no lexical examples, no word lists).

Now I will paste the materials in this exact order:

---SOURCE MATERIAL---
(paste the source here)
---ORIGINAL PROMPT---
(paste the original prompt here)
---REDACTED ARTICLE---
(paste the final edited article here)

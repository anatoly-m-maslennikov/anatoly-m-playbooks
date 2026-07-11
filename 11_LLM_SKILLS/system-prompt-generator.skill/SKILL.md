---
name: system-prompt-generator
description: Generate a production-ready system prompt for a specified LLM role, goal, audience, context, task type, output format, browsing/citation policy, and quality bar. Use when the user wants a reusable system/developer prompt and provides or needs help filling prompt parameters.
---

# System Prompt Generator

Generate reusable system/developer prompts by loading `references/system_prompt_generator_prompt.md` first; that reference is the authoritative prompt contract for inputs, defaults, section order, output rules, and validation.

## Workflow

1. Collect or infer goal, task type, domain, audience, context, source availability, browsing/citation policy, language, tone, output format/style/brevity/strictness, quality bar, non-goals, dates, timezone, examples, and preferred frameworks.
2. Ask only minimal targeted questions when critical inputs are missing; otherwise use the reference defaults.
3. Return only the generated system prompt, starting with `# System Prompt`, unless the user explicitly requests commentary.
4. Do not fabricate citations, source access, hidden context, or browsing results; follow the reference citation and browsing toggles.

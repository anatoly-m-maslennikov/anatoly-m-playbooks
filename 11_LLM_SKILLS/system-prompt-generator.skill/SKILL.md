---
name: system-prompt-generator
description: Generate a production-ready system prompt for a specified LLM role, goal, audience, context, task type, output format, browsing/citation policy, and quality bar. Use when the user wants a reusable system/developer prompt and provides or needs help filling prompt parameters.
---

# System Prompt Generator

Use this skill when the user wants a reusable system prompt for an assistant, workflow, domain, or task type.

Read `references/system_prompt_generator_prompt.md` before generating. It defines the input parameters, section order, output rules, and validation checklist.

## Workflow

1. Collect or infer the core inputs: goal, task type, domain, audience, context, source availability, browsing/citation policy, language, tone, output format, brevity, strictness, quality bar, non-goals, dates, and timezone.
2. If critical inputs are missing, ask the minimum targeted questions. Otherwise use defaults from the reference prompt.
3. Produce only the requested system prompt text, starting with `# System Prompt`, unless the user asks for commentary.
4. Do not fabricate citations or hidden source access.

## Reference

- `references/system_prompt_generator_prompt.md` — preserved generator prompt.

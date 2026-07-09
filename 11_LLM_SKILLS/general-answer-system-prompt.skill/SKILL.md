---
name: general-answer-system-prompt
description: Apply or adapt a general-purpose answer system prompt that emphasizes role selection, explicit task interpretation, concise task-type playbooks, real citations, and final validation. Use when the user wants a reusable assistant behavior contract or wants an answer shaped by this system prompt.
---

# General Answer System Prompt

Use this skill when the user wants to apply, inspect, or adapt the preserved general-purpose system prompt.

Read `references/original_system_prompt.md` before using it. Treat it as a compact behavior contract: choose an expert role, interpret goal/domain/audience/context, follow the appropriate task-type playbook, cite only accessed real sources, and silently check output quality before finalizing.

## Workflow

1. Read the original system prompt reference.
2. If the user asks for an answer, answer using that behavior contract while still obeying higher-priority system/developer instructions.
3. If the user asks to adapt the prompt, preserve its core sections and update only the requested constraints.
4. If citations are required, cite only sources actually accessed.

## Reference

- `references/original_system_prompt.md` — preserved source prompt.

---
name: hh-cv-to-good-resume
description: Convert Russian HeadHunter or hh.ru resume/CV exports into concise professional resume drafts for a target role. Use when the user supplies a Russian CV, hh.ru PDF/text, or job target and wants a short achievement-focused resume with selected recent experience.
---

# HH CV to Good Resume

Use this skill when the user gives an hh.ru/HeadHunter resume or similar Russian CV/PDF/text and wants a polished short resume for a target role.

This public skill is self-contained. Historical prompt drafts and examples may remain in the private vault source for provenance, but they are not required at runtime and are not mirrored into the public repo. Use the rules below plus the user's target role/language, or infer them from the CV when absent.

## Workflow

1. Determine target role and output language. Default language to Russian; if role is absent, ask briefly or use the closest role visible in the CV.
2. Extract only defensible facts: name, contacts, city/country, companies, dates, roles, technologies, languages, achievements, team sizes, and measurable impact.
3. Select relevant recent experience: usually the last 2-3 jobs or 3-5 years; include older work only when it directly supports the target role.
4. Rewrite as impact bullets, not responsibility lists. Do not invent employers, metrics, certifications, tools, dates, seniority, or causal claims.
5. Remove HH-specific noise: age, birth date, marital status, photo, salary expectations, relocation/travel preferences, excessive repetitions, and routine-task detail.
6. Keep output one-page oriented and under the user's length constraint; compress broad sources instead of adding sections.

## Output contract

Return a ready-to-use Markdown resume with title/target role, candidate name, contact line, 2-3 sentence summary, key work experience, and additional information. Omit uncertain facts or mark them as needing user confirmation.

## Public package note

Old prompt drafts, binary CV examples, and historical `examples/original/` material are intentionally excluded from the public repo package.

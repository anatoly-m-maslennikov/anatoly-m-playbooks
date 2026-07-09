---
name: hh-cv-to-good-resume
description: Convert Russian HeadHunter or hh.ru resume/CV exports into concise professional resume drafts for a target role. Use when the user supplies a Russian CV, hh.ru PDF/text, or job target and wants a short achievement-focused resume with selected recent experience.
---

# HH CV to Good Resume

Use this skill when the user gives an hh.ru/HeadHunter resume or similar Russian CV and wants a polished short resume for a target role.

Read `references/original/hh_cv_to_good_resume_10_years_exp_prompt.md` before drafting. Treat it as the source prompt unless the user gives newer constraints.

## Workflow

1. Identify the target role from the user request. If absent, ask briefly or use the closest role visible in the CV.
2. Identify desired output language. Default to Russian unless the user asks otherwise.
3. Extract only defensible facts from the CV: names, contacts, companies, dates, roles, technologies, languages, achievements, team sizes, and measurable impact.
4. Select the most relevant recent experience for the target role. Prefer the last 2-3 jobs or 3-5 years, and include older experience only when it directly supports the target role.
5. Rewrite bullets as achievements and impact, not responsibilities. Do not invent employers, metrics, certifications, tools, or seniority.
6. Keep the final resume short and one-page oriented. If the source is too broad, compress rather than adding sections.

## Output contract

Return a ready-to-use Markdown resume with header, contact line, summary, key work experience, and additional information. If a fact is missing or uncertain, omit it or mark it as needing user confirmation rather than hallucinating.

## References

- `references/original/hh_cv_to_good_resume_10_years_exp_prompt.md` — original reusable prompt.
- `references/original/hh_cv_to_good_resume_10_years_exp_about.md` — original short about note.
- `examples/original/` — preserved example output from the previous prompt folder.

# Contributor Guide

This guide explains how contributors should design, revise, and validate skills in `open-translation`.

## Project Shape

Current public surface:

- `skills/<skill-name>/SKILL.md`

Future surfaces may include `mcp/`, `web/`, or shared core modules, but contributions should follow the current repo structure unless maintainers expand it.

## What Good Contributions Look Like

- one clear improvement at a time
- concise skill instructions
- low duplication across skills
- explicit scope boundaries
- examples only when they materially improve behavior
- output quality that sounds human, not generic AI translation

## Skill Design Rules

- Keep each skill focused on one main job.
- Prefer task-type boundaries over language-pair folder explosion.
- Keep runtime-safety rules in the skills that need them.
- Put cross-cutting guidance in separate skills instead of copying it into every skill.
- Use YAML frontmatter with `name` and `description`.

## Before You Change A Skill

Check:

- does this conflict with a recorded [project decision](../../DECISIONS.md)?
- does this belong in an existing skill, or is it a different failure mode?
- does this increase overlap with a sibling skill?
- is this rule public and reusable, or only local/private workflow?

## Public Vs Private Material

Public repo content:

- `AGENTS.md`
- `README.md`
- `docs/contributors/CONTRIBUTING.md`
- `docs/contributors/README.md`
- `docs/end-users/README.md`
- `LICENSE`
- `skills/`

Local-only content:

- `.local/`

Do not add `.local/` files to git. Contributors should not depend on local-only planning or eval notes to understand the public repo.

## Skill Workflow

Treat every new skill and every meaningful skill revision as something that should be evaluated, not just written.

The intended loop is:

1. Identify the target skill or propose a new one.
2. Keep the edit narrow.
3. Re-read sibling skills for overlap.
4. Make sure the skill still reads cleanly end to end.
5. Run a small set of representative eval cases.
6. Record recurring weaknesses.
7. Revise the skill only when the same weakness appears across multiple cases.
8. Stop revising when new cases mostly confirm expected behavior instead of exposing new systematic problems.

For this repo stage, the main goal of evaluation is to answer:

- does the skill actually improve output quality?
- what failure modes still repeat?
- is the problem scope, wording guidance, or terminology policy?

## Evaluation Expectations

Use this rule of thumb:

1. Start with a few representative cases, not a huge dataset.
2. Prefer real examples when possible.
3. If you are using a local eval workspace, add or update a case or run note.
4. If a skill is improved but not fully proven stable, mark it as monitored rather than pretending it is finished.

## Model Notes

Model choice matters for contributors because it changes how well a skill follows instructions, preserves structure, and produces natural translation. Do not assume that results from one strong model automatically generalize to weaker ones.

Preferred approach:

- think in terms of capability, not one fixed model name
- record which model was used when running meaningful evals
- be cautious about declaring a skill solid if it has only been exercised on one high-end model

Recommended capability profile:

- strong instruction following
- strong bilingual translation quality
- good structural reliability for locale and docs tasks
- good rewriting ability for natural target-language output

## Pull Request Notes

- Explain the problem being fixed.
- Explain why the change belongs in that skill.
- Mention any overlap or terminology tradeoffs.
- Keep PRs small when possible.

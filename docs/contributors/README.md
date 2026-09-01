# Contributor Guide

This guide explains how contributors should design, revise, and validate skills in `open-writing`.

## Project Shape

Current public surface:

- `skills/<skill-name>/SKILL.md`
- `docs/routing.md` for skill selection and composition rules

Future surfaces may include `mcp/`, `web/`, or shared core modules. Follow the current repo structure unless maintainers expand it.

The project supports translation alongside first-class same-language writing and rewriting.

## What Good Contributions Look Like

- one clear improvement at a time
- concise skill instructions
- low duplication across skills
- explicit scope boundaries
- routing that remains understandable to an agent
- examples only when they materially improve behavior
- output quality that sounds human, not generically professional or AI-written

## Skill Design Rules

- Keep each skill focused on one main job.
- Route from the user's requested operation first: translation, same-language writing/rewrite, review, or cleanup.
- After operation, choose by content/domain and then apply format or structural constraints.
- Treat formats such as Markdown, MDX, JSON, and YAML as constraints, not automatic task types.
- Distinguish primary skills from companion skills. A companion skill should not become a fallback for a missing primary capability.
- Keep runtime-safety rules in the skills that need them.
- Put cross-cutting guidance in separate skills instead of copying it into every skill.
- Use the smallest useful composition rather than requiring every task to run through multiple passes.
- Use YAML frontmatter with `name` and `description`.
- Read `docs/routing.md` before adding a new skill category or changing an existing skill's routing role.

## Before You Change A Skill

Check:

- does this conflict with a recorded [project decision](../../DECISIONS.md)?
- does this belong in an existing skill, or is it a different failure mode?
- what operation is this skill responsible for?
- is it a primary transformation or a companion review/cleanup pass?
- is this a content/domain problem or only a format constraint?
- does this increase overlap with a sibling skill?
- is this rule public and reusable, or only local/private workflow?
- has the pattern repeated across representative cases, or is it one project preference?

## Public Vs Private Material

Public repo content:

- `AGENTS.md`
- `CONTRIBUTING.md`
- `DECISIONS.md`
- `README.md`
- `docs/routing.md`
- `docs/contributors/README.md`
- `docs/end-users/README.md`
- `LICENSE`
- `skills/`

Local-only content:

- `.local/`

Do not add `.local/` files to git. Contributors should not depend on local-only planning or eval notes to understand the public repo.

## Skill Workflow

Evaluate every new skill and every meaningful skill revision. Do not treat the instructions alone as proof that the behavior works.

The intended loop is:

1. Identify the requested operation and target skill, or propose a new one when a real capability gap exists.
2. Keep the edit narrow.
3. Re-read `docs/routing.md` and sibling skills for overlap.
4. Make sure the skill still reads cleanly end to end.
5. Run a small set of representative eval cases.
6. Record recurring weaknesses and their project or domain context.
7. Revise the public skill only when the same weakness appears across representative cases.
8. Stop revising when new cases mostly confirm expected behavior instead of exposing new systematic problems.

For this repo stage, the main goal of evaluation is to answer:

- does the skill actually improve output quality?
- what failure modes still repeat?
- is the problem routing, scope, wording guidance, structure, or terminology policy?
- did a companion pass improve the result, or merely over-process it?

## Evaluation Expectations

Use this rule of thumb:

1. Start with a few representative cases, not a huge dataset.
2. Prefer real examples when possible.
3. If you are using a local eval workspace, add or update a case or run note.
4. If a skill is improved but not fully proven stable, mark it as monitored rather than pretending it is finished.
5. Before generalizing project-specific wording, confirm the failure mode on another representative case when practical.
6. Compare single-skill and composed workflows when introducing a new companion relationship.

## Automated validation

Before you open a pull request, validate the public skill structure:

```shell
python3 .github/validate-skills.py
```

The validator checks that every skill has a non-empty `SKILL.md`, includes the required frontmatter fields, and uses the same name as its directory.
GitHub Actions runs the same check for every pull request and change to `main`.

The structural validator does not prove that routing or behavior is correct. Review `docs/routing.md`, sibling boundaries, and representative output separately.

## Model Notes

Model choice matters because it affects instruction following, structural preservation, translation quality, and rewriting behavior. Do not assume that results from one strong model automatically generalize to weaker ones.

Preferred approach:

- think in terms of capability, not one fixed model name
- record which model was used when running meaningful evals
- record reasoning or runtime settings when they materially affect results
- be cautious about declaring a skill solid if it has only been exercised on one high-end model
- watch for model-default professionalization when evaluating editorial rewriting

Recommended capability profile:

- strong instruction following
- strong bilingual translation quality for translation tasks
- good structural reliability for locale and docs tasks
- good rewriting ability for natural target-language and same-language output
- ability to preserve uncertainty, evidence boundaries, and writer voice

## Pull Request Notes

- Explain the problem being fixed.
- Describe the evidence or repeated failure mode behind the change.
- Explain why the change belongs in that skill.
- Mention routing impact, sibling overlap, terminology tradeoffs, and format constraints.
- Mention the validation and representative evals you ran.
- Keep PRs small when possible.

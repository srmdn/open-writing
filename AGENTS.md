# AGENTS.md — open-writing

## Purpose

- Build open writing and translation skills for humans, AI agents, and developers.
- Treat English <-> Indonesian as the first translation quality benchmark.
- Keep skills focused and compose them by requested operation, content/domain, and constraints.

## Repository structure

- Store installable skills in `skills/<skill-name>/SKILL.md`.
- Store routing guidance in `docs/routing.md`.
- Store public guidance in `docs/end-users/` and `docs/contributors/`.
- Record durable public choices in `DECISIONS.md`.
- Reserve `mcp/`, `web/`, and shared modules for approved future work.
- Keep optional private planning and evaluation under `.local/`.

## Skill rules

- Keep each `SKILL.md` concise, targeted, and limited to one main job.
- Use YAML frontmatter with clear `name` and `description` fields.
- Preserve existing skill names unless a rename includes repo-wide follow-through.
- Prefer a new skill when adding guidance would blur an existing boundary.
- Keep terminology and safety rules close to the skill that needs them.
- Treat language direction as runtime input, not a folder-level assumption.
- Route from the user's requested operation first: translation, same-language writing/rewrite, review, or cleanup.
- After operation, choose by content/domain and then apply format or structural constraints.
- Treat formats such as Markdown, MDX, JSON, and YAML as constraints, not automatic task types.
- Distinguish primary skills from companion skills. Do not use `anti-slop-writing` or `translation-review` as universal fallbacks for a missing primary capability.
- Use the smallest useful composition. Do not run every output through every available skill.
- Prefer examples over repeated or abstract explanation.

## Routing

Read `docs/routing.md` before adding a new skill category or changing how an existing skill is selected.

Current primary skills perform the main transformation:

- `editorial-writing`
- `general-translation`
- `technical-docs-translation`
- `locale-translation`
- `marketing-translation`
- `subtitle-translation`
- `religious-content-translation`

Current companion skills perform narrower review or cleanup jobs:

- `anti-slop-writing`
- `translation-review`

## Workflow

- Treat `skills/` as the source of truth for writing and translation behavior.
- Read `DECISIONS.md` before changing public scope or architecture.
- If present, read `.local/PRD.md` and `.local/ROADMAP.md` before expanding product surfaces or skill categories.
- If present, read `.local/WORKFLOW.md` for maintainer-local execution rules.
- Refine skills through sample -> score -> finding -> narrow revision.
- Revise for repeated weaknesses, not isolated wording preferences.
- Treat skills as living beta behavior definitions that can evolve through real use.
- Promote a project finding into public guidance only when representative cases show that the failure mode recurs. Keep project-specific preferences local.
- Keep public changes focused and explain validation in the pull request.
- Follow `docs/contributors/README.md` for the contribution process.

## Quality and validation

- Preserve meaning, tone, domain accuracy, evidence boundaries, and runtime-sensitive structure.
- Produce natural writing without generic AI phrasing or unnecessary professionalization.
- Review frontmatter, scope boundaries, sibling overlap, routing impact, and examples.
- For meaningful skill changes, update an eval case or run note when `.local/eval/` is available.
- Run relevant tests, lint, format checks, and skill validation before commit.

## Private workspace

- Keep `.local/` out of git and out of the public repository contract.
- Never stage private evals, plans, or unrelated user changes.
- Ensure public contributors can work without local-only files.

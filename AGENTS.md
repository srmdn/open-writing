# AGENTS.md — open-translation

## Purpose

- Build open translation tools for humans, AI agents, and developers.
- Treat English <-> Indonesian as the first quality benchmark.
- Keep skills focused and compose them by task type.

## Repository structure

- Store installable skills in `skills/<skill-name>/SKILL.md`.
- Store public guidance in `docs/end-users/` and `docs/contributors/`.
- Record durable public choices in `DECISIONS.md`.
- Reserve `mcp/`, `web/`, and shared modules for approved future work.
- Keep optional private planning and evaluation under `.local/`.

## Skill rules

- Keep each `SKILL.md` concise, targeted, and limited to one main job.
- Use YAML frontmatter with clear `name` and `description` fields.
- Preserve existing skill names unless a rename includes repo-wide
  follow-through.
- Prefer a new skill when adding guidance would blur an existing boundary.
- Keep terminology and safety rules close to the skill that needs them.
- Treat language direction as runtime input, not a folder-level assumption.
- Prefer examples over repeated or abstract explanation.

## Workflow

- Treat `skills/` as the source of truth for translation behavior.
- Read `DECISIONS.md` before changing public scope or architecture.
- If present, read `.local/PRD.md` and `.local/ROADMAP.md` before expanding
  product surfaces or skill categories.
- Refine skills through sample -> score -> finding -> narrow revision.
- Revise for repeated weaknesses, not isolated wording preferences.
- Keep public changes focused and explain validation in the pull request.
- Follow `docs/contributors/README.md` for the contribution process.

## Quality and validation

- Preserve meaning, tone, domain accuracy, and runtime-sensitive structure.
- Produce natural target-language writing without generic AI phrasing.
- Review frontmatter, scope boundaries, sibling overlap, and examples.
- For meaningful skill changes, update an eval case or run note when
  `.local/eval/` is available.
- Run relevant tests, lint, format checks, and skill validation before commit.

## Private workspace

- Keep `.local/` out of git and out of the public repository contract.
- Never stage private evals, plans, or unrelated user changes.
- Ensure public contributors can work without local-only files.

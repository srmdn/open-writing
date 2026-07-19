# AGENTS.md — open-translation

## Purpose

- Monorepo for open translation tools, starting with strong English <-> Indonesian support.
- Keep each skill focused. One skill, one main job.
- Prefer composition over one large mixed-purpose skill.
- Keep the project free and open for humans, AI agents, and developers.

## Repo Layout

- `skills/<skill-name>/SKILL.md` for each installable skill
- `docs/end-users/` for public end-user documentation
- `docs/contributors/` for public contributor documentation
- optional local-only workspace under `.local/`
  - `.local/PRD.md` for private product definition
  - `.local/ROADMAP.md` for private sequencing and milestones
  - `.local/eval/` for private evaluation cases, rubric, and run logs
- Reserve room for future `mcp/`, `web/`, and shared core modules if the repo expands
- Avoid extra docs inside skill folders unless required by the skill design
- Keep root docs minimal: repo entry files such as `README.md`, `LICENSE`, and `AGENTS.md`
- Place audience-specific public docs under `docs/end-users/` and `docs/contributors/`

## Skill Design Rules

- Keep `SKILL.md` concise and targeted
- Use clear YAML frontmatter with `name` and `description`
- Do not duplicate large guidance blocks across multiple skills
- Put cross-cutting guidance in a separate reusable skill instead of copying it everywhere
- Prefer examples over long explanation when one example is enough
- Keep scope boundaries explicit: general prose, technical docs, locale/i18n, marketing, subtitle, religious content, anti-slop, review
- Prefer task-based skill boundaries over language-pair-specific folder explosion

## Workflow

- Treat `open-translation/skills` as the source of truth for future translation work
- If present, read `.local/PRD.md` before making scope changes
- If present, read `.local/ROADMAP.md` before adding new surfaces or major new skill categories
- If present, use `.local/eval/` to validate skill quality with real cases before broadening scope
- Prefer eval-driven refinement: real sample -> score -> findings -> skill update
- Do not treat a skill as solid just because the `SKILL.md` reads well; it must survive evaluation
- Keep public changes focused and use a short-lived branch so `main` stays
  healthy
- Validate changes before commit and include the problem, scope, and validation
  evidence in the pull request
- Merge only after relevant checks and review are complete
- Follow `docs/contributors/README.md` for the public contribution process

## Editing Rules

- Preserve existing skill names unless intentionally renaming with repo-wide follow-through
- Do not broaden a skill casually; create a new skill when scope or failure mode is materially different
- Keep terminology rules close to the skill that needs them
- Keep runtime-safety rules in locale/i18n skills, not general prose skills
- Keep code/Markdown safety rules in technical-doc skills, not general prose skills
- Design for language direction as a parameter where practical, not a hardcoded repo assumption

## Quality Bar

- Output should read human, not generic AI translation
- Preserve meaning, tone, and domain accuracy
- Avoid AI-sounding filler, stiffness, and repetitive structure
- Do not sacrifice structural safety for style improvements
- Indonesian quality is the first-class benchmark, but repo structure should stay extensible to other languages

## Validation

- For skill changes, review:
  - frontmatter clarity
  - scope boundaries
  - overlap with sibling skills
  - examples and wording rules
- For meaningful skill changes, add or update at least one eval case or run note in `.local/eval/` when that local workspace is being used
- If repo automation exists later, run tests/lint before commit

## Private Docs

- `.local/` is optional and local-only
- Keep `.local/` out of git
- Private planning, eval notes, and working product docs belong in `.local/`
- Public contributors should be able to work without any `.local/` files
- Do not move private eval material into public skill folders

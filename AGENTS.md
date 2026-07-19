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

## Autonomous contribution workflow

Use this workflow automatically for any authorized task that produces public
tracked changes. Once the user asks for a change, complete the routine
branch-to-merge lifecycle without asking for separate prompts between steps. A
user instruction to avoid commits, pushes, pull requests, or merges overrides
this default.

1. Start from an up-to-date `main`.
2. Before editing, create a short-lived branch named
   `codex/<short-task-name>`. If already on the correct task branch, continue
   there.
3. Read the relevant public files and private anchors before changing scope or
   skill behavior.
4. Make the smallest change that solves the evidenced problem.
5. For meaningful skill changes:
   - add or update a private eval case or run note when `.local/eval/` is
     available
   - run a clean follow-up after a behavior revision
   - revise again only when evidence still shows a repeated weakness
6. Run validation proportional to the change, including skill validation,
   format checks, tests, lint, or eval scoring when available.
7. If validation fails, keep working on the same branch until it passes or a
   genuine blocker requires user input.
8. Stage only task-scoped public files. Never stage `.local/` or unrelated user
   changes.
9. Commit with a concise descriptive message, then push the task branch.
10. Open a ready pull request that explains:
    - the problem
    - why the change belongs in its current scope
    - validation performed
    - relevant eval outcome without exposing private eval material
11. Monitor required checks and review state. Fix failures on the same branch
    and push follow-up commits automatically.
12. Merge into `main` when checks pass, no unresolved review issue remains, and
    the final diff is still task-scoped. Prefer squash merge unless repo policy
    or the user requests another strategy.
13. Delete the merged task branch when practical, switch back to `main`, update
    it, and verify the worktree is clean.

Do not pause for routine branch creation, validation, staging, commits, pushes,
pull-request creation, check monitoring, or merge after the original change
request authorizes the workflow. Pause only when:

- credentials or tool approval are unavailable
- a destructive or irreversible action falls outside the requested scope
- requirements are materially ambiguous
- validation exposes a product decision the agent cannot safely make
- merge conflicts or review feedback require user judgment

Keep `main` as the healthy baseline. Do not commit public work directly to
`main` unless the user explicitly requests it or an established emergency
policy requires it.

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

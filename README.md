# open-writing

Open writing and translation skills for humans, AI agents, and developers.

Initial translation quality target:

- English <-> Indonesian

The goal is not generic machine translation or generic AI rewriting. The goal is output that is:

- natural
- human-sounding
- faithful to supported meaning and evidence
- structurally safe when format matters
- reusable across agent workflows and future tooling

## Current Scope

The repo contains two first-class operation families:

- same-language writing and rewriting
- translation

It also contains narrower companion skills for review and cleanup.

Available public skills:

### Primary writing

- `editorial-writing`

### Primary translation

- `general-translation`
- `technical-docs-translation`
- `locale-translation`
- `marketing-translation`
- `subtitle-translation`
- `religious-content-translation`

### Companion skills

- `anti-slop-writing`
- `translation-review`

The intended model is:

```text
operation -> content/domain -> constraints -> primary skill -> optional companion
```

See [docs/routing.md](./docs/routing.md) for the routing contract.

## Principles

- keep each skill focused
- prefer composition over one large mixed-purpose skill
- route from the requested operation before content type or file format
- distinguish primary transformation skills from narrow review/cleanup skills
- preserve meaning, tone, evidence boundaries, and domain accuracy
- avoid AI-sounding filler, stiffness, and over-professionalized prose
- keep code, Markdown, locale tokens, and other runtime-sensitive structure safe
- use evaluation to refine skills, not only intuition
- use the smallest useful skill composition rather than running every pass by default

## Audience Docs

- Routing: [docs/routing.md](./docs/routing.md)
- End users: [docs/end-users/README.md](./docs/end-users/README.md)
- Contributors: [docs/contributors/README.md](./docs/contributors/README.md)
- Contribution policy: [CONTRIBUTING.md](./CONTRIBUTING.md)
- Project decisions: [DECISIONS.md](./DECISIONS.md)

## How To Use

Current reality:

- this repo ships instruction skills
- it does not yet ship MCP tools or a web app

Today, the main way to use the repo is to apply one or more focused skills in an AI agent workflow such as Codex, ChatGPT, or Claude.

Basic flow:

1. Identify what the user wants done: translation, same-language writing/rewrite, review, or cleanup.
2. Choose the primary skill from the content/domain and constraints.
3. Add a companion skill only when the task actually needs a separate review or cleanup pass.

Quick examples:

- translate everyday prose or an editorial article -> `general-translation`
- translate developer-facing docs or code-sensitive Markdown/MDX -> `technical-docs-translation`
- translate locale strings or UI copy -> `locale-translation`
- translate campaigns or CTA-heavy copy -> `marketing-translation`
- translate spoken on-screen dialogue -> `subtitle-translation`
- translate religious or reverent material -> `religious-content-translation`
- substantively rewrite an existing article or explainer -> `editorial-writing`
- make already-sound wording less generic or stiff -> `anti-slop-writing`
- compare a source with an existing translation -> `translation-review`

Choose by operation and content, not file extension alone.

## Repo Layout

```text
skills/
  <skill-name>/
    SKILL.md
AGENTS.md
CONTRIBUTING.md
DECISIONS.md
docs/
  routing.md
  contributors/
    README.md
  end-users/
    README.md
LICENSE
```

Local/private planning and evaluation may exist under `.local/`, but that workspace is optional and not part of the public repo contract.

## Status

Current state:

- translation skill set scaffolded and refined through evaluation
- `editorial-writing` introduced as the first primary same-language writing skill
- operation-first routing documented
- `anti-slop-writing` retained as a focused cleanup companion rather than a universal article editor
- private planning and evaluation may exist in the maintainer's local workspace

Planned later:

- expand writing skills only when representative evaluation shows a real capability gap
- MCP surface
- web surface
- broader language coverage

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md) for contribution policy and [docs/contributors/README.md](./docs/contributors/README.md) for the working process.

Short version:

- keep edits narrow
- avoid duplicating guidance across skills
- preserve clear scope boundaries
- route by operation before domain and format
- optimize for human-sounding output, not generic prompt bloat

## License

[Apache-2.0](./LICENSE)

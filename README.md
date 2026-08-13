# open-translation

Open translation skills and tooling for humans, AI agents, and developers.

Initial quality target:

- English <-> Indonesian

The goal is not generic machine translation. The goal is translation that is:

- natural
- human-sounding
- structurally safe when format matters
- reusable across agent workflows and future tooling

## Current Scope

This repo currently focuses on task-based translation skills.

Available public skills:

- `general-translation`
- `technical-docs-translation`
- `locale-translation`
- `marketing-translation`
- `subtitle-translation`
- `religious-content-translation`
- `anti-slop-writing`
- `translation-review`

The project is organized by task type, not by language-pair folder explosion.

That means the intended model is:

- task type as the main skill boundary
- source language and target language as runtime inputs

## Principles

- keep each skill focused
- prefer composition over one large mixed-purpose skill
- preserve meaning and tone
- avoid AI-sounding filler and stiffness
- keep code, Markdown, locale tokens, and other runtime-sensitive structure safe
- use evaluation to refine skills, not only intuition

## Audience Docs

- End users: [docs/end-users/README.md](./docs/end-users/README.md)
- Contributors: [docs/contributors/README.md](./docs/contributors/README.md)
- Contribution policy: [docs/contributors/CONTRIBUTING.md](./docs/contributors/CONTRIBUTING.md)
- Project decisions: [DECISIONS.md](./DECISIONS.md)

## How To Use

Current reality:

- this repo ships translation skills
- it does not yet ship MCP tools or a web app

Today, the main way to use `open-translation` is to apply one skill in an AI agent workflow such as Codex, ChatGPT, or Claude.

Basic flow:

1. Pick the skill that matches your task.
2. Give the model your source text plus source and target language.
3. Tell the model to use that skill for the translation.
4. For sensitive output, follow with `translation-review`.

Quick skill chooser:

Choose by task and content, not by file extension alone.

- everyday prose or chat: `general-translation`
- developer-facing docs or code-sensitive Markdown/MDX:
  `technical-docs-translation`
- locale strings or UI copy: `locale-translation`
- campaigns or CTA-heavy copy: `marketing-translation`
- spoken on-screen dialogue: `subtitle-translation`
- religious or reverent material: `religious-content-translation`
- make writing sound less generic: `anti-slop-writing`
- compare a source with an existing translation: `translation-review`

For examples and practical usage notes, see [docs/end-users/README.md](./docs/end-users/README.md).

## Repo Layout

```text
skills/
  <skill-name>/
    SKILL.md
AGENTS.md
DECISIONS.md
docs/
  contributors/
    CONTRIBUTING.md
    README.md
  end-users/
    README.md
LICENSE
```

Local/private planning and evaluation may exist under `.local/`, but that workspace is optional and not part of the public repo contract.

## Status

Current state:

- initial skill set scaffolded
- private PRD and roadmap in local workspace
- private evaluation harness seeded with real OSS translation cases
- first evaluation-driven refinements already applied to core translation skills

Planned later:

- MCP surface
- web surface
- broader language coverage

## Contributing

See [docs/contributors/CONTRIBUTING.md](./docs/contributors/CONTRIBUTING.md) for contribution policy and [docs/contributors/README.md](./docs/contributors/README.md) for working process.

Short version:

- keep edits narrow
- avoid duplicating guidance across skills
- preserve clear scope boundaries
- optimize for human-sounding output, not generic prompt bloat

## License

[Apache-2.0](./LICENSE)

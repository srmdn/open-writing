# End Users

`open-writing` is a writing and translation skill set for humans and AI users who want natural output, preserved meaning, and structurally safe handling when format matters.

## How To Use It Today

Current public repo state:

- this is a skills repo
- it is not yet a hosted app
- it does not yet expose MCP tools

That means current usage is manual: use these skills inside an AI tool that supports instruction-following well.

Start from what you want the model to do:

1. translation
2. same-language writing or rewriting
3. review
4. cleanup/humanization

Then choose the content/domain skill and any needed structural constraints.

See [../routing.md](../routing.md) for the full routing contract.

## Picking The Right Skill

### Same-language writing or rewriting

Use:

- `editorial-writing` for articles, essays, explainers, technical-popular writing,
  opinion pieces, and experience-based long-form prose when structure, headings,
  flow, voice, or reader progression need substantive work

Optional:

- `anti-slop-writing` after the editorial pass when the result is structurally
  sound but still feels generic, stiff, over-polished, or AI-sounding

### Translation

Use:

- `general-translation` for everyday prose, articles, chat, and editorial text,
  including articles stored in Markdown
- `technical-docs-translation` for README files, API guides, tutorials, and
  developer-facing Markdown or MDX where code-sensitive structure matters
- `locale-translation` for JSON/YAML locale files, UI strings, placeholders, and tags
- `marketing-translation` for persuasive copy, launches, announcements, and CTAs
- `subtitle-translation` for spoken dialogue meant to be read quickly on screen
- `religious-content-translation` for religious, devotional, or reverent material

Optional companions:

- `translation-review` when the goal is to compare a source with an existing translation
- `anti-slop-writing` when an otherwise accurate translation still sounds generic or stiff

### Cleanup only

Use `anti-slop-writing` directly when the wording is already structurally sound and the actual request is only to make it less generic, stiff, translated, over-polished, or AI-sounding.

Do not use it as a substitute for `editorial-writing` when the article still needs substantive editorial work.

## Prompt Patterns

Same-language article rewrite:

```text
Use the `editorial-writing` skill.

Audience: technical readers
Goal: improve structure, headings, flow, and voice without changing factual claims.

Rewrite this article:
...
```

General translation:

```text
Use the `general-translation` skill.

Source language: Indonesian
Target language: English
Goal: natural product-help copy

Translate this text:
...
```

Technical docs translation:

```text
Use the `technical-docs-translation` skill.
Source language: English
Target language: Indonesian
Preserve Markdown and code exactly.

Translate this README section:
...
```

Cleanup pass:

```text
Use the `anti-slop-writing` skill.

Keep the meaning and evidence boundaries unchanged.
Make this draft sound less generic, stiff, and AI-written:
...
```

Translation review:

```text
Use the `translation-review` skill.
Source language: Indonesian
Target language: English

Review this translation for fidelity, naturalness, and domain fit.
Point out real issues only, then suggest a better version.

Source text:
...

Existing translation:
...
```

## Tool-Specific Setup

Current setup is lightweight and manual. This repo does not yet ship a one-click installer, MCP server, or hosted UI.

### Codex

- Open this repo in your Codex workspace.
- Read `docs/routing.md` when the correct skill is not obvious.
- Read the relevant `skills/<skill-name>/SKILL.md`.
- Tell Codex to use that skill for your task.
- Include task context such as audience, tone, domain, source/target language when translating, and format constraints.

### ChatGPT

- Open `docs/routing.md` when the correct skill is not obvious.
- Open the relevant `SKILL.md` file from this repo.
- Paste or adapt the skill instruction into your chat.
- Add your text and task request below it.

### Claude

- Open `docs/routing.md` when the correct skill is not obvious.
- Open the relevant `SKILL.md` file from this repo.
- Paste or adapt the skill instruction into your conversation.
- Add task context such as tone, domain, and structural constraints.

## What To Expect

The project is optimized for:

- human-sounding writing and translation
- substantive editorial rewriting without flattening writer voice
- better handling of structure-sensitive content such as locale strings and technical docs
- task-based behavior instead of one generic writing or translation mode
- narrow cleanup and review passes that are composed only when useful

## Quality Expectations

The goal is output that is:

- faithful to supported meaning and evidence
- natural for the intended audience
- structurally safe when tokens, markup, or code matter
- specific rather than generically professional

## Limitations

Quality can still vary depending on:

- the requested operation
- the content/domain
- source and target language direction for translation
- terminology policy for the domain
- the model or runtime behind the tool

For sensitive or terminology-heavy content, review may still be useful even when the output is already strong.

## Current Project State

The repo is still focused on skill design and evaluation rather than a polished end-user product.

Planned later:

- expand writing skills only when representative evaluation shows a real capability gap
- MCP tools
- web interface
- broader language coverage

# End Users

`open-translation` is intended to become a translation toolset for humans and AI users who want output that sounds natural, preserves meaning, and stays structurally safe when format matters.

## How To Use It Today

Current public repo state:

- this is a skills repo
- it is not yet a hosted app
- it does not yet expose MCP tools

That means current usage is manual: use these skills inside an AI tool that supports instruction-following well.

Typical flow:

1. Choose the task type that matches your text.
2. Provide source text plus source and target language.
3. Ask the model to use the matching `open-translation` skill.
4. If quality matters more than speed, run a second pass with `translation-review`.

## Picking The Right Skill

Choose by task and content, not by file extension alone.

Use:

- `general-translation` for everyday prose, articles, chat, and editorial text,
  including articles stored in Markdown
- `technical-docs-translation` for README files, API guides, tutorials, and
  developer-facing Markdown or MDX where code-sensitive structure matters
- `locale-translation` for JSON/YAML locale files, UI strings, placeholders, and tags
- `marketing-translation` for persuasive copy, launches, announcements, and CTAs
- `subtitle-translation` for spoken dialogue meant to be read quickly on screen
- `religious-content-translation` for religious, devotional, or reverent material
- `anti-slop-writing` when the goal is to make wording less generic or stiff
- `translation-review` when the goal is to compare a source with an existing
  translation

## Prompt Pattern

Use a prompt shape like:

```text
Use the `general-translation` skill.

Source language: Indonesian
Target language: English
Goal: natural product-help copy

Translate this text:
...
```

Add context when useful:

- audience
- tone
- domain
- format constraints
- terminology that must stay unchanged

## Tool-Specific Setup

Current setup is lightweight and manual. This repo does not yet ship a one-click installer, MCP server, or hosted UI.

### Codex

- Open this repo in your Codex workspace.
- Read the relevant `skills/<skill-name>/SKILL.md`.
- Tell Codex to use that skill for your task.
- Include source text, source language, target language, and any format constraints.

### ChatGPT

- Open the relevant `SKILL.md` file from this repo.
- Paste or adapt the skill instruction into your chat.
- Add your source text and translation request below it.

### Claude

- Open the relevant `SKILL.md` file from this repo.
- Paste or adapt the skill instruction into your conversation.
- Add task context such as tone, domain, and structural constraints.

### Current Limitation

- usage is manual today
- exact loading flow depends on your AI tool
- future MCP and web surfaces should reduce this setup friction

## Examples

General prose:

```text
Use the `general-translation` skill.
Source language: English
Target language: Indonesian
Tone: natural and warm

Translate:
"I saved your draft so you can come back to it later."
```

Technical docs:

```text
Use the `technical-docs-translation` skill.
Source language: English
Target language: Indonesian
Preserve Markdown and code exactly.

Translate this README section:
...
```

Locale strings:

```text
Use the `locale-translation` skill.
Source language: English
Target language: Indonesian
Keep keys, placeholders, and tags unchanged.

Translate this JSON:
...
```

Review pass:

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

## What To Expect

The project is optimized for:

- human-sounding translation
- better handling of structure-sensitive content such as locale strings and technical docs
- task-based behavior instead of one generic translation mode

Current task types include:

- general translation
- technical docs translation
- locale translation
- marketing translation
- subtitle translation
- religious content translation
- anti-slop rewriting
- translation review

## Quality Expectations

The goal is not just correctness. The goal is output that is:

- faithful to the source
- natural in the target language
- structurally safe when tokens, markup, or code matter

## Limitations

Quality can still vary depending on:

- the task type
- the source and target language direction
- terminology policy for the domain
- the model or runtime behind the tool

For sensitive or terminology-heavy content, review may still be useful even when the output is already strong.

## Current Project State

The repo is still focused on skill design and evaluation rather than a polished end-user product.

Planned later:

- MCP tools
- web interface
- broader language coverage

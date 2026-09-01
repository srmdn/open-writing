# Skill Routing

Choose skills from the user's requested operation first, then the content/domain, then any structural or review constraints.

The routing order is:

```text
operation -> content/domain -> constraints -> primary skill -> optional companion skill
```

Do not route from file extension alone. Markdown, MDX, JSON, and other formats are constraints unless the user's actual task is defined by that format.

## Primary and companion skills

Primary skills perform the main requested transformation.

Current primary skills:

- `editorial-writing`
- `general-translation`
- `technical-docs-translation`
- `locale-translation`
- `marketing-translation`
- `subtitle-translation`
- `religious-content-translation`

Companion skills perform a narrower review or cleanup job and should not replace the appropriate primary skill.

Current companion skills:

- `anti-slop-writing`
- `translation-review`

Use companion skills only when the task needs them. Do not automatically run every output through every available pass.

## 1. Translation

If the user wants text translated between languages, select the translation skill from the content and constraints.

- ordinary prose, articles, essays, or editorial text -> `general-translation`
- developer-facing documentation, README files, API guides, or code-sensitive docs -> `technical-docs-translation`
- locale files, UI strings, placeholders, or runtime-sensitive interface copy -> `locale-translation`
- persuasive marketing or campaign copy -> `marketing-translation`
- spoken dialogue, captions, or subtitles -> `subtitle-translation`
- religious, devotional, or doctrinally sensitive prose -> `religious-content-translation`

Optional companions:

- source-target fidelity review -> `translation-review`
- a separate cleanup pass for wording that remains generic, stiff, or machine-like -> `anti-slop-writing`

Do not use `anti-slop-writing` as a substitute for translation. Do not use `translation-review` without both source and translated text.

## 2. Same-language writing or rewriting

If the user wants substantive same-language writing or rewriting of an article, essay, explainer, technical-popular piece, opinion piece, or experience-based long-form prose:

-> `editorial-writing`

Use this when structure, headings, information order, voice, explanation level, or reader progression are part of the problem.

Optional companion:

- final cleanup for generic or AI-sounding wording -> `anti-slop-writing`

Do not route a substantive article rewrite directly to `anti-slop-writing` when the article itself still needs editorial work.

## 3. Cleanup or humanization

If the text is already structurally sound and the request is specifically to make it less generic, stiff, translated, over-polished, or AI-sounding:

-> `anti-slop-writing`

Examples:

- `make this paragraph sound less AI`
- `humanize this draft without changing the meaning`
- `this translation is accurate but still sounds stiff`

This is a cleanup pass, not a general-purpose article editor.

## 4. Translation review

If both source and translation exist and the user wants fidelity, tone, terminology, naturalness, or structural QA:

-> `translation-review`

When domain-specific or structural constraints matter, compose the review with the relevant translation skill's safeguards.

Examples:

- translated README -> `translation-review` + structural safeguards from `technical-docs-translation`
- translated locale file -> `translation-review` + token safeguards from `locale-translation`
- translated religious prose -> `translation-review` + terminology/tone constraints from `religious-content-translation`

## 5. Format is a constraint, not a task

Do not route merely because a file ends in `.md`, `.mdx`, `.json`, or `.yaml`.

Examples:

- blog article stored in Markdown, same-language rewrite -> `editorial-writing`
- blog article stored in Markdown, translation -> `general-translation`
- README with code fences, translation -> `technical-docs-translation`
- JSON locale dictionary -> `locale-translation`

Apply narrow structural safeguards as companions when an otherwise editorial file contains fragile frontmatter, code, links, footnotes, or other structure that must remain intact.

## 6. Prefer the smallest useful composition

Do not create a multi-pass workflow when one skill is enough.

Examples:

```text
"Translate this sentence."
-> general-translation
```

```text
"Rewrite this technical blog post so it reads naturally and the headings are less stiff."
-> editorial-writing
-> anti-slop-writing if a final cleanup is still needed
```

```text
"Review this Indonesian translation against the English source."
-> translation-review
```

```text
"Translate this README and preserve code and Markdown."
-> technical-docs-translation
```

The goal of routing is not to maximize the number of skills used. It is to select the narrowest combination that fully covers the user's actual task.

---
name: technical-docs-translation
description: Use this to translate developer-facing technical documentation such as README files, API guides, tutorials, and Markdown or MDX with code-sensitive structure. Preserves code, commands, identifiers, and document structure while keeping prose natural. Do not use it for ordinary editorial articles merely because they are stored in Markdown.
---

# Technical Docs Translation

Translate developer documentation without breaking code, structure, or terminology.

## Scope Boundary

- Use this for developer-facing docs where code samples, commands, identifiers,
  framework terms, or Markdown/MDX structure need special protection.
- Treat Markdown and MDX as formats, not automatic triggers. For essays,
  reporting, and editorial articles without developer-documentation
  constraints, use `general-translation`.
- For editorial Markdown with fragile frontmatter, links, footnotes, or embedded
  code, keep `general-translation` as the prose skill and apply only this
  skill's structural safeguards as a companion.
- For app locale files or UI dictionaries, use `locale-translation`.
- To evaluate an existing source-and-translation pair, compose this skill's
  structural rules with `translation-review`.

## Use Cases

- README
- code-sensitive Markdown
- developer-facing MDX
- framework docs
- API guides
- tutorials
- developer references

## Core Rules

- Translate prose, not executable code.
- Preserve code fences, inline code, commands, paths, imports, exports, URLs, placeholders, JSX/component names, and frontmatter keys.
- Translate frontmatter values only when they are human-facing text.
- Keep common developer terms in the source language when translating them would slow comprehension.
- Keep technical terminology consistent within the file.
- Avoid stacking too many English words into one untranslated phrase when the surrounding prose can be localized more naturally.
- If project-visible labels such as admonition tags or heading conventions are ambiguous, follow the file's existing convention instead of localizing inconsistently.
- For Indonesian developer-facing prose, prefer the term used by the technical
  community over a dictionary-like Indonesian equivalent when the English term
  is clearer or more idiomatic.

## Typical Inputs

- source language
- target language
- format such as `markdown` or `mdx`
- domain such as framework docs or API docs

## Failure Modes To Prevent

- broken Markdown or MDX
- translated code identifiers
- literal phrasing around technical concepts
- inconsistent terminology
- mixed-language prose that sounds imported rather than written naturally

## Wording Guidance

- Keep developer terms in English when needed, but localize the surrounding phrase naturally.
- Do not preserve an English phrase mechanically just because one term inside it should remain English.
- Avoid literal carryover such as `membuat scaffold` when a more natural phrase is available.
- Reduce mixed-language phrase stacking when a short Indonesian frame keeps the developer meaning just as clear.
- When a conceptual phrase sounds literal after translation, rewrite the surrounding sentence so it matches how developers actually describe the idea in the target language.
- When several English technical terms appear in one paragraph, add natural
  Indonesian framing so the prose does not become English nouns with Indonesian
  verbs attached.
- Distinguish product/concept terms from UI component terms. Use `chatbot` for a
  conversational AI system or product experience; reserve `chatbox` for the
  visible chat input/container in an interface.

Prefer:

- `editor teks dengan dukungan sintaks Markdown`
- `setup wizard di command line`
- `menyiapkan struktur awal proyek`
- `wizard setup berbasis command line`
- `struktur data yang konsisten`
- `neural network` when the article targets developers or AI practitioners
- `Di recommendation system, ...` instead of starting every sentence with a
  bare English technical noun
- `era AI modern terasa dimulai dari chatbot`

Over:

- `Text Editor dengan dukungan sintaks Markdown`
- `command line setup wizard`
- `membuat scaffold proyek`
- `bentuk yang konsisten`
- `jaringan saraf` when it sounds like a dictionary choice for the audience
- stacked phrasing such as `Recommendation system memilih... Machine translation
  mengubah... Voice assistant menerima...`
- `era AI modern terasa dimulai dari chatbox` when the meaning is the product or
  interaction pattern, not the UI box

## Final Check

- Is the structure intact?
- Is the prose natural for developers in the target language?
- Were code-sensitive regions preserved exactly?
- Are English technical terms used intentionally rather than piled together
  awkwardly in prose?

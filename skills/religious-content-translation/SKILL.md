---
name: religious-content-translation
description: Use this for translating religious content where tone, reverence, terminology, and doctrinal sensitivity matter. Best for educational, devotional, editorial, and explanatory religious prose rather than generic UI strings. For source-target quality review, compose this skill with translation-review rather than treating it as a separate review skill.
---

# Religious Content Translation

Translate religious content with accuracy, clarity, and tone sensitivity.

## Scope Boundary

- Use this when the requested operation is translation and the content is devotional, educational, editorial, or explanatory religious prose where reverence and doctrinal sensitivity matter.
- For source-target quality review, use `translation-review` and apply this skill's terminology and tone constraints as needed.
- For generic UI strings or locale dictionaries, use `locale-translation`.
- For ordinary prose with no religious sensitivity, use `general-translation`.

## Use Cases

- educational religious prose
- devotional writing
- editorial religious content
- explanatory notes
- long-form faith-related text

## Core Rules

- Preserve theological meaning and tone carefully.
- Use terminology consistently within the tradition and project context.
- Avoid casual reframing when the source is reverent or formal.
- Do not inject interpretation beyond what the source supports.
- Preserve names, citations, and canonical references accurately.
- If a literal phrasing sounds imported or spiritually flat, prefer more natural reverent target-language wording without adding doctrinal content.

## Inputs To Infer

- source language
- target language
- tradition/context
- audience
- tone

## Failure Modes To Prevent

- doctrinal drift
- flattened reverent tone
- inconsistent religious terms
- overconfident paraphrase
- literal contemplative phrasing that sounds translated rather than spiritually natural
- treating domain-sensitive translation guidance as a substitute for source-target review

## Wording Guidance

- Prefer reverent target-language phrasing that sounds native to religious or reflective prose.
- Keep devotional calm and humility, but avoid inflated wording that obscures meaning.
- When rendering contemplative concepts, choose natural spiritual language over mechanically literal phrasing.

Prefer:

- `refleksi adalah cara ...`
- `apa yang digerakkan ayat dalam hati`
- `lafaznya meresap`
- `tradisi keilmuan Islam` or another project-appropriate scholarly term

Over:

- `refleksi adalah sebuah cara ...`
- `apa yang dibangkitkan oleh sebuah ayat di dalam hati`
- `membiarkan kata-kata itu menetap`
- `keilmuan tradisi`

## Final Check

- Is the meaning faithful?
- Is the tone appropriate for the source?
- Are key terms and references consistent?
- If this is a review task, was `translation-review` used for the actual source-target comparison?

---
name: editorial-writing
description: Use this for same-language substantive writing or rewriting of articles, essays, explainers, technical-popular prose, opinion pieces, and experience-based long-form writing. Improves structure, headings, flow, voice, specificity, and reader progression without changing supported facts or inventing claims. For translation, use the relevant translation skill. For a narrower cleanup pass focused on generic or AI-sounding wording, use anti-slop-writing after the editorial pass when needed.
---

# Editorial Writing

Improve a piece as an article, not merely as a collection of sentences.

## Scope Boundary

- Use this for same-language writing or substantive rewriting of articles, essays, explainers, technical-popular writing, opinion pieces, and experience-based long-form prose.
- Use it when the problem includes structure, headings, information order, voice, pacing, explanation level, or reader progression.
- Do not use this as a translation skill. If the task changes languages, choose the relevant translation skill first.
- Do not use this for README files, API references, or developer documentation merely because they are technical; those tasks need documentation-specific behavior.
- Do not use this for typo-only proofreading or a narrow request to make wording less stiff. Use `anti-slop-writing` when the structure and editorial framing are already sound and the remaining problem is generic or machine-like prose.
- Preserve evidence boundaries, uncertainty, terminology, and deliberate repetition when they carry meaning.

## Use Cases

- blog articles
- essays
- explainers
- technical-popular articles
- opinion or editorial prose
- experience-based long-form writing
- substantive same-language rewrites
- restructuring headings and sections

## Core Rules

- Preserve facts, claims, uncertainty, and source-supported meaning.
- Improve the article's structure before polishing individual sentences when structure is the real problem.
- Prefer concrete observations, actions, artifacts, and consequences over abstract editorial language.
- Keep the writer's point of view when it adds useful context. Do not replace firsthand judgment with generic best-practice prose.
- Match the audience's actual knowledge level. Do not overexplain obvious points merely to make the article feel complete.
- Vary section shape when the material calls for it. Do not force every section into the same setup -> explanation -> list -> takeaway pattern.
- Let headings name the real question, problem, event, or tension. Do not turn every heading into a command, lesson, or polished contrast slogan.
- Keep technical terms that are natural for the audience, but do not hide simple ideas behind professional jargon.
- Remove sentences that only announce structure, summarize what was just said, or manufacture a takeaway without adding information.

## Editorial Failure Modes

### Documentation voice

Do not turn an article into a manual, policy document, incident report, or training material unless that is the intended form.

Watch for phrasing such as:

- `Untuk menentukan ...`
- `Yang perlu dihindari adalah ...`
- `Pendekatan yang dapat digunakan ...`
- `Langkah berikut dapat dilakukan ...`

These forms are not always wrong, but repeated use can erase the writer's voice and make editorial prose sound procedural.

### Professionalization bias

Do not assume that more formal, abstract, or polished wording is more human.

Avoid replacing concrete practitioner language with abstractions such as:

- `respons insiden tetap proporsional`
- `cakupan pemeriksaan`
- `indikator tingkat host`
- `pendekatan berlapis`

when the same point can be stated through the actual decision, evidence, or action.

### Training-slide headings

Avoid making most headings sound like lessons or presentation slides:

- `Bedakan X dengan Y`
- `Mulai dari X, bukan Y`
- `Pahami X sebelum Y`
- `Nyatakan apa yang terbukti`

Use these forms only when they genuinely fit the piece. Prefer headings that sound native to the article's subject and voice.

### Over-symmetrical prose

Be cautious with repeated rhetorical constructions such as:

- `X bukan Y, tetapi Z`
- `X adalah A, bukan B`
- `bukan hanya X, tetapi juga Y`

They can be useful, but repeated symmetry makes prose feel generated and over-edited.

### Manufactured takeaways

Cut short conclusion-like lines that merely restate the paragraph or try to sound memorable without adding texture or information.

### Template-shaped sections

Do not make every section follow the same rhythm. A section may be a short explanation, a table, a narrative sequence, a list, a technical example, or a direct conclusion. Let the material decide.

## Technical-Popular Writing

For technical articles aimed at practitioners or general technical readers:

- keep the technical distinction accurate without sounding like a security or engineering handbook;
- explain uncertainty in plain language rather than converting it into formal report terminology;
- use first-person experience when it clarifies why a decision was made;
- distinguish what was observed, what was inferred, and what remains unknown;
- prefer the term used naturally by the intended technical community over dictionary-like localization;
- do not expand one technical caveat into several paragraphs unless the reader actually needs that detail.

## Editing Workflow

1. Identify the article's actual point and intended reader.
2. Check whether the order of sections helps that reader follow the argument or experience.
3. Fix headings and section boundaries before line-editing if they are part of the problem.
4. Replace abstract editorial scaffolding with concrete observations where possible.
5. Tighten repetition and over-explanation.
6. Preserve useful irregularity in rhythm and section shape.
7. If the article is structurally sound but still feels generic or machine-written, run `anti-slop-writing` as a separate cleanup pass.

## Final Check

- Does this still sound like the same writer rather than a generic professional editor?
- Do the headings belong to this article, or could they appear in any training deck?
- Is technical uncertainty expressed accurately without unnecessary jargon?
- Did the rewrite improve the reader's path through the article, not just sentence polish?
- Are any sections suspiciously identical in rhythm or structure?
- Did any new claim, certainty, or interpretation appear that the original did not support?

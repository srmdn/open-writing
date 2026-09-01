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
- Keep the writer's point of view when it adds useful firsthand context or explains a real decision. Do not add first-person phrasing merely to make informational prose sound more human.
- Match the audience's actual knowledge level. Do not overexplain obvious points merely to make the article feel complete.
- Vary section shape when the material calls for it. Do not force every section into the same setup -> explanation -> list -> takeaway pattern.
- Let headings name the real question, problem, event, or tension. Do not turn every heading into a command, lesson, polished contrast slogan, or conversational hook.
- Keep technical terms that are natural for the audience, but do not hide simple ideas behind professional jargon.
- Remove sentences that only announce structure, summarize what was just said, or manufacture a takeaway without adding information.
- Prefer wording that names what is actually happening. A technically valid term is not automatically the most natural phrase for the sentence.

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

Also watch for technically valid but unnatural lexical choices that read like direct translations of professional English. Prefer the phrase a native writer would use in context. For example, `plugin yang sebenarnya sah` may be formally understandable, but `plugin yang sebenarnya tidak bermasalah` can be more natural when the intended contrast is harmful vs unaffected behavior rather than legitimate vs illegitimate identity.

### Over-personalization

First person is useful when the writer is describing something they observed, did, decided, or learned firsthand. It becomes a failure mode when the rewrite adds `saya`, `menurut saya`, `buat saya`, or similar framing to generic informational claims only to make the prose feel less formal.

Do not turn neutral technical statements into personal preferences when the point is not actually subjective.

Question repeated forms such as:

- `saya biasanya ...`
- `saya lebih memilih ...`
- `saya ingin tahu ...`
- `menurut saya ...`
- `buat saya ...`

Keep them when they carry real authorial evidence or decision context. Remove or neutralize them when the sentence would mean the same thing without the personal wrapper.

### Training-slide headings

Avoid making most headings sound like lessons or presentation slides:

- `Bedakan X dengan Y`
- `Mulai dari X, bukan Y`
- `Pahami X sebelum Y`
- `Nyatakan apa yang terbukti`

Use these forms only when they genuinely fit the piece. Prefer headings that sound native to the article's subject and voice.

### Over-conversational headings

Avoid overcorrecting formal headings into copywriting-like questions or casual hooks merely to sound human.

Question headings such as:

- `Update selesai, tapi apa yang ditinggalkan penyerang?`
- `Ada hal yang saya tahu, ada juga yang tidak`

when a shorter concrete heading would fit the article better. A natural heading does not need to sound like spoken dialogue.

### Over-symmetrical prose

Be cautious with repeated rhetorical constructions such as:

- `X bukan Y, tetapi Z`
- `X adalah A, bukan B`
- `bukan hanya X, tetapi juga Y`

They can be useful, but repeated symmetry makes prose feel generated and over-edited.

### Vague conversational wording

Making prose less formal does not justify replacing precise wording with vague conversational placeholders.

Watch for phrases such as:

- `bagian yang bermasalah`
- `sesuatu yang perlu diuji`
- `ada yang salah`
- `bagian mana yang terkena`

when the sentence can name the actual endpoint, file, account, rule, evidence, or affected layer.

### Manufactured takeaways

Cut short conclusion-like lines that merely restate the paragraph or try to sound memorable without adding texture or information.

### Template-shaped sections

Do not make every section follow the same rhythm. A section may be a short explanation, a table, a narrative sequence, a list, a technical example, or a direct conclusion. Let the material decide.

## Technical-Popular Writing

For technical articles aimed at practitioners or general technical readers:

- keep the technical distinction accurate without sounding like a security or engineering handbook;
- explain uncertainty in plain language rather than converting it into formal report terminology;
- use first-person experience only where it clarifies an observed fact or a decision actually made by the writer;
- distinguish what was observed, what was inferred, and what remains unknown;
- prefer the term used naturally by the intended technical community over dictionary-like localization;
- when an English technical concept has several possible Indonesian renderings, choose the one that best matches the concrete meaning in that sentence rather than preserving the source-language category mechanically;
- do not expand one technical caveat into several paragraphs unless the reader actually needs that detail.

## Editing Workflow

1. Identify the article's actual point and intended reader.
2. Check whether the order of sections helps that reader follow the argument or experience.
3. Fix headings and section boundaries before line-editing if they are part of the problem.
4. Replace abstract editorial scaffolding with concrete observations where possible.
5. Check whether first-person voice is carrying real experience or merely decorating informational prose.
6. Check technically correct terms for contextual naturalness, not only dictionary correctness.
7. Tighten repetition and over-explanation.
8. Preserve useful irregularity in rhythm and section shape.
9. If the article is structurally sound but still feels generic or machine-written, run `anti-slop-writing` as a separate cleanup pass.

## Final Check

- Does this still sound like the same writer rather than a generic professional editor?
- Is first-person voice used because the writer actually observed or decided something, or merely to manufacture personality?
- Do the headings belong to this article, or do they sound like a training deck or a copywriting hook?
- Is technical uncertainty expressed accurately without unnecessary jargon?
- Are technically valid terms also natural in the sentence and context?
- Did the rewrite improve the reader's path through the article, not just sentence polish?
- Are any sections suspiciously identical in rhythm or structure?
- Did conversational cleanup make any wording vague or less precise?
- Did any new claim, certainty, or interpretation appear that the original did not support?

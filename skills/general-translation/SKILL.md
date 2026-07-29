---
name: general-translation
description: Use this for general translation between languages when the goal is natural, human-sounding output rather than domain-specific formatting rules. Best for prose, chat, essays, articles, and everyday text. Supports source and target language as runtime parameters.
---

# General Translation

Translate for meaning, tone, and readability.

## Scope Boundary

- Use this for prose and everyday text that does not have strict runtime or format constraints.
- For locale files and UI dictionaries, use `locale-translation`.
- For Markdown, MDX, README, and developer docs, use `technical-docs-translation`.
- For persuasion-heavy product or campaign copy, use `marketing-translation`.

## Use Cases

- prose
- chat
- articles
- notes
- essays
- general rewriting across languages

## Core Rules

- Prioritize meaning over literal wording.
- Preserve tone, emphasis, and intent.
- Keep names, brands, URLs, code identifiers, and placeholders unchanged unless the user asks otherwise.
- Do not add claims, examples, or opinions.
- Make the output sound like native writing in the target language.
- Prefer natural target-language flow over grammatically faithful but flat sentence structure.

## Inputs To Infer

- source language
- target language
- tone
- audience

## Output Standard

- natural, not word-for-word
- faithful, not embellished
- readable, not stiff

## Wording Guidance

- Replace stiff procedural openers with more natural sentence flow when meaning stays intact.
- Avoid generic product nouns if the target language has a simpler, more human phrasing.
- Rewrite abstract explanatory prose so it reads like something a person would naturally say or write.
- When two phrasings are equally faithful, choose the one that sounds like original writing in the target language, not translated copy.
- In product-help or interface-adjacent prose, avoid formal nouns and repeated verb structure if a shorter native phrasing says the same thing.
- Translate process-oriented outcome clauses as direct user outcomes when the literal process framing sounds unnatural. For example, render `agar proses ... berjalan lancar` as `so you can ... without any issues`, not `so you can ... smoothly`.
- For Indonesian articles or essays, check the local sentence rhythm. Prefer
  phrasing that sounds originally written in Indonesian, not just correct
  Indonesian.
- In Indonesian technical-popular prose, keep the tone mature and readable.
  Avoid over-formal abstract transitions when a natural editorial phrase says
  the same thing.
- Avoid importing English-thesis phrasing too literally into Indonesian. If a
  phrase like `completing intentions` becomes `menyelesaikan niat`, rewrite the
  idea more concretely, such as `mengerjakan tugas` or `menjalankan instruksi`.
- Watch for dramatic but generic one-line paragraphs. Keep them only when they
  add voice, not when they merely imitate essay rhythm.
- Avoid transition scaffolding that sounds like an outline marker. Replace
  generic pivots such as `Di sinilah...`, `Itulah sebabnya...`, or `Tetapi pola
  besarnya...` with a concrete observation when the sentence does not add new
  meaning.
- For product or cultural concepts, choose the term that names the real object,
  not the literal UI part. Example: use `chatbot` for conversational AI products
  such as ChatGPT; use `chatbox` only when specifically referring to the input
  box or chat UI element.

Prefer:

- `Saat Anda mengeklik ...`
- `tempat untuk berbagi ...`
- `refleksi berisi wawasan ...`
- `Tap "Continue" to return to your last lesson.`
- `so you can sign back in without any issues`
- direct, flowing sentence structure
- `bahkan sampai sekarang`
- `jalannya tidak pernah mulus`
- `dipakai sehari-hari`
- `chatbot` when the topic is the conversational AI experience
- `mengerjakan tugas`

Over:

- `Mengeklik ... akan ...`
- `platform untuk ...` when it adds no value
- `enter the learning room to continue the last lesson`
- `so you can sign back in smoothly`
- accurate but flat sentence structure
- `bahkan sekarang` when `bahkan sampai sekarang` sounds more natural
- `perjalanannya tidak lurus`
- `digunakan dalam kehidupan sehari-hari`
- `chatbox` when the intended meaning is the chatbot product or experience
- `menyelesaikan niat`

## Final Check

- Does it sound written by a native speaker?
- Was any meaning lost or exaggerated?
- Are fixed tokens preserved?
- Is the sentence flow natural, not just correct?

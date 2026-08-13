---
name: anti-slop-writing
description: Use this as a second-pass writing skill when no source-text comparison is needed. Removes AI-sounding prose, translation stiffness, generic rhythm, filler, and predictable wording without changing the underlying meaning. Best for humanizing drafts, same-language cleanup, or cleaning a translation after the translation pass. For source-to-translation fidelity review, use translation-review instead.
---

# Anti-Slop Writing

Improve text that sounds machine-made or generically AI-written.

## Scope Boundary

- Use this to improve the supplied draft itself, whether it was written in the
  target language or produced by an earlier translation pass.
- Do not infer missing source meaning or treat stylistic preference as factual
  correction.
- When both source and translation are available and fidelity must be checked,
  use `translation-review` first.
- Preserve established project terminology, register, evidence boundaries, and
  deliberate repetition.

## Use Cases

- second-pass cleanup after translation
- humanizing drafts
- reducing stiffness
- removing generic AI tone
- tightening repetitive phrasing
- separate cleanup pass after `general-translation` when a clean
  translation-only baseline still feels stiff, generic, or too machine-written

## Core Rules

- Preserve meaning while improving the writing.
- Remove filler, throat-clearing, empty emphasis, and generic transitions.
- Break repetitive rhythm and predictable sentence patterns.
- Prefer direct phrasing over inflated phrasing.
- Do not rewrite so aggressively that tone or facts drift.
- Improve text that is technically correct but still sounds generically translated.

## Common Problems

- literal translation feel
- overexplaining
- vague high-level claims
- repetitive sentence cadence
- polished but impersonal wording
- stiff procedural phrasing
- generic product nouns that flatten the sentence
- correct but dictionary-like Indonesian
- technical terms translated even though the English term is more natural for
  the intended audience
- mixed English-Indonesian phrasing that feels pasted together
- calques that remain stiff after synonym swapping and need the clause or
  sentence to be restructured
- noun stacks or adjective-modifier chains that mirror English structure
- internal workflow labels carried into reader-facing prose
- em dashes (`—`) used as a generic connector where the target language would
  naturally use a colon, comma, parentheses, a period, or a restructured
  sentence
- staccato manifesto rhythm: short declarative lines that sound profound but do
  not add texture (`Itu sudah besar.`, `Tiga kata itu penting.`)
- repetitive capability ladders (`Ia bisa... Ia bisa... Ia bisa...`) when a
  compressed sentence or grouped list would sound more human
- pseudo-deep abstraction carried over from another language when a concrete
  phrase is clearer
- cute metaphors that flatten technical meaning unless the surrounding prose
  earns them
- generic transition scaffolding (`Di sinilah...`, `Itulah sebabnya...`,
  `Tetapi pola besarnya...`) when the sentence merely announces structure
  instead of adding a concrete observation
- ungrounded abstraction: polished concepts repeated without concrete actions,
  artifacts, decisions, or consequences

## Useful Rewrite Patterns

- `Mengeklik ... akan ...` -> `Saat Anda mengeklik ...` or a more direct action phrase
- `platform untuk ...` -> `tempat untuk ...` when the sentence becomes more human and no product nuance is lost
- abstract explanatory prose -> tighter and more concrete target-language phrasing
- `Kalimat itu masih terasa berani bahkan sekarang.` ->
  `Kalimat itu masih terasa berani bahkan sampai sekarang.`
- `Perjalanannya tidak lurus.` -> `Jalannya tidak pernah mulus.`
- `Sistem memeriksa input. Sistem menyimpan hasil. Sistem mengirim notifikasi.`
  -> `Sistem memeriksa input, menyimpan hasil, dan mengirim notifikasi.`
- `Itu sudah besar.` -> expand only if it carries a real observation, or cut it
  when it only adds dramatic pause
- `Di sinilah konsep ini menjadi penting.` -> replace the transition with the
  concrete observation that makes the concept important
- `pengalaman belajar atlas` -> `belajar dari atlas` when the noun stack mirrors
  English rather than natural Indonesian
- `pertanyaan yang terarah` -> restructure around the action or outcome, such as
  `mulai dari satu pertanyaan yang bisa dijawab`, when adjective swapping still
  sounds translated
- `Audit sumber proyek` -> `Pemeriksaan sumber` when internal workflow wording
  leaks into public prose and the narrower label preserves the meaning

## Punctuation

In Indonesian copy, avoid the em dash (`—`) as a default connector. Match the
replacement to the clause's function:

- colon (`:`) for an explanation, apposition, or example that follows;
- comma (`,`) or parentheses for a short aside;
- a period (`.`) and a new sentence for a strong break;
- semicolon (`;`) only between two independent clauses, not as a general
  substitute for a dash.

Examples:

- `definisi kerja proyek — definisi yang bisa berubah` ->
  `definisi kerja proyek: definisi yang bisa berubah`
- `dua versi — yang lama dan yang baru` ->
  `dua versi, yang lama dan yang baru`
- `Dia setuju — tapi dengan syarat.` -> `Dia setuju, tapi dengan syarat.`

## Final Check

- Does it still mean the same thing?
- Does it sound more human, specific, and direct?
- Is any line still obviously AI-sounding?
- Is the prose merely polished, or does it actually feel less translated?
- Would this sound like it was written directly for the intended audience and
  project rather than cleaned up from a generic template?

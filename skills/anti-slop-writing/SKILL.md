---
name: anti-slop-writing
description: Use this as a second-pass writing skill when no source-text comparison is needed. Removes AI-sounding prose, translation stiffness, generic rhythm, filler, predictable wording, and over-professionalized phrasing without changing the underlying meaning. Best for humanizing drafts, same-language cleanup, or cleaning a translation after the primary pass. For substantive article restructuring use editorial-writing first. For source-to-translation fidelity review, use translation-review instead.
---

# Anti-Slop Writing

Improve text that sounds machine-made or generically AI-written without turning cleanup into a broad rewrite.

## Scope Boundary

- Use this to improve the supplied draft itself, whether it was written in the target language or produced by an earlier translation or writing pass.
- Treat this as a cleanup or humanization pass, not the default primary skill for substantive article editing.
- If an article needs changes to structure, headings, information order, reader progression, or editorial framing, use `editorial-writing` first.
- Do not infer missing source meaning or treat stylistic preference as factual correction.
- When both source and translation are available and fidelity must be checked, use `translation-review` first.
- Preserve established project terminology, register, evidence boundaries, uncertainty, and deliberate repetition.

## Use Cases

- second-pass cleanup after translation
- second-pass cleanup after editorial rewriting
- humanizing drafts that are already structurally sound
- reducing stiffness
- removing generic AI tone
- tightening repetitive phrasing
- cleaning accurate translations that still sound machine-written

## Core Rules

- Preserve meaning while improving the writing.
- Remove filler, throat-clearing, empty emphasis, and generic transitions.
- Break repetitive rhythm and predictable sentence patterns.
- Prefer direct phrasing over inflated phrasing.
- Do not rewrite so aggressively that tone, facts, uncertainty, or evidence boundaries drift.
- Do not assume that making prose more formal, abstract, symmetrical, or polished makes it more human.
- Preserve useful irregularity when it sounds natural for the writer and audience.

## Common Problems

- literal translation feel
- overexplaining
- vague high-level claims
- repetitive sentence cadence
- polished but impersonal wording
- stiff procedural phrasing
- documentation or handbook voice leaking into editorial prose
- abstract professional jargon replacing concrete actions or observations
- training-slide headings that make every section sound like a lesson
- repeated contrast formulas such as `X bukan Y, tetapi Z`
- manufactured takeaway lines that restate the paragraph without adding information
- repeated section shapes such as setup -> explanation -> list -> takeaway
- generic product nouns that flatten the sentence
- correct but dictionary-like Indonesian
- technical terms translated even though the English term is more natural for the intended audience
- mixed English-Indonesian phrasing that feels pasted together
- calques that remain stiff after synonym swapping and need the clause or sentence to be restructured
- noun stacks or adjective-modifier chains that mirror English structure
- internal workflow labels carried into reader-facing prose
- em dashes (`—`) used as a generic connector where the target language would naturally use a colon, comma, parentheses, a period, or a restructured sentence
- staccato manifesto rhythm: short declarative lines that sound profound but do not add texture (`Itu sudah besar.`, `Tiga kata itu penting.`)
- repetitive capability ladders (`Ia bisa... Ia bisa... Ia bisa...`) when a compressed sentence or grouped list would sound more human
- pseudo-deep abstraction carried over from another language when a concrete phrase is clearer
- cute metaphors that flatten technical meaning unless the surrounding prose earns them
- generic transition scaffolding (`Di sinilah...`, `Itulah sebabnya...`, `Tetapi pola besarnya...`) when the sentence merely announces structure instead of adding a concrete observation
- ungrounded abstraction: polished concepts repeated without concrete actions, artifacts, decisions, or consequences

## Professionalization Bias

A common failure mode is turning an already understandable draft into prose that sounds more like documentation, consulting language, a policy memo, or a training deck.

Watch for changes that:

- replace a concrete action with an abstract category;
- replace a practitioner's judgment with generic best-practice language;
- make every sentence grammatically balanced and rhetorically symmetrical;
- add formal transitions only to make paragraph structure more visible;
- make headings sound like instructions or lessons even when the article is experiential or editorial;
- add short conclusion lines merely because they sound quotable.

Examples of suspicious phrasing in Indonesian include:

- `Untuk menentukan ...`
- `Yang perlu dihindari adalah ...`
- `Pendekatan berlapis dapat mencakup ...`
- `Pemisahan ini penting supaya ... tetap proporsional.`
- `Salah satu pelajaran paling penting ...`
- `Prinsip yang sama berlaku ...`

These phrases are not banned. Rewrite or cut them when they merely make the prose sound professionally packaged rather than more precise.

## Heading Check

Do not turn most headings into training-slide commands or polished contrast slogans.

Patterns to question when repeated:

- `Bedakan X dengan Y`
- `Mulai dari X, bukan Y`
- `Pahami X sebelum Y`
- `Nyatakan apa yang terbukti`
- `Bangun kembali dari ...`

Prefer headings that belong specifically to the article's subject, question, event, or tension. Keep an imperative or contrast heading when it genuinely sounds natural for that piece.

## Useful Rewrite Patterns

- `Mengeklik ... akan ...` -> `Saat Anda mengeklik ...` or a more direct action phrase
- `platform untuk ...` -> `tempat untuk ...` when the sentence becomes more human and no product nuance is lost
- abstract explanatory prose -> tighter and more concrete target-language phrasing
- professional abstraction -> name the actual action, evidence, decision, or consequence
- `Kalimat itu masih terasa berani bahkan sekarang.` -> `Kalimat itu masih terasa berani bahkan sampai sekarang.`
- `Perjalanannya tidak lurus.` -> `Jalannya tidak pernah mulus.`
- `Sistem memeriksa input. Sistem menyimpan hasil. Sistem mengirim notifikasi.` -> `Sistem memeriksa input, menyimpan hasil, dan mengirim notifikasi.`
- `Itu sudah besar.` -> expand only if it carries a real observation, or cut it when it only adds dramatic pause
- `Di sinilah konsep ini menjadi penting.` -> replace the transition with the concrete observation that makes the concept important
- `pengalaman belajar atlas` -> `belajar dari atlas` when the noun stack mirrors English rather than natural Indonesian
- `pertanyaan yang terarah` -> restructure around the action or outcome, such as `mulai dari satu pertanyaan yang bisa dijawab`, when adjective swapping still sounds translated
- `Audit sumber proyek` -> `Pemeriksaan sumber` when internal workflow wording leaks into public prose and the narrower label preserves the meaning

## Punctuation

In Indonesian copy, avoid the em dash (`—`) as a default connector. Match the replacement to the clause's function:

- colon (`:`) for an explanation, apposition, or example that follows;
- comma (`,`) or parentheses for a short aside;
- a period (`.`) and a new sentence for a strong break;
- semicolon (`;`) only between two independent clauses, not as a general substitute for a dash.

Examples:

- `definisi kerja proyek — definisi yang bisa berubah` -> `definisi kerja proyek: definisi yang bisa berubah`
- `dua versi — yang lama dan yang baru` -> `dua versi, yang lama dan yang baru`
- `Dia setuju — tapi dengan syarat.` -> `Dia setuju, tapi dengan syarat.`

## Final Check

- Does it still mean the same thing?
- Does it sound more human, specific, and direct?
- Is any line still obviously AI-sounding?
- Did cleanup accidentally turn the draft into documentation, a training deck, or generic professional prose?
- Are abstract nouns hiding a simpler concrete statement?
- Are sentence and section rhythms suspiciously uniform?
- Is the prose merely polished, or does it actually feel more naturally written?
- Would this sound like it was written directly for the intended audience and project rather than cleaned up from a generic template?

---
name: marketing-translation
description: Use this for translating persuasive marketing copy such as landing pages, product copy, CTAs, email copy, announcements, and campaigns. Optimizes for persuasive, human-sounding target-language copy without drifting from the source message. For same-language marketing rewriting, use a dedicated writing skill when one exists rather than treating this translation skill as a general copy editor.
---

# Marketing Translation

Translate marketing copy for impact, not just correctness.

## Scope Boundary

- Use this when the requested operation is translation and the source is meant to persuade, attract, announce, or convert.
- Do not use this as a general same-language marketing rewrite skill.
- For ordinary prose without persuasion goals, use `general-translation`.
- For UI strings and locale dictionaries, use `locale-translation`.
- If a translated result is accurate but still sounds generic or stiff, use `anti-slop-writing` as a separate cleanup pass when needed.

## Use Cases

- landing pages
- product copy
- CTAs
- email campaigns
- announcements
- ad-style copy

## Core Rules

- Preserve the promise and meaning of the source.
- Rewrite within the translation pass for natural persuasion in the target language; do not expand this into unrelated same-language copy editing.
- Prefer concise and concrete copy over generic hype.
- Keep brand names, product names, and fixed claims unchanged.
- Avoid robotic polish and safe-sounding filler.
- If a literal translation sounds acceptable but weak, prefer sharper target-language sales rhythm as long as the promise does not drift.

## Inputs To Infer

- source language
- target language
- audience
- tone
- campaign context

## Failure Modes To Prevent

- literal but weak copy
- overhyped copy not supported by the source
- generic AI marketing tone
- flat CTAs
- imported product metaphors or verbs that sound translated in the target language
- drifting from translation into unsupported copywriting or new claims

## Wording Guidance

- Prefer direct CTA phrasing over mechanically literal renderings of English calls to action.
- Replace imported product verbs with natural target-language verbs when the benefit stays the same.
- Keep contrast and momentum sharp. Marketing lines often need cleaner rhythm than general prose.

Prefer:

- `Coba lebih dulu ...`
- `akses lebih awal`
- `susun rencana belajar`
- `tanpa repot ...`

Over:

- `Jadilah yang pertama untuk mencoba ...`
- `akses awal` when it reads like direct carryover
- `bangun rencana belajar`
- literal struggle metaphors such as `bergulat dengan alat ...`

## Final Check

- Would a native speaker find this persuasive?
- Does it still match the source claim?
- Does it sound specific rather than generic?
- Did the translation pass stay within the source message instead of becoming a new marketing rewrite?

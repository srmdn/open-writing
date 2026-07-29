---
name: translation-review
description: Use this to review, critique, and improve translation outputs. Checks fidelity, tone, terminology, structural safety, and human-sounding quality across general prose, technical docs, locale files, and other translation tasks.
---

# Translation Review

Review a translation before treating it as final.

## Review Goals

- fidelity to source meaning
- target-language naturalness
- terminology consistency
- structure and token safety
- domain fit

## Review Workflow

1. Check meaning preservation.
2. Check tone and audience fit.
3. Check domain-specific terminology.
4. Check structure-sensitive tokens and formatting.
5. Check whether the text sounds human or machine-made.
6. For Indonesian technical or editorial prose, check whether the rhythm sounds
   originally written in Indonesian rather than merely cleaned up.
7. Suggest fixes only where needed.

## Review Inputs

- source text
- translated text
- source language
- target language
- task type
- format

## Failure Modes To Catch

- missing or added meaning
- awkward literal phrasing
- broken placeholders or formatting
- inconsistent terms
- AI-sounding polish or filler
- dictionary-like technical terms when the audience would expect the English
  term
- mixed English-Indonesian phrasing that preserves terms but loses natural
  sentence flow
- correct Indonesian sentences that still sound translated or over-smoothed
- near-miss technical terms that change the object being discussed, such as
  `chatbox` for a conversational AI product where `chatbot` is intended

## Output Style

- concise findings first
- examples of better phrasing when useful
- preserve what is already good
- call out terminology tradeoffs instead of forcing every English technical term
  into Indonesian

---
name: translation-review
description: Use this to compare a source text with an existing translation and review fidelity, tone, terminology, structural safety, and target-language naturalness. Best for source-target quality assurance across prose, technical docs, locale files, and other translation tasks. For humanization without a source text or for same-language cleanup, use anti-slop-writing instead.
---

# Translation Review

Review a translation before treating it as final.

## Scope Boundary

- Require both the source text and the translated text for a full review.
- Judge naturalness against the source, audience, domain, and task brief rather
  than applying a generic house style.
- For cleanup without a source text or for same-language rewriting, use
  `anti-slop-writing`.
- When code-sensitive or runtime-sensitive structure matters, compose this
  review with the relevant domain skill.

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
5. Check whether the target reads naturally without becoming looser or more
   specific than the source.
6. Separate fidelity errors from optional style preferences.
7. Suggest fixes only where needed and leave sound passages unchanged.

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
- target-language filler, abstraction, or emphasis not supported by the source
- dictionary-like technical terms when the audience would expect the English
  term
- mixed English-Indonesian phrasing that preserves terms but loses natural
  sentence flow
- correct Indonesian sentences that still sound translated or over-smoothed
- near-miss terminology that names the wrong object, action, or relationship
- natural-sounding additions that quietly introduce unsupported detail
- broad rewrites that impose reviewer taste instead of fixing a translation
  problem

## Output Style

- concise findings first
- examples of better phrasing when useful
- preserve what is already good
- call out terminology tradeoffs instead of forcing every English technical term
  into Indonesian
- label optional improvements separately from fidelity or safety problems

# Decisions

This log records choices that affect the project's public scope, skill
architecture, or quality method. Revisit a decision when its stated trigger
occurs.

## D-001: Organize translation behavior by task type

- **Status:** accepted
- **Decision:** Use task type as the main boundary for translation skills and future tools.
  Treat source and target language as runtime inputs.
- **Why:** The same translation direction needs different behavior for prose,
  technical docs, locale files, marketing, subtitles, and religious content.
- **Trade-off:** Contributors must maintain clear boundaries when a case could
  fit more than one skill.
- **Revisit when:** Repeated eval failures show that task type cannot express a
  materially different translation workflow.

## D-002: Benchmark English and Indonesian first

- **Status:** accepted
- **Decision:** Use English <-> Indonesian as the initial translation quality benchmark
  while keeping skill structure extensible to other languages.
- **Why:** A narrow benchmark enables deeper evaluation and terminology work
  without hardcoding the language pair into the architecture.
- **Trade-off:** Quality claims for other languages remain limited until they
  receive their own representative evaluation.
- **Revisit when:** The current benchmark is stable enough and another language
  has sustained user demand plus evaluation coverage.

## D-003: Keep skills focused and composable

- **Status:** accepted
- **Decision:** Give each skill one main job and compose reusable skills such as
  review or anti-slop guidance with primary writing or translation skills.
- **Why:** Focused skills are easier to trigger, evaluate, revise, and reuse
  than one large mixed-purpose instruction set.
- **Trade-off:** Some tasks require more than one skill or a deliberate choice
  between nearby scopes.
- **Revisit when:** Composition repeatedly creates conflicting instructions or
  unnecessary multi-pass work.

## D-004: Keep structural safety in domain-specific skills

- **Status:** accepted
- **Decision:** Keep locale token safety in `locale-translation` and code or
  Markdown safety in `technical-docs-translation`, not in general prose rules.
- **Why:** Runtime-sensitive formats need stricter constraints than ordinary
  translation and should be tested near the behavior they protect.
- **Trade-off:** Shared translation principles may appear in shorter forms
  across multiple skills.
- **Revisit when:** Repeated duplication justifies a separate reusable safety
  skill without weakening domain boundaries.

## D-005: Use evaluation to drive skill revisions

- **Status:** accepted
- **Decision:** Treat a skill as a behavior hypothesis. Revise it when evals
  expose a repeated weakness, then run a targeted follow-up.
- **Why:** Good-looking instructions do not prove that output is faithful,
  natural, safe, or consistent.
- **Trade-off:** Evidence-driven refinement takes longer than editing from
  intuition alone.
- **Boundary:** Public contributors may use their own representative evidence;
  access to the maintainer's private eval workspace is not required.
- **Revisit when:** Automated evaluation or a public benchmark provides a more
  reliable replacement for the current process.

## D-006: Keep private planning outside the public contract

- **Status:** accepted
- **Decision:** Use optional `.local/` files for private planning, evaluation,
  release notes, and session continuity. Keep them out of git.
- **Why:** Private experiments can evolve quickly without becoming required
  context or exposing local evaluation material.
- **Trade-off:** Public contributors cannot inspect every internal experiment
  behind a published skill revision.
- **Rule:** Public documentation must remain sufficient for contribution and
  use without `.local/`.
- **Revisit when:** A private artifact becomes stable, reusable, and necessary
  for public collaboration.

## D-007: Stabilize skills before adding product surfaces

- **Status:** accepted
- **Decision:** Build and evaluate the skill layer before implementing MCP or
  web surfaces.
- **Why:** Later interfaces should expose proven writing and translation behavior rather
  than freeze unstable behavior into APIs or user flows.
- **Trade-off:** Users rely on agent-driven skill workflows until programmable
  and human-facing interfaces exist.
- **Revisit when:** The V1 skill set has enough repeated evidence to serve as a
  stable baseline for MCP design.

## D-008: Route by task and content, not file extension

- **Status:** accepted
- **Decision:** Choose the primary translation skill from the content and task.
  Treat Markdown, MDX, JSON, and other formats as constraints, not automatic
  task types. Use `general-translation` for editorial prose stored in Markdown;
  add structural safeguards from `technical-docs-translation` when fragile
  frontmatter, links, footnotes, or embedded code require them.
- **Why:** The same format can contain an essay, developer guide, interface
  copy, or another task type. Routing from the extension alone applies the
  wrong terminology and prose behavior.
- **Trade-off:** Some editorial files need composed behavior: one skill for the
  prose task and another skill's narrow structural safeguards.
- **Revisit when:** Composition repeatedly creates conflicting instructions or
  fails to protect structure reliably.

## D-009: Expand the skill layer beyond translation

- **Status:** accepted and validated for V1
- **Decision:** Treat same-language writing and rewriting as a first-class public
  capability alongside translation. Add focused writing skills when repeated
  evaluation shows a real capability gap instead of stretching translation or
  cleanup skills beyond their intended jobs.
- **Why:** Same-language editorial rewriting requires decisions about structure,
  headings, information order, voice, and reader progression that translation
  and anti-slop cleanup do not fully cover.
- **Outcome:** Representative editorial evaluation exposed and then reduced
  professionalization bias, over-personalization, training-slide headings,
  conversational overcorrection, vague wording, and context-insensitive lexical
  choices. This is sufficient to adopt the broader `open-writing` project scope.
- **Trade-off:** Writing remains a smaller skill family than translation and
  should expand only when further evaluation shows a real capability gap.
- **Revisit when:** Writing skills remain too narrow to justify the broader project
  scope or overlap starts to outweigh the benefit of separate capabilities.

## D-010: Route by requested operation first

- **Status:** accepted
- **Decision:** Route in the order `operation -> content/domain -> constraints`.
  Determine whether the user wants translation, same-language writing/rewrite,
  review, or cleanup before choosing a content-specific skill.
- **Why:** Content type alone cannot distinguish tasks such as translating an
  article, rewriting the same article, or only removing stiff wording from it.
- **Trade-off:** Routing documentation must remain explicit enough for agents to
  distinguish nearby operations without adding a large orchestration layer.
- **Revisit when:** Operation-first routing creates repeated ambiguity or a more
  structured routing schema becomes necessary.

## D-011: Separate primary and companion skills

- **Status:** accepted
- **Decision:** Primary skills perform the user's main transformation. Companion
  skills perform narrower review or cleanup jobs and should be composed only
  when needed. Treat `anti-slop-writing` and `translation-review` as companion
  skills; do not use them as universal fallbacks when a primary skill is
  missing.
- **Why:** Using a cleanup skill as a substitute for substantive editorial work
  encourages over-polishing, scope drift, and model-default professionalization.
- **Trade-off:** Some requests require a deliberate multi-pass workflow, while
  simple requests should still use only one skill.
- **Revisit when:** Companion passes repeatedly undo good primary output or add
  unnecessary complexity.

## Initial assumptions

- Skills are the current public product surface.
- English <-> Indonesian remains the only translation benchmark with meaningful
  local evaluation coverage.
- Same-language writing evaluation now runs alongside translation evaluation.
- MCP and web interfaces remain future work.
- Public contributors do not need `.local/` files.

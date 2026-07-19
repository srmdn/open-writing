# Decisions

This log records choices that affect the project's public scope, skill
architecture, or quality method. Revisit a decision when its stated trigger
occurs.

## D-001: Organize translation behavior by task type

- **Status:** accepted
- **Decision:** Use task type as the main boundary for skills and future tools.
  Treat source and target language as runtime inputs.
- **Why:** The same translation direction needs different behavior for prose,
  technical docs, locale files, marketing, subtitles, and religious content.
- **Trade-off:** Contributors must maintain clear boundaries when a case could
  fit more than one skill.
- **Revisit when:** Repeated eval failures show that task type cannot express a
  materially different translation workflow.

## D-002: Benchmark English and Indonesian first

- **Status:** accepted
- **Decision:** Use English <-> Indonesian as the initial quality benchmark
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
  review or anti-slop guidance with domain-specific translation skills.
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
- **Why:** Good-looking instructions do not prove that translation output is
  faithful, natural, safe, or consistent.
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
- **Why:** Later interfaces should expose a proven translation model rather than
  freeze unstable behavior into APIs or user flows.
- **Trade-off:** Users rely on agent-driven skill workflows until programmable
  and human-facing interfaces exist.
- **Revisit when:** The V1 skill set has enough repeated evidence to serve as a
  stable baseline for MCP design.

## Initial assumptions

- Skills are the current public product surface.
- English <-> Indonesian is the only quality benchmark with meaningful local
  evaluation coverage.
- MCP and web interfaces remain future work.
- Public contributors do not need `.local/` files.

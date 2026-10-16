---
id: openai-math-044
record_type: family
title: Finite cut quotients and graded flat lifting
source_family: '044'
source_collection: openai/math
batch_id: B039
subject: Algebraic and complex geometry
source_paper_ids:
- P-000228
instrument_ids:
- MI-000418
- MI-000419
headline: The source claims an equivariant cohomological Hikita theorem for arbitrary quivers.
central_instrument: Level-set cuts certify finiteness of a polynomial quotient; flatness and a grading
  lift a special-fiber isomorphism.
novelty_assessment: Cut/cocircuit ideals and graded Nakayama arguments are established methods. The source
  packages them for its quiver setting; no new general algebra theorem is asserted here.
formalization_summary: No formalization scope document is listed for this family in the pinned inventory.
  No Lean build.
statement_faithfulness: Cut exponents are nonnegative. The lifting map is surjective, the target is flat
  over the parameter ring, and the kernel is graded bounded below. These are necessary inputs, not consequences
  of the special fiber alone.
dependencies: Nullstellensatz, finite-group invariants in characteristic zero, flat base change and graded
  Nakayama.
antecedents: Hausel-Sturmfels toric hyperkahler/cocircuit framework and standard flat lifting.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Finite cut quotients and graded flat lifting

## Source manuscript and claim

[The equivariant cohomological Hikita conjecture for arbitrary quivers](../papers/P-000228.md), by OpenAI, September 24, 2026.

The source claims an equivariant cohomological Hikita theorem for arbitrary quivers.

## Extracted instruments

- [MI-000418: Prove a cut-polynomial quotient is finite by selecting a nonzero level set](../instruments/MI-000418.md)
- [MI-000419: Lift a graded special-fiber isomorphism using target flatness](../instruments/MI-000419.md)

## Dependencies and antecedents

Nullstellensatz, finite-group invariants in characteristic zero, flat base change and graded Nakayama.

Hausel-Sturmfels toric hyperkahler/cocircuit framework and standard flat lifting. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the cut definitions, complete finiteness proof and complete flavor-lifting proof. The global cut recurrence and the geometric surjectivity/special-fiber inputs were not audited.

No formalization scope document is listed for this family in the pinned inventory. No Lean build.

Cut exponents are nonnegative. The lifting map is surjective, the target is flat over the parameter ring, and the kernel is graded bounded below. These are necessary inputs, not consequences of the special fiber alone.

[Batch record](../../batches/B039/README.md)

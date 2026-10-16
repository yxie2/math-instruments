---
id: openai-math-204
record_type: family
title: Filtered intersection bounds and nilpotent centralizer motion
source_family: '204'
source_collection: openai/math
batch_id: B019
subject: Algebra
source_paper_ids:
- P-000150
instrument_ids:
- MI-000261
- MI-000262
headline: The source claims scale-one tensor saturation for Spin(2n), n>=2, for dominant integral weights
  whose sum lies in the type-D root lattice, including half-integral spin weights and every positive stretching
  integer.
central_instrument: Nested-support matching computes generic intersection dimensions, and the nilpotent
  centralizer realizes all motions preserving the induced filtration on the kernel.
novelty_assessment: The intersection formula is a Hall-matching consequence and the centralizer action
  is explicitly compared with Fresse. The source-specific application is positioning subspaces in a zero-tail
  removal argument; the saturation theorem was not audited.
formalization_summary: No family-specific Lean scope document was listed in the pinned inventory. No Lean
  proof was certified.
statement_faithfulness: Generic means on a nonempty Zariski-open subset of the complex filtration stabilizer.
  The centralizer acts as the full stabilizer on the kernel and separately on the dual kernel; arbitrary
  independent prescribed motions on both are not asserted simultaneously.
dependencies: Hall matching, generic matrix rank, filtration-adapted bases, nilpotent Jordan modules and
  irreducible algebraic groups.
antecedents: Hall, On Representatives of Subsets, Theorem 1; Fresse, Betti numbers of Springer fibers
  in type A, Section 3.6.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Filtered intersection bounds and nilpotent centralizer motion

## Source manuscript and claim

[Tensor saturation for even spin groups](../papers/P-000150.md), by OpenAI, September 24, 2026.

The source claims scale-one tensor saturation for Spin(2n), n>=2, for dominant integral weights whose sum lies in the type-D root lattice, including half-integral spin weights and every positive stretching integer.

## Extracted instruments

- [MI-000261: Nested filtration profiles determine the generic intersection exactly](../instruments/MI-000261.md)
- [MI-000262: A nilpotent centralizer realizes every allowed motion of its kernel filtration](../instruments/MI-000262.md)

## Dependencies and antecedents

Hall matching, generic matrix rank, filtration-adapted bases, nilpotent Jordan modules and irreducible algebraic groups.

Hall, On Representatives of Subsets, Theorem 1; Fresse, Betti numbers of Springer fibers in type A, Section 3.6. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the complete filtered-intersection and centralizer proofs. Real schedules, integral continuation, simultaneous switches, representation criteria and the full zero-tail construction were not audited.

No family-specific Lean scope document was listed in the pinned inventory. No Lean proof was certified.

Generic means on a nonempty Zariski-open subset of the complex filtration stabilizer. The centralizer acts as the full stabilizer on the kernel and separately on the dual kernel; arbitrary independent prescribed motions on both are not asserted simultaneously.

[Batch record](../../batches/B019/README.md)

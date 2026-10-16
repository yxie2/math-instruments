---
id: openai-math-201
record_type: family
title: Annihilated resolvent poles and fixed-root Schur equations
source_family: '201'
source_collection: openai/math
batch_id: B019
subject: Algebra
source_paper_ids:
- P-000149
instrument_ids:
- MI-000259
- MI-000260
headline: The source claims a countable characteristic-zero division ring algebraic over its actual center,
  generated as an algebra over that center by two elements, but infinite-dimensional over the center.
central_instrument: Two vanishing couplings remove a simple resolvent pole. Over a truncated free algebra,
  fixed-root Schur equations are equivalent to one central polynomial identity.
novelty_assessment: Schur complements, spectral interpolation and nilpotent-ideal inversion are classical.
  The source packages them for its noncommutative correction process; the long lifting construction and
  division-ring conclusion were not audited.
formalization_summary: No family-specific Lean scope document was listed in the pinned inventory. No Lean
  proof was certified.
statement_faithfulness: The zero eigenvalue is semisimple and the derivative compressed to its kernel
  is invertible. Both couplings must annihilate the kernel at constant order. Fixed roots are distinct
  central scalars, although the coefficient ring itself is noncommutative.
dependencies: Block inversion, formal Laurent series, spectral projections, finite geometric inverses,
  central polynomial interpolation and free-word truncations.
antecedents: Classical Schur-complement inversion and polynomial spectral idempotents. No priority claim
  is made for these elementary linear-algebra mechanisms.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Annihilated resolvent poles and fixed-root Schur equations

## Source manuscript and claim

[A Counterexample to Kurosh’s Division-Ring Problem](../papers/P-000149.md), by OpenAI, September 23, 2026.

The source claims a countable characteristic-zero division ring algebraic over its actual center, generated as an algebra over that center by two elements, but infinite-dimensional over the center.

## Extracted instruments

- [MI-000259: Two vanishing couplings remove a simple resolvent pole and permit a fixed complement](../instruments/MI-000259.md)
- [MI-000260: Fixed-root Schur equations are equivalent to a polynomial identity over truncated free coefficients](../instruments/MI-000260.md)

## Dependencies and antecedents

Block inversion, formal Laurent series, spectral projections, finite geometric inverses, central polynomial interpolation and free-word truncations.

Classical Schur-complement inversion and polynomial spectral idempotents. No priority claim is made for these elementary linear-algebra mechanisms. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the complete killed-pole and Schur-polynomial proofs. The spectral-response, cyclic-compatibility, eleven-block correction, central division realization and actual-center descent arguments were not audited.

No family-specific Lean scope document was listed in the pinned inventory. No Lean proof was certified.

The zero eigenvalue is semisimple and the derivative compressed to its kernel is invertible. Both couplings must annihilate the kernel at constant order. Fixed roots are distinct central scalars, although the coefficient ring itself is noncommutative.

[Batch record](../../batches/B019/README.md)

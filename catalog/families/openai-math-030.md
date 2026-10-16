---
id: openai-math-030
record_type: family
title: Finite torsion control and integral character evaluation
source_family: '030'
source_collection: openai/math
batch_id: B042
subject: Number theory
source_paper_ids:
- P-000242
instrument_ids:
- MI-000446
- MI-000447
headline: The source claims modularity of elliptic curves over imaginary quadratic fields.
central_instrument: Bounded integral Frobenius polynomials are distinguishable at finite torsion precision.
  Evaluating a free integral group-ring module produces congruent lattices even at primes dividing the
  group order.
novelty_assessment: These use classical semistable reduction, finite-etale local constancy and integral
  base change. The source global automorphy chain remains separate.
formalization_summary: No formalization scope document is listed for this family in the pinned inventory.
  No Lean build.
statement_faithfulness: Use the full Tate-module Frobenius polynomial, retaining both toric and lattice
  pieces. Integral group-ring freeness is assumed before character evaluation; rational character projectors
  cannot supply it.
dependencies: Finite-etale torsion, semistable Tate-module filtration, Weil root bounds, bounded integer
  coefficients and integral group-ring base change.
antecedents: Grothendieck semistable reduction and monodromy; standard integral character specialization.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Finite torsion control and integral character evaluation

## Source manuscript and claim

[Modularity of elliptic curves over imaginary quadratic fields](../papers/P-000242.md), by OpenAI, October 4, 2026.

The source claims modularity of elliptic curves over imaginary quadratic fields.

## Extracted instruments

- [MI-000446: Recover a semistable Frobenius polynomial from sufficiently precise finite torsion](../instruments/MI-000446.md)
- [MI-000447: Compare residual character summands by integral group-ring evaluation](../instruments/MI-000447.md)

## Dependencies and antecedents

Finite-etale torsion, semistable Tate-module filtration, Weil root bounds, bounded integer coefficients and integral group-ring base change.

Grothendieck semistable reduction and monodromy; standard integral character specialization. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read local finite-torsion constancy, finite Frobenius polynomials and semistable-type constancy proofs, plus integral evaluation and its congruence corollary. The geometric group-ring freeness and automorphy inputs were not audited.

No formalization scope document is listed for this family in the pinned inventory. No Lean build.

Use the full Tate-module Frobenius polynomial, retaining both toric and lattice pieces. Integral group-ring freeness is assumed before character evaluation; rational character projectors cannot supply it.

[Batch record](../../batches/B042/README.md)

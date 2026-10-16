---
id: openai-math-006
record_type: family
title: Squareclass density transfer and rank-tail uniform integrability
source_family: '006'
source_collection: openai/math
batch_id: B065
subject: Number theory
source_paper_ids:
- P-000391
- P-000392
instrument_ids:
- MI-000622
- MI-000623
headline: The sources claim Goldfeld density and mean analytic rank for quadratic twists.
central_instrument: Mobius inversion transfers squareclass-invariant density to squarefree representatives.
  A truncated tail estimate plus an individual logarithmic bound gives uniform integrability.
novelty_assessment: The extracted arguments use classical ingredients. The particular source interfaces
  are recorded without certifying a new headline theorem or earliest priority.
formalization_summary: No Lean scope document or linked Comparator is supplied for this family in the
  pinned inventory. No formal solution was built.
statement_faithfulness: Density transfer assumes invariance under multiplication by positive integer squares.
  Mean-rank transfer assumes both the counting estimate and the individual rank bound; density alone is
  insufficient.
dependencies: Mobius inversion, summable square tails, layer-cake sums and dyadic decomposition.
antecedents: Classical Dirichlet convolution and the uniform-integrability criterion for convergence of
  means.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Squareclass density transfer and rank-tail uniform integrability

## Source manuscripts and claim

- [Goldfeld's analytic density conjecture and the 2-converse for elliptic curves](../papers/P-000391.md): selected passages extracted.
- [The mean analytic rank of quadratic twists of elliptic curves](../papers/P-000392.md): selected passages extracted.

The sources claim Goldfeld density and mean analytic rank for quadratic twists.

## Extracted instruments

- [MI-000622: Transfer an integer density to squarefree squareclasses](../instruments/MI-000622.md)
- [MI-000623: Upgrade truncated rank tails to uniform integrability](../instruments/MI-000623.md)

## Dependencies and antecedents

Mobius inversion, summable square tails, layer-cake sums and dyadic decomposition.

Classical Dirichlet convolution and the uniform-integrability criterion for convergence of means.

## Review and formalization scope

Read the complete squarefree-density lemma, the stated tail-count input, the complete Jensen bound, the rank-weighted tail proof and the final mean reduction. The source analytic counting and Goldfeld arguments remain unaudited.

No Lean scope document or linked Comparator is supplied for this family in the pinned inventory. No formal solution was built.

Density transfer assumes invariance under multiplication by positive integer squares. Mean-rank transfer assumes both the counting estimate and the individual rank bound; density alone is insufficient.

[Batch record](../../batches/B065/README.md)

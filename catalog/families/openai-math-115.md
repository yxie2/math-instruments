---
id: openai-math-115
record_type: family
title: Exact residual sampling and capacity-adapted forest coordinates
source_family: '115'
source_collection: openai/math
batch_id: B049
subject: Theoretical computer science
source_paper_ids:
- P-000271
- P-000272
instrument_ids:
- MI-000492
- MI-000493
headline: The sources claim exact uniform sampling for arbitrary contingency-table margins and an FPRAS
  with arbitrary individual cell bounds.
central_instrument: A rare residual branch removes an approximate sampler error exactly. A maximum-capacity
  forest prevents free-coordinate perturbations from being amplified relative to tree capacities.
novelty_assessment: Explicit antecedents are Gobel-Liu-Manurangsi-Pappik for exact correction and Cryan-Dyer-Randall
  for capacity-weighted spanning trees.
formalization_summary: The supplied target includes exact expected-polynomial sampling, bounded-time approximate
  sampling, and cell-bounded approximate counting, with binary encoded margins and freely varying dimensions.
  The scope document and all linked Comparator definitions and target statements were read. The selected
  targets contain sorry; no solution or Lean project was built.
statement_faithfulness: Residual probabilities require pointwise domination and exact distribution tabulation.
  Small-edge row and column incidences may disagree and must be retained separately in forest cut sums.
dependencies: Finite dyadic laws, exact integer sampling and expected-cost accounting; forest elimination,
  maximum-spanning-tree exchange and normalized piecewise-linear penalties.
antecedents: Gobel-Liu-Manurangsi-Pappik arXiv:2410.00882v2 Section 3.1; Cryan-Dyer-Randall Section 2.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Exact residual sampling and capacity-adapted forest coordinates

## Source manuscripts and claim

- [Exact Uniform Sampling of Contingency Tables with Arbitrary Margins](../papers/P-000271.md): selected passages extracted.
- [An FPRAS for Cell-Bounded Contingency Tables](../papers/P-000272.md): selected passages extracted.

The sources claim exact uniform sampling for arbitrary contingency-table margins and an FPRAS with arbitrary individual cell bounds.

## Extracted instruments

- [MI-000492: Correct a dyadic approximate sampler by a rare exact residual](../instruments/MI-000492.md)
- [MI-000493: Choose a maximum-capacity forest before normalizing free variables](../instruments/MI-000493.md)

## Dependencies and antecedents

Finite dyadic laws, exact integer sampling and expected-cost accounting; forest elimination, maximum-spanning-tree exchange and normalized piecewise-linear penalties.

Gobel-Liu-Manurangsi-Pappik arXiv:2410.00882v2 Section 3.1; Cryan-Dyer-Randall Section 2.

## Review and formalization scope

Read the full exact-sampling residual proof and the full forest-coordinate lemma, including its cut identity and Lipschitz estimate. The source approximate samplers, tabulation complexity and global counting schemes remain outside these checks.

The supplied target includes exact expected-polynomial sampling, bounded-time approximate sampling, and cell-bounded approximate counting, with binary encoded margins and freely varying dimensions. The scope document and all linked Comparator definitions and target statements were read. The selected targets contain sorry; no solution or Lean project was built.

Residual probabilities require pointwise domination and exact distribution tabulation. Small-edge row and column incidences may disagree and must be retained separately in forest cut sums.

[Batch record](../../batches/B049/README.md)

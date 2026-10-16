---
id: openai-math-086
record_type: family
title: Noncommuting nested-prefix bounds and two-earliest-increment expansions
source_family: 086
source_collection: openai/math
batch_id: B023
subject: Real and complex analysis
source_paper_ids:
- P-000166
instrument_ids:
- MI-000294
- MI-000295
headline: The source claims an L3 times L3 times L3 to L1 bound for the fixed trilinear Hilbert transform
  with slopes 1,2,3, and its unique bounded trilinear extension. It does not claim the full exponent range
  or arbitrary slopes.
central_instrument: Binary decomposition controls products of nested projection prefixes despite noncommutation
  between layers. Grouping a four-linear expansion by its two earliest increments leaves two later residuals
  and makes the terminal remainder explicit.
novelty_assessment: The source explicitly credits the Rademacher-Menshov binary mechanism. Multilinear
  telescoping is standard. The noncommuting projection formulation and staggered-accuracy organization
  are extracted without certifying the later compression, inverse-theorem transfer or scale summation.
formalization_summary: No family-specific Lean scope document is listed in the pinned release inventory
  for family 086. No formal proof project was built.
statement_faithfulness: Projection families increase within each layer; different layers need not commute.
  The earliest-increment expansion has a terminal remainder at every finite cutoff. Its decay and pairwise
  form-norm estimates need separate analytic accuracy and complexity hypotheses.
dependencies: Orthogonal increments, dyadic index blocks, Bessel row contractions, telescoping products,
  multilinearity and staggered approximation accuracies.
antecedents: Rademacher-Menshov binary decomposition, including Mikhailets-Murach Section 3 Lemma 1; classical
  multilinear telescoping and paraproduct organization.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Noncommuting nested-prefix bounds and two-earliest-increment expansions

## Source manuscript and claim

[An <i>L</i><sup>3</sup> bound for the trilinear Hilbert transform](../papers/P-000166.md), by OpenAI, October 5, 2026.

The source claims an L3 times L3 times L3 to L1 bound for the fixed trilinear Hilbert transform with slopes 1,2,3, and its unique bounded trilinear extension. It does not claim the full exponent range or arbitrary slopes.

## Extracted instruments

- [MI-000294: Binary blocks control row-selected products of noncommuting nested projections](../instruments/MI-000294.md)
- [MI-000295: Group a multilinear expansion by its two earliest increments and retain the remainder](../instruments/MI-000295.md)

## Dependencies and antecedents

Orthogonal increments, dyadic index blocks, Bessel row contractions, telescoping products, multilinearity and staggered approximation accuracies.

Rademacher-Menshov binary decomposition, including Mikhailets-Murach Section 3 Lemma 1; classical multilinear telescoping and paraproduct organization. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the full nested-prefix proof and two-earliest-increment proof, plus the preceding adaptive-approximation argument. Detection, the continuous inverse theorem, later compression and sparse-count estimates were not audited.

No family-specific Lean scope document is listed in the pinned release inventory for family 086. No formal proof project was built.

Projection families increase within each layer; different layers need not commute. The earliest-increment expansion has a terminal remainder at every finite cutoff. Its decay and pairwise form-norm estimates need separate analytic accuracy and complexity hypotheses.

[Batch record](../../batches/B023/README.md)

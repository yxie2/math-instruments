---
id: openai-math-164
record_type: family
title: Rational snapping and ordered product chains
source_family: '164'
source_collection: openai/math
batch_id: B036
subject: Combinatorics
source_paper_ids:
- P-000216
instrument_ids:
- MI-000394
- MI-000395
headline: The source claims finite monochromatic sums-and-products configurations in every finite coloring
  of the positive integers.
central_instrument: Near-integral polynomial samples snap to a rational polynomial with exact repeated-root
  divisibility; Ramsey homogenization by cardinality yields product blocks with separated tails and pivots.
novelty_assessment: Interpolation, denominator separation and finite Ramsey selection are classical. The
  source explicitly credits the product-chain architecture to Alweiss; the full integer sums-and-products
  theorem is not certified.
formalization_summary: No formalization scope document is listed for this family in the pinned inventory.
  No Lean build was performed.
statement_faithfulness: Interpolation thresholds may depend on the fixed interval length; its approximation
  constant depends only on the degree. The chain lemma produces monochromatic products alone; simultaneous
  sums require additional analytic principles.
dependencies: Rational Lagrange interpolation, smooth/rough coprimality, a repeated-root denominator lower
  bound, finite Ramsey and finite finite-sums selection.
antecedents: Classical integer-valued interpolation and finite Ramsey theory; Alweiss, Monochromatic sums
  and products over Q.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Rational snapping and ordered product chains

## Source manuscript and claim

[Monochromatic finite sums and products in the positive integers](../papers/P-000216.md), by OpenAI, September 23, 2026.

The source claims finite monochromatic sums-and-products configurations in every finite coloring of the positive integers.

## Extracted instruments

- [MI-000394: Turn near-integral samples into exact repeated-root divisibility](../instruments/MI-000394.md)
- [MI-000395: Choose monochromatic product blocks with ordered tails and pivots](../instruments/MI-000395.md)

## Dependencies and antecedents

Rational Lagrange interpolation, smooth/rough coprimality, a repeated-root denominator lower bound, finite Ramsey and finite finite-sums selection.

Classical integer-valued interpolation and finite Ramsey theory; Alweiss, Monochromatic sums and products over Q. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read rough interpolation, ordered-block definitions and the complete chain-selection proof. The source prediction and alignment principles, including nilsequence inputs, were not audited.

No formalization scope document is listed for this family in the pinned inventory. No Lean build was performed.

Interpolation thresholds may depend on the fixed interval length; its approximation constant depends only on the degree. The chain lemma produces monochromatic products alone; simultaneous sums require additional analytic principles.

[Batch record](../../batches/B036/README.md)

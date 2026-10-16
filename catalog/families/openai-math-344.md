---
id: openai-math-344
record_type: family
title: Weighted Jensen cancellation and endpoint Schur bounds
source_family: '344'
source_collection: openai/math
batch_id: B047
subject: Differential geometry
source_paper_ids:
- P-000256
instrument_ids:
- MI-000474
- MI-000475
headline: The source claims the metric Blaschke theorem.
central_instrument: A symmetric interval weight cancels endpoint terms into an integrated Jensen gap.
  Completing a Schur-complement derivative square works in either endpoint order.
novelty_assessment: Kazdan cancellation and classical Schur-complement algebra with a stated geometric
  interface. No metric Blaschke theorem or priority certification.
formalization_summary: No formalization scope document is listed for this family in the pinned inventory.
  No Lean project was built.
statement_faithfulness: Retain symmetry and endpoint integrability of the weight. Schur derivative bounds
  need H positive derivative and invertible endpoint difference; positive integrated bounds additionally
  require the source cut-pair zeros.
dependencies: Bounded logarithmic ratios, symmetric measurable weights, Fubini, Jensen, smooth block matrices,
  positive derivative H, and separately established cut-pair identities.
antecedents: Kazdan, An Inequality Arising in Geometry (1978), Appendix E; Boyd-Vandenberghe, Convex Optimization,
  Appendix A.5.5.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Weighted Jensen cancellation and endpoint Schur bounds

## Source manuscripts and claim

- [The metric Blaschke theorem](../papers/P-000256.md): selected passages extracted.

The source claims the metric Blaschke theorem.

## Extracted instruments

- [MI-000474: Turn a weighted interval comparison into an integrated Jensen gap](../instruments/MI-000474.md)
- [MI-000475: Differentiate an endpoint Schur complement without assuming endpoint order](../instruments/MI-000475.md)

## Dependencies and antecedents

Bounded logarithmic ratios, symmetric measurable weights, Fubini, Jensen, smooth block matrices, positive derivative H, and separately established cut-pair identities.

Kazdan, An Inequality Arising in Geometry (1978), Appendix E; Boyd-Vandenberghe, Convex Optimization, Appendix A.5.5.

## Review and formalization scope

Read the full weighted scalar proof and full Schur-complement proposition. The source explicitly attributes the cancellation to Kazdan; only the publisher preview was retrieved for that appendix. Boyd-Vandenberghe A.5.5 was read directly. The geometric construction of the blocks and cut-pair zeros was not audited.

No formalization scope document is listed for this family in the pinned inventory. No Lean project was built.

Retain symmetry and endpoint integrability of the weight. Schur derivative bounds need H positive derivative and invertible endpoint difference; positive integrated bounds additionally require the source cut-pair zeros.

[Batch record](../../batches/B047/README.md)

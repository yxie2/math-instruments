---
id: openai-math-088
record_type: family
title: Affine balancing and multiplicative projection-body tests
source_family: 088
source_collection: openai/math
batch_id: B048
subject: Convex and metric geometry
source_paper_ids:
- P-000259
- P-000260
instrument_ids:
- MI-000480
- MI-000481
headline: The principal source claims Petty projection-volume rigidity in dimensions at least four; its
  companion gives a product-of-simplices counterexample to a proposed maximum.
central_instrument: A strictly inward covariance field has an interior zero by projected fixed points.
  Projection-body ratios multiply under Cartesian products, converting comparison into exact arithmetic.
novelty_assessment: Brouwer projection, Gaussian moments and Cauchy projection formulas are classical.
  The source product witness is reproduced algebraically; no independent historical-priority claim.
formalization_summary: The supplied scope describes the n>=4 lower bound with ellipsoid equality and the
  dimension-20 product counterexample. It excludes the companion all-large-dimension exponential excess.
  The scope document and linked Comparator definitions and target statements were read. The inspected
  targets contain sorry; no solution or Lean project was built.
statement_faithfulness: Affine balancing assumes a continuous nonzero seminorm assignment with the specified
  kernel dependence. The product formula uses the factor 1/2 in Cauchy projection and the normalization
  |Pi K|/|K|^(d-1).
dependencies: Continuity of the source variational minimizers, Gaussian radial moments, nearest-point
  projection, Cauchy projection formula, product facets and simplex volumes.
antecedents: Classical Brouwer fixed points and Cauchy projection; Saroglou supplies a checked primary
  statement of the projection formula and affine invariance.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Affine balancing and multiplicative projection-body tests

## Source manuscripts and claim

- [Petty’s projection-volume conjecture in dimensions at least four](../papers/P-000259.md): selected passages extracted.
- [A product counterexample to the simplex maximum for projection-body volume](../papers/P-000260.md): selected passages extracted.

The principal source claims Petty projection-volume rigidity in dimensions at least four; its companion gives a product-of-simplices counterexample to a proposed maximum.

## Extracted instruments

- [MI-000480: Find an interior balancing zero by projecting a strictly inward field](../instruments/MI-000480.md)
- [MI-000481: Multiply normalized projection-body volumes using Cartesian products](../instruments/MI-000481.md)

## Dependencies and antecedents

Continuity of the source variational minimizers, Gaussian radial moments, nearest-point projection, Cauchy projection formula, product facets and simplex volumes.

Classical Brouwer fixed points and Cauchy projection; Saroglou supplies a checked primary statement of the projection formula and affine invariance.

## Review and formalization scope

Read the selected fixed-point and affine-position proofs, and the companion facet, product, affine covariance, simplex and dimension-20 comparison proofs. Continuity and existence of the principal variational minimizers were left as inputs. Both manuscripts have extracted passages.

The supplied scope describes the n>=4 lower bound with ellipsoid equality and the dimension-20 product counterexample. It excludes the companion all-large-dimension exponential excess. The scope document and linked Comparator definitions and target statements were read. The inspected targets contain sorry; no solution or Lean project was built.

Affine balancing assumes a continuous nonzero seminorm assignment with the specified kernel dependence. The product formula uses the factor 1/2 in Cauchy projection and the normalization |Pi K|/|K|^(d-1).

[Batch record](../../batches/B048/README.md)

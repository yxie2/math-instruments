---
id: openai-math-355
record_type: family
title: Delayed error summation and Gevrey bounds from stopped approximants
source_family: '355'
source_collection: openai/math
batch_id: B053
subject: Differential geometry
source_paper_ids:
- P-000292
instrument_ids:
- MI-000522
- MI-000523
headline: The source claims uniqueness, in the fixed ambient frame, of every tangent flow at the first
  singular time of a closed embedded surface in three-space.
central_instrument: Delayed radii turn cutoff tails into a summable convolution that can be absorbed.
  Exponentially close holomorphic approximants on shrinking disks yield all-orders Gevrey remainders.
novelty_assessment: Discrete gradient-length summation has a Colding-Minicozzi antecedent; exponentially
  flat differences and Gevrey asymptotics are classical. The precise delayed-radius and stopped-disk interfaces
  are source arguments without exhaustive priority certification.
formalization_summary: No family scope document or Comparator target is listed in the pinned inventory.
  No formal verification is claimed.
statement_faithfulness: Finite-length control assumes the discrete gradient inequality and a sufficiently
  small initial energy. Gevrey control assumes holomorphy on complete shrinking disks and exponential
  differences; it does not follow from a merely formal series.
dependencies: Energy monotonicity, concavity, good/bad index splitting, finite nonnegative convolution
  sums; Cauchy estimates, exponential moments and stopped Taylor expansions.
antecedents: Colding-Minicozzi discrete Lojasiewicz length estimates; the classical Ramis-Sibuya mechanism
  for Gevrey asymptotics.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Delayed error summation and Gevrey bounds from stopped approximants

## Source manuscripts and claim

- [Uniqueness of tangent flows at the first singular time of embedded surface mean-curvature flow](../papers/P-000292.md): selected passages extracted.

The source claims uniqueness, in the fixed ambient frame, of every tangent flow at the first singular time of a closed embedded surface in three-space.

## Extracted instruments

- [MI-000522: Absorb delayed Gaussian errors on every finite energy prefix](../instruments/MI-000522.md)
- [MI-000523: Convert exponentially close stopped approximants into all-orders Gevrey bounds](../instruments/MI-000523.md)

## Dependencies and antecedents

Energy monotonicity, concavity, good/bad index splitting, finite nonnegative convolution sums; Cauchy estimates, exponential moments and stopped Taylor expansions.

Colding-Minicozzi discrete Lojasiewicz length estimates; the classical Ramis-Sibuya mechanism for Gevrey asymptotics.

## Review and formalization scope

Read the full delayed-radius setup and finite-prefix summation proof, and the complete geometric-telescoping proof including coefficient identification and transfer to sector arrays. The geometric propagation, normalized contour inverses and no-critical-arc argument remain unverified.

No family scope document or Comparator target is listed in the pinned inventory. No formal verification is claimed.

Finite-length control assumes the discrete gradient inequality and a sufficiently small initial energy. Gevrey control assumes holomorphy on complete shrinking disks and exponential differences; it does not follow from a merely formal series.

[Batch record](../../batches/B053/README.md)

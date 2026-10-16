---
id: openai-math-212
record_type: family
title: Raywise metric limits and convex boundary regularity
source_family: '212'
source_collection: openai/math
batch_id: B077
subject: Probability and statistical mechanics
source_paper_ids:
- P-000484
- P-000485
instrument_ids:
- MI-000718
- MI-000719
headline: The family claims absence of planar bigeodesics, differentiability of Gamma first-passage norms
  and strict convexity in the exponential case.
central_instrument: Subtract distance along a calibrated ray to obtain a monotone limit; turn unique supports
  into continuous derivatives and regular boundary charts.
novelty_assessment: Selected mechanisms are separated from source headline claims and credited to known
  antecedents where established. Exhaustive priority is not established.
formalization_summary: PlanarFirstPassage and GammaPassage target actual deterministic passage-time norms
  with differentiability and regular C1 boundary charts. The selected targets omit strict convexity and
  absence of bigeodesics. The complete scope and named Comparators were read. Inspected theorem targets
  contain sorry; no separate solution or Lean build was checked.
statement_faithfulness: A ray must minimize every finite subsegment. Convex regularity assumes uniqueness
  of supports at every nonzero direction; that uniqueness is not supplied by the final deterministic lemma.
dependencies: Triangle inequalities, geodesic calibration, one-sided convex derivatives, compact dual
  balls and the implicit function theorem.
antecedents: Classical Busemann functions and finite-dimensional convex analysis.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Raywise metric limits and convex boundary regularity

## Source manuscripts and claim

- [No bigeodesics in planar first-passage percolation](../papers/P-000484.md): selected passages extracted.
- [Strict convexity and differentiability of the planar exponential first-passage limit shape](../papers/P-000485.md): selected passages extracted.

The family claims absence of planar bigeodesics, differentiability of Gamma first-passage norms and strict convexity in the exponential case.

## Extracted instruments

- [MI-000718: Measure calibration error by a decreasing raywise sequence](../instruments/MI-000718.md)
- [MI-000719: Upgrade unique supports to a regular C1 norm sphere](../instruments/MI-000719.md)

## Dependencies and antecedents

Triangle inequalities, geodesic calibration, one-sided convex derivatives, compact dual balls and the implicit function theorem.

Classical Busemann functions and finite-dimensional convex analysis.

## Review and formalization scope

Read the complete finite-minimizer and elementary Busemann proofs in the bigeodesic manuscript and the convex-boundary proof in the limit-shape manuscript. Both manuscripts receive extractions. The probabilistic no-corner and no-bigeodesic arguments are not certified.

PlanarFirstPassage and GammaPassage target actual deterministic passage-time norms with differentiability and regular C1 boundary charts. The selected targets omit strict convexity and absence of bigeodesics. The complete scope and named Comparators were read. Inspected theorem targets contain sorry; no separate solution or Lean build was checked.

A ray must minimize every finite subsegment. Convex regularity assumes uniqueness of supports at every nonzero direction; that uniqueness is not supplied by the final deterministic lemma.

[Batch record](../../batches/B077/README.md)

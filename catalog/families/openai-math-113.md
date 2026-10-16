---
id: openai-math-113
record_type: family
title: Tight multiplicative scaling and a covariance trace obstruction
source_family: '113'
source_collection: openai/math
batch_id: B049
subject: Theoretical computer science
source_paper_ids:
- P-000267
- P-000268
instrument_ids:
- MI-000488
- MI-000489
headline: The sources claim an FPRAS for general perfect matchings and refined maximum-entropy bounds
  throughout the matching polytope.
central_instrument: A single decreasing coordinate sweep makes every multiplicative constraint row tight.
  Exponential tilts turn a local entropy comparison into a trace inequality on the minimal face.
novelty_assessment: Coordinate feasibility and exponential-family covariance are classical. The selected
  trace reduction is recorded as a source argument, without a priority claim or certification of the global
  matching results.
formalization_summary: The supplied scope includes the general-graph FPRAS, pointwise entropy bounds,
  earlier deterministic approximations and a triangle-expansion face correspondence. Its selected face
  target excludes the sharp global face-dimension bound. The scope document and all linked Comparator
  definitions and target statements were read. The selected targets contain sorry; no solution or Lean
  project was built.
statement_faithfulness: Positive symmetric off-diagonal data and feasible initialization are essential
  for the sweep. The trace conclusion is necessary at a relative interior local maximum, with all retained
  marginals strictly between zero and one.
dependencies: Monotone coordinate updates; finite-support maximum entropy, exponential families, covariance
  rank and a second-variation argument on the face tangent space.
antecedents: Elementary feasibility-preserving scaling; Wainwright-Jordan Section 3.5.1 for exponential-family
  derivatives and covariance rank.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Tight multiplicative scaling and a covariance trace obstruction

## Source manuscripts and claim

- [A Fully Polynomial Randomized Approximation Scheme for Perfect Matchings in General Graphs](../papers/P-000267.md): selected passages extracted.
- [Entropy and Face Dimension of the Perfect-Matching Polytope](../papers/P-000268.md): selected passages extracted.

The sources claim an FPRAS for general perfect matchings and refined maximum-entropy bounds throughout the matching polytope.

## Extracted instruments

- [MI-000488: Make every row tight by one decreasing multiplicative sweep](../instruments/MI-000488.md)
- [MI-000489: Use covariance rank to obstruct an interior entropy maximum](../instruments/MI-000489.md)

## Dependencies and antecedents

Monotone coordinate updates; finite-support maximum entropy, exponential families, covariance rank and a second-variation argument on the face tangent space.

Elementary feasibility-preserving scaling; Wainwright-Jordan Section 3.5.1 for exponential-family derivatives and covariance rank.

## Review and formalization scope

Read the full one-pass-scaling proof and the companion continuity, exponential representation and covariance-trace proofs. The FPRAS, face-dimension lower bound and global induction are not certified by this extraction.

The supplied scope includes the general-graph FPRAS, pointwise entropy bounds, earlier deterministic approximations and a triangle-expansion face correspondence. Its selected face target excludes the sharp global face-dimension bound. The scope document and all linked Comparator definitions and target statements were read. The selected targets contain sorry; no solution or Lean project was built.

Positive symmetric off-diagonal data and feasible initialization are essential for the sweep. The trace conclusion is necessary at a relative interior local maximum, with all retained marginals strictly between zero and one.

[Batch record](../../batches/B049/README.md)

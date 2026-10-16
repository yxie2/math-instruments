---
id: openai-math-146
record_type: family
title: Matrix growth geometry and positive dilation balances
source_family: '146'
source_collection: openai/math
batch_id: B051
subject: Dynamical systems and ergodic theory
source_paper_ids:
- P-000283
instrument_ids:
- MI-000504
- MI-000505
headline: The source claims positive metric entropy for every sufficiently large parameter of the standard
  map.
central_instrument: Two-dimensional singular directions turn logarithmic matrix growth into approximate
  tree geometry. A positive dilation balance splits locally finite mass into backward images of a source
  and an invariant remainder.
novelty_assessment: Classical singular-value geometry and positive potential decomposition. The source
  gives a specific scale-limit interface; no exhaustive novelty claim.
formalization_summary: The three targets specify positive area entropy for a full parameter tail, positive
  largest Lyapunov exponents, and an invariant positive-area hyperbolic ergodic component with finitely
  many cyclic Bernoulli pieces. The scope document and all linked Comparator definitions and targets were
  read. Their target proofs contain sorry; no solution or Lean project was built.
statement_faithfulness: The matrix estimate is for real two-dimensional determinant-one matrices. The
  measure decomposition needs an invertible map on the supported space and locally finite positive measures;
  total masses may be infinite.
dependencies: Singular-value decomposition, the sine triangle inequality, properness for vague convergence
  and monotone convergence for positive measures.
antecedents: Gromov-product and real-tree limit geometry, as reviewed by Bestvina; classical positive
  potential and invariant decompositions.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Matrix growth geometry and positive dilation balances

## Source manuscripts and claim

- [Positive Metric Entropy for the Standard Map at Large Parameters](../papers/P-000283.md): selected passages extracted.

The source claims positive metric entropy for every sufficiently large parameter of the standard map.

## Extracted instruments

- [MI-000504: Read approximate tree geometry from determinant-one matrix growth](../instruments/MI-000504.md)
- [MI-000505: Split a positive dilation balance without subtracting infinite masses](../instruments/MI-000505.md)

## Dependencies and antecedents

Singular-value decomposition, the sine triangle inequality, properness for vague convergence and monotone convergence for positive measures.

Gromov-product and real-tree limit geometry, as reviewed by Bestvina; classical positive potential and invariant decompositions.

## Review and formalization scope

Read the complete four-point and cancellation-truncation proofs, the local-limit proof, and the positive dilation decomposition. The cancellation-scarcity, fast-bridge and final entropy arguments were not certified.

The three targets specify positive area entropy for a full parameter tail, positive largest Lyapunov exponents, and an invariant positive-area hyperbolic ergodic component with finitely many cyclic Bernoulli pieces. The scope document and all linked Comparator definitions and targets were read. Their target proofs contain sorry; no solution or Lean project was built.

The matrix estimate is for real two-dimensional determinant-one matrices. The measure decomposition needs an invertible map on the supported space and locally finite positive measures; total masses may be infinite.

[Batch record](../../batches/B051/README.md)

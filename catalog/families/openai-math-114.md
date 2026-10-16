---
id: openai-math-114
record_type: family
title: Barycentric slack centers and observable-specific variance bounds
source_family: '114'
source_collection: openai/math
batch_id: B049
subject: Theoretical computer science
source_paper_ids:
- P-000269
- P-000270
instrument_ids:
- MI-000490
- MI-000491
headline: The sources claim approximate counting of common integer polymatroid bases and common bases
  of two matroids.
central_instrument: Determinant exchanges create a center controlling every nonnegative affine slack.
  A restricted Poincare inequality controls the time average of selected observables without a full-chain
  relaxation bound.
novelty_assessment: 'Both cores have explicit antecedents: Awerbuch-Kleinberg barycentric spanners and
  Chen-Vigoda-Yang restricted empirical-variance bounds.'
formalization_summary: The supplied scope and Comparator concern common bases of two equal-rank matroids
  with independence oracles; they do not state the binary-capacity polymatroid companion extension. The
  scope document and all linked Comparator definitions and target statements were read. The selected targets
  contain sorry; no solution or Lean project was built.
statement_faithfulness: The slack center requires a bounded rational polytope and a suitable vertex optimization
  oracle for the complexity claim. The variance estimate requires the restricted inequality for every
  test function, not merely for functions already in the observed subspace.
dependencies: Affine coordinates, determinant exchanges, vertex encoding bounds; reversibility, laziness,
  an orthogonal projection fixing constants and warm-start domination.
antecedents: Awerbuch-Kleinberg Proposition 2.4; Chen-Vigoda-Yang Theorem 5(ii) and Section 3.6.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Barycentric slack centers and observable-specific variance bounds

## Source manuscripts and claim

- [An FPRAS for Common Integer Polymatroid Bases with Binary Capacities](../papers/P-000269.md): selected passages extracted.
- [Approximate counting of common bases of two matroids](../papers/P-000270.md): selected passages extracted.

The sources claim approximate counting of common integer polymatroid bases and common bases of two matroids.

## Extracted instruments

- [MI-000490: Build one center that controls every affine slack](../instruments/MI-000490.md)
- [MI-000491: Bound empirical error using only the observed subspace](../instruments/MI-000491.md)

## Dependencies and antecedents

Affine coordinates, determinant exchanges, vertex encoding bounds; reversibility, laziness, an orthogonal projection fixing constants and warm-start domination.

Awerbuch-Kleinberg Proposition 2.4; Chen-Vigoda-Yang Theorem 5(ii) and Section 3.6.

## Review and formalization scope

Read the full center lemma and the full empirical-time-average lemma. The counting algorithms and their geometric or restricted-Poincare inputs were not certified.

The supplied scope and Comparator concern common bases of two equal-rank matroids with independence oracles; they do not state the binary-capacity polymatroid companion extension. The scope document and all linked Comparator definitions and target statements were read. The selected targets contain sorry; no solution or Lean project was built.

The slack center requires a bounded rational polytope and a suitable vertex optimization oracle for the complexity claim. The variance estimate requires the restricted inequality for every test function, not merely for functions already in the observed subspace.

[Batch record](../../batches/B049/README.md)

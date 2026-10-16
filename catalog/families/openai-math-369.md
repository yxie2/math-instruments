---
id: openai-math-369
record_type: family
title: Regularize reciprocal Green kernels while preserving one positive direction
source_family: '369'
source_collection: openai/math
batch_id: B027
subject: Partial differential equations
source_paper_ids:
- P-000180
instrument_ids:
- MI-000322
- MI-000323
headline: The source claims that every nonzero first positive Neumann eigenfunction on every smooth bounded
  simply connected planar domain has no interior critical point and satisfies strict boundary extrema.
central_instrument: A positive-semidefinite defect of a logarithmic mean regularizes the singular Green
  kernel. Column-based resolvent updates preserve the one-positive-eigenvalue property of entrywise reciprocals.
novelty_assessment: Reciprocal one-positive-eigenvalue criteria have a direct antecedent in McCullough-Quiggin
  theory as presented by Agler-McCarthy. Bernstein representations of logarithmic means also predate this
  source. The concrete Green regularization and update packaging are extracted without certifying the
  hot-spots claim.
formalization_summary: Read HotSpots.lean and its scope document. It defines smooth domains, weak H1 gradients,
  a Rayleigh-infimum first value and every nonzero member of its eigenspace, including multiplicities.
  The inspected Comparator ends in sorry. It is a target statement, not a Lean proof built or kernel-checked
  here.
statement_faithfulness: Reciprocal always means entrywise reciprocal, not a matrix inverse. A column update
  uses a column of the current kernel. The regularized kernel is pointwise positive; a separate positive
  quadratic-form claim is not needed for the stated operator domination.
dependencies: Schur product theorem, logarithmic-mean integral representations, congruence and inertia,
  and geometric series.
antecedents: Agler-McCarthy, Complete Nevanlinna-Pick Kernels, Corollary 1.12; Qi-Zhang-Li, arXiv:1303.3122,
  Theorem 4.1 and Corollary 4.1; classical Schoenberg distance construction.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Regularize reciprocal Green kernels while preserving one positive direction

## Source manuscript and claim

[Strict hot spots and absence of interior critical points on smooth simply connected planar domains](../papers/P-000180.md), by OpenAI, September 24, 2026.

The source claims that every nonzero first positive Neumann eigenfunction on every smooth bounded simply connected planar domain has no interior critical point and satisfies strict boundary extrema.

## Extracted instruments

- [MI-000322: Regularize a logarithmic Green singularity through a positive-semidefinite defect](../instruments/MI-000322.md)
- [MI-000323: Preserve reciprocal inertia under current-column updates](../instruments/MI-000323.md)

## Dependencies and antecedents

Schur product theorem, logarithmic-mean integral representations, congruence and inertia, and geometric series.

Agler-McCarthy, Complete Nevanlinna-Pick Kernels, Corollary 1.12; Qi-Zhang-Li, arXiv:1303.3122, Theorem 4.1 and Corollary 4.1; classical Schoenberg distance construction. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the complete regularization and update proofs, the quadrature-resolvent propagation, and the final conditional-negative-type argument. Only the statement and initial radial-limit part of the bordered boundary lemma were read; its entire boundary-limit proof and the global spectral reduction were not audited.

Read HotSpots.lean and its scope document. It defines smooth domains, weak H1 gradients, a Rayleigh-infimum first value and every nonzero member of its eigenspace, including multiplicities. The inspected Comparator ends in sorry. It is a target statement, not a Lean proof built or kernel-checked here.

Reciprocal always means entrywise reciprocal, not a matrix inverse. A column update uses a column of the current kernel. The regularized kernel is pointwise positive; a separate positive quadratic-form claim is not needed for the stated operator domination.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/369.md) · [Batch record](../../batches/B027/README.md)

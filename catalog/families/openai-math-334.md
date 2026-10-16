---
id: openai-math-334
record_type: family
title: Prescribed curvature and smooth accumulation with a flat Taylor jet
source_family: '334'
source_collection: openai/math
batch_id: B029
subject: Differential geometry
source_paper_ids:
- P-000188
instrument_ids:
- MI-000338
- MI-000339
headline: The source claims a smooth positive surface metric on (-1,1)^2 for which no neighborhood of
  the origin admits a smooth isometric immersion into R3; its metric can have the Euclidean Taylor jet
  at the origin.
central_instrument: A scalar ODE realizes a small curvature function in semigeodesic coordinates. Diagonal
  seminorm budgets let infinitely many local tensor modifications accumulate while preserving smoothness,
  positivity and all prescribed jets.
novelty_assessment: The prescribed-curvature ODE is explicit in Khuri 2009, page 453, which was checked.
  Diagonal smooth summation is classical. The local obstruction needed for the source nonimmersion conclusion
  is not certified here.
formalization_summary: Read IsometricImmersion.lean and its scope. The target constructs a smooth positive-definite
  metric and excludes every smooth isometric candidate on every open neighborhood of the origin contained
  in the coordinate square. The inspected Comparator contains a sorry target, not a proof built or kernel-checked
  here.
statement_faithfulness: Curvature is invariant under actual pullback; the lambda^2 factor in the pulled-back
  metric must be retained. Pushing a covariant two-tensor back to ambient coordinates costs lambda^{-2}
  before taking derivatives. A Euclidean Taylor jet alone is not the nonimmersion obstruction.
dependencies: Smooth parameter-dependent ODEs, the semigeodesic curvature formula, tensor coordinate transformations
  and uniform convergence of every derivative series.
antecedents: Marcus Khuri, On the local solvability of Darboux equation, 2009, page 453; classical diagonal
  smooth-series constructions.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Prescribed curvature and smooth accumulation with a flat Taylor jet

## Source manuscript and claim

[A Smooth Metric with No Local Isometric Immersion into Three-Space](../papers/P-000188.md), by OpenAI, None.

The source claims a smooth positive surface metric on (-1,1)^2 for which no neighborhood of the origin admits a smooth isometric immersion into R3; its metric can have the Euclidean Taylor jet at the origin.

## Extracted instruments

- [MI-000338: Realize a small arbitrary curvature function through a scalar ODE](../instruments/MI-000338.md)
- [MI-000339: Pay coordinate-scaling costs before summing accumulating local perturbations](../instruments/MI-000339.md)

## Dependencies and antecedents

Smooth parameter-dependent ODEs, the semigeodesic curvature formula, tensor coordinate transformations and uniform convergence of every derivative series.

Marcus Khuri, On the local solvability of Darboux equation, 2009, page 453; classical diagonal smooth-series constructions. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the prescribed-curvature proof, the full placement and smooth-summation construction, and the Euclidean-jet corollary. The cap regularity, pulse obstruction and negative-disk obstruction were not audited.

Read IsometricImmersion.lean and its scope. The target constructs a smooth positive-definite metric and excludes every smooth isometric candidate on every open neighborhood of the origin contained in the coordinate square. The inspected Comparator contains a sorry target, not a proof built or kernel-checked here.

Curvature is invariant under actual pullback; the lambda^2 factor in the pulled-back metric must be retained. Pushing a covariant two-tensor back to ambient coordinates costs lambda^{-2} before taking derivatives. A Euclidean Taylor jet alone is not the nonimmersion obstruction.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/334.md) · [Batch record](../../batches/B029/README.md)

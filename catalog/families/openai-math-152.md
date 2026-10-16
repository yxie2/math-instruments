---
id: openai-math-152
record_type: family
title: Stationary chord control and sparse cheap-scale selection
source_family: '152'
source_collection: openai/math
batch_id: B051
subject: Dynamical systems and ergodic theory
source_paper_ids:
- P-000285
instrument_ids:
- MI-000508
- MI-000509
headline: The source claims a zero-entropy ergodic system with no smooth positive-volume model in any
  finite dimension.
central_instrument: Second-moment losses of adjacent block averages control maximal deviations from each
  block own chord. Divergent weighted scale budgets force a subsequence where any summable cost is negligible.
novelty_assessment: Dyadic interpolation and convolution are classical tools; the exact stationary chord
  estimate is recorded from the source without a settled priority claim. The scale-selection step is an
  elementary summability contradiction.
formalization_summary: The target gives a standard nonatomic invertible ergodic finite-entropy system
  with no measurable conjugacy to a smooth diffeomorphism preserving a strictly positive smooth density
  on any compact finite-dimensional manifold, including boundary. The source stronger zero-entropy conclusion
  is outside this target; arbitrary full-support or merely equivalent-to-volume measures are not excluded.
  The scope document and all linked Comparator definitions and targets were read. Their target proofs
  contain sorry; no solution or Lean project was built.
statement_faithfulness: The stationary estimate uses the random average of each block, not the process
  mean, and needs only a finite second moment. Scale selection needs divergent weighted availability in
  disjoint scale windows.
dependencies: Stationarity, quadratic averaging identity, dyadic polygon interpolation, Minkowski inequality,
  summable convolution and a weighted pigeonhole argument.
antecedents: Classical dyadic maximal and square-function methods; elementary summability versus divergent
  weighted budgets.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Stationary chord control and sparse cheap-scale selection

## Source manuscripts and claim

- [A zero-entropy system without a smooth positive-volume model](../papers/P-000285.md): selected passages extracted.

The source claims a zero-entropy ergodic system with no smooth positive-volume model in any finite dimension.

## Extracted instruments

- [MI-000508: Control stationary fluctuations relative to each dyadic block chord](../instruments/MI-000508.md)
- [MI-000509: Choose scales where a summable cost loses to a divergent test budget](../instruments/MI-000509.md)

## Dependencies and antecedents

Stationarity, quadratic averaging identity, dyadic polygon interpolation, Minkowski inequality, summable convolution and a weighted pigeonhole argument.

Classical dyadic maximal and square-function methods; elementary summability versus divergent weighted budgets.

## Review and formalization scope

Read the complete dyadic chord lemma, cheap-scale lemma and supporting word-rate proof, plus the introduction delimiting the realization problem. The smooth switching theorem and symbolic construction were not certified.

The target gives a standard nonatomic invertible ergodic finite-entropy system with no measurable conjugacy to a smooth diffeomorphism preserving a strictly positive smooth density on any compact finite-dimensional manifold, including boundary. The source stronger zero-entropy conclusion is outside this target; arbitrary full-support or merely equivalent-to-volume measures are not excluded. The scope document and all linked Comparator definitions and targets were read. Their target proofs contain sorry; no solution or Lean project was built.

The stationary estimate uses the random average of each block, not the process mean, and needs only a finite second moment. Scale selection needs divergent weighted availability in disjoint scale windows.

[Batch record](../../batches/B051/README.md)

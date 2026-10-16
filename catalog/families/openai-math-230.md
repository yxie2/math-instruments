---
id: openai-math-230
record_type: family
title: Moment-built gauges and integrable collision kernels
source_family: '230'
source_collection: openai/math
batch_id: B079
subject: Probability and statistical mechanics
source_paper_ids:
- P-000497
instrument_ids:
- MI-000740
- MI-000741
headline: The family claims exact Hausdorff gauges for SLE, through moment batches and an explicit asymptotic
  formula.
central_instrument: Build a nondegenerate gauge from finite moment batches and control nearest-neighbor
  singularities by directed graph elimination.
novelty_assessment: Known finite mechanisms are credited separately from source headline claims. Exhaustive
  novelty is not established.
formalization_summary: SLELowerPositivity targets only positivity of the explicit small-radius gauge on
  every nontrivial compact positive-time SLE segment. It does not state a finite upper measure or identify
  the moment-batch envelope with that formula. Full scope and named Comparator read; other linked Comparators
  were not inspected. The target contains sorry; no separate solution or Lean build was checked.
statement_faithfulness: The gauge construction assumes positive finite moments of a nonnegative mass and
  monotone approximating masses. The kernel estimate requires exponent alpha<1 in the plane.
dependencies: Dyadic geometric sums, moment tail truncation, quadratic envelope regularization, Tonelli
  and Cauchy-Schwarz.
antecedents: Peres-Solomyak quadratic gauge regularization and elementary integrability of planar power
  kernels.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Moment-built gauges and integrable collision kernels

## Source manuscripts and claim

- [An exact Hausdorff gauge for SLE](../papers/P-000497.md): selected passages extracted.

The following companions are inventoried but have no extraction in this batch:

- [An explicit exact Hausdorff gauge for SLE](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/An-explicit-exact-Hausdorff-gauge-for-SLE-September-26-2026)

The family claims exact Hausdorff gauges for SLE, through moment batches and an explicit asymptotic formula.

## Extracted instruments

- [MI-000740: Build a positive quadratic gauge from repeated moment thresholds](../instruments/MI-000740.md)
- [MI-000741: Integrate nearest-neighbor collision products using directed graph elimination](../instruments/MI-000741.md)

## Dependencies and antecedents

Dyadic geometric sums, moment tail truncation, quadratic envelope regularization, Tonelli and Cauchy-Schwarz.

Peres-Solomyak quadratic gauge regularization and elementary integrability of planar power kernels.

## Review and formalization scope

Read the complete moment-batch, gauge-admissibility, finite-exclusion and collision-kernel proofs. The explicit-gauge companion is inventory-only. SLE mass construction and covering arguments are not certified.

SLELowerPositivity targets only positivity of the explicit small-radius gauge on every nontrivial compact positive-time SLE segment. It does not state a finite upper measure or identify the moment-batch envelope with that formula. Full scope and named Comparator read; other linked Comparators were not inspected. The target contains sorry; no separate solution or Lean build was checked.

The gauge construction assumes positive finite moments of a nonnegative mass and monotone approximating masses. The kernel estimate requires exponent alpha<1 in the plane.

[Batch record](../../batches/B079/README.md)

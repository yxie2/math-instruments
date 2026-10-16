---
id: openai-math-140
record_type: family
title: Selection costs and posterior-replica information
source_family: '140'
source_collection: openai/math
batch_id: B075
subject: Theoretical computer science
source_paper_ids:
- P-000473
- P-000474
instrument_ids:
- MI-000704
- MI-000705
headline: The family claims memory-sample and precision lower bounds for exact Gaussian observations.
central_instrument: A shared support makes selection among N continuations cost N^(1/p); replica correlation
  loss bounds conditional information in a finite message.
novelty_assessment: Selected local mechanisms are distinguished from the manuscripts headline claims.
  Primary comparisons identify established antecedents; exhaustive priority is not established.
formalization_summary: Read the complete scope and both named Comparators. They specify finite-state noiseless
  Gaussian regression, fixed-quadratic and subquadratic memory targets, exact equal-label measures and
  several block-information comparisons. The other six listed Comparators were not inspected. Inspected
  theorem targets contain sorry; no separate solution or Lean build was checked.
statement_faithfulness: Selection uses one reference measure and one common domain. Replica signals must
  have matching joint laws with the message; equal signal marginals alone are insufficient, and side randomness
  is independent.
dependencies: Holder inequalities, relative-entropy chain rules, coordinatewise data processing and posterior
  resampling.
antecedents: Classical selection inequalities, total correlation and the Nishimori posterior-resampling
  identity.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Selection costs and posterior-replica information

## Source manuscripts and claim

- [Memory and precision in noiseless Gaussian regression](../papers/P-000473.md): selected passages extracted.
- [Posterior replicas and conditional information in Gaussian regression](../papers/P-000474.md): selected passages extracted.

The following companions are inventoried but have no extraction in this batch:

- [Localization costs and information growth for exact Gaussian observations](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Localization-costs-and-information-growth-for-exact-Gaussian-observations-September-27-2026)
- [Projection moments, positive cap domination, and Riesz estimates on the sphere](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Projection-moments-positive-cap-domination-and-Riesz-estimates-on-the-sphere-September-27-2026)
- [Replacing Gaussian observations in memory-constrained inference](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Replacing-Gaussian-observations-in-memory-constrained-inference-September-27-2026)
- [Subsphere methods for memory-sample lower bounds in noiseless Gaussian regression](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Subsphere-methods-for-memory-sample-lower-bounds-in-noiseless-Gaussian-regression-September-27-2026)

The family claims memory-sample and precision lower bounds for exact Gaussian observations.

## Extracted instruments

- [MI-000704: Pay only a root-of-count cost when selecting on one data domain](../instruments/MI-000704.md)
- [MI-000705: Bound message information by the correlation lost under projection](../instruments/MI-000705.md)

## Dependencies and antecedents

Holder inequalities, relative-entropy chain rules, coordinatewise data processing and posterior resampling.

Classical selection inequalities, total correlation and the Nishimori posterior-resampling identity.

## Review and formalization scope

Read the complete common-domain selection proof, replica-information proof, posterior-coupling explanation and entropy-test discussion. Two of six manuscripts receive extractions; four companion approaches remain inventory-only. Projection density estimates and streaming iteration are not certified.

Read the complete scope and both named Comparators. They specify finite-state noiseless Gaussian regression, fixed-quadratic and subquadratic memory targets, exact equal-label measures and several block-information comparisons. The other six listed Comparators were not inspected. Inspected theorem targets contain sorry; no separate solution or Lean build was checked.

Selection uses one reference measure and one common domain. Replica signals must have matching joint laws with the message; equal signal marginals alone are insufficient, and side randomness is independent.

[Batch record](../../batches/B075/README.md)

---
id: openai-math-224
record_type: family
title: Signed histories and calibration through a common observable
source_family: '224'
source_collection: openai/math
batch_id: B079
subject: Probability and statistical mechanics
source_paper_ids:
- P-000494
instrument_ids:
- MI-000734
- MI-000735
headline: The family claims Cardy limits, pivotal amplitudes and quenched near-critical universality for
  Voronoi percolation.
central_instrument: Expand exact finite color histories, then determine a comparison amplitude through
  a shared normalized first coefficient.
novelty_assessment: Known finite mechanisms are credited separately from source headline claims. Exhaustive
  novelty is not established.
formalization_summary: No scope document is supplied in the inventory. No Lean verification is claimed.
statement_faithfulness: Time labels and tied times are retained. Calibration assumes local replacement,
  fixed-scale convergence and uniform integrability; it does not supply those inputs.
dependencies: Product expansion, Poisson factorial moments, signed-kernel estimates, cutoff control and
  compactness.
antecedents: Classical product-measure perturbation and normalization by a response observable.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Signed histories and calibration through a common observable

## Source manuscripts and claim

- [From critical crossings to quenched near-critical universality in Voronoi percolation](../papers/P-000494.md): selected passages extracted.

The following companions are inventoried but have no extraction in this batch:

- [A Pivotal Amplitude for Voronoi Percolation from Cardy's Formula](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/A-Pivotal-Amplitude-for-Voronoi-Percolation-from-Cardys-Formula-October-5-2026)
- [Cardy’s formula for critical Poisson–Voronoi percolation](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Cardys-formula-for-critical-Poisson-Voronoi-percolation-September-23-2026)

The family claims Cardy limits, pivotal amplitudes and quenched near-critical universality for Voronoi percolation.

## Extracted instruments

- [MI-000734: Expand coupled time histories as a zero-mass signed perturbation](../instruments/MI-000734.md)
- [MI-000735: Fix a microscopic amplitude by one normalized macroscopic coefficient](../instruments/MI-000735.md)

## Dependencies and antecedents

Product expansion, Poisson factorial moments, signed-kernel estimates, cutoff control and compactness.

Classical product-measure perturbation and normalization by a response observable.

## Review and formalization scope

Read the full exact-history construction and common-calibration proof. Two companions are inventory-only; the crossing, replacement and uniform-integrability inputs are not certified.

No scope document is supplied in the inventory. No Lean verification is claimed.

Time labels and tied times are retained. Calibration assumes local replacement, fixed-scale convergence and uniform integrability; it does not supply those inputs.

[Batch record](../../batches/B079/README.md)

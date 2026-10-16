---
id: openai-math-227
record_type: family
title: Likelihood action and posterior entropy contraction
source_family: '227'
source_collection: openai/math
batch_id: B079
subject: Probability and statistical mechanics
source_paper_ids:
- P-000495
instrument_ids:
- MI-000736
- MI-000737
headline: The family claims high-temperature mixing, critical autocorrelation universality and low-temperature
  barriers for SK dynamics.
central_instrument: Use a square-root likelihood to control accumulated intensity changes; use concavity
  of two-point conductance to average posterior entropy production.
novelty_assessment: Known finite mechanisms are credited separately from source headline claims. Exhaustive
  novelty is not established.
formalization_summary: SKHighTemperature targets a high-probability Poincare bound for Gaussian zero-field
  SK at each beta in (0,1), with the corresponding 1/n discrete gap. The scope lists further restricted
  dynamics results; this inspected target does not state critical quench universality. Full scope and
  named Comparator read; other linked Comparators were not inspected. The target contains sorry; no separate
  solution or Lean build was checked.
statement_faithfulness: The point-process reference filtration includes initial information but no newly
  revealed future. Posterior contraction uses a test fixed before the observation.
dependencies: Likelihood supermartingales, localization, entropy tensorization and concavity of ab/(a+b).
antecedents: Classical point-process change of measure and product-measure entropy tensorization.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Likelihood action and posterior entropy contraction

## Source manuscripts and claim

- [Universality of critical quench autocorrelations in the Sherrington–Kirkpatrick model](../papers/P-000495.md): selected passages extracted.

The following companions are inventoried but have no extraction in this batch:

- [Functional universality of critical SK autocorrelations](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Functional-universality-of-critical-SK-autocorrelations-October-5-2026)
- [A spectral gap throughout the high-temperature Sherrington–Kirkpatrick phase](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/A-spectral-gap-throughout-the-high-temperature-Sherrington-Kirkpatrick-phase-September-24-2026)
- [Cutoff throughout the high-temperature Sherrington–Kirkpatrick phase](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Cutoff-throughout-the-high-temperature-Sherrington-Kirkpatrick-phase-September-24-2026)
- [Critical slowing down in the Sherrington–Kirkpatrick model](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Critical-slowing-down-in-the-Sherrington-Kirkpatrick-model-September-24-2026)
- [Stretched-exponential barriers for typical SK initial states](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Stretched-exponential-barriers-for-typical-SK-initial-states-September-24-2026)
- [A typical-start upper bound for low-temperature SK Glauber dynamics](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/A-typical-start-upper-bound-for-low-temperature-SK-Glauber-dynamics-September-24-2026)
- [Critical mixing in the Sherrington–Kirkpatrick model](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Critical-mixing-in-the-Sherrington-Kirkpatrick-model-September-25-2026)

The family claims high-temperature mixing, critical autocorrelation universality and low-temperature barriers for SK dynamics.

## Extracted instruments

- [MI-000736: Control integrated intensity distortion by the square-root likelihood](../instruments/MI-000736.md)
- [MI-000737: Average posterior entropy production through a concave two-point conductance](../instruments/MI-000737.md)

## Dependencies and antecedents

Likelihood supermartingales, localization, entropy tensorization and concavity of ab/(a+b).

Classical point-process change of measure and product-measure entropy tensorization.

## Review and formalization scope

Read the full likelihood/intensity proof and product-posterior entropy proof. Seven companions are inventory-only. Only the generic likelihood inequality and field-free posterior bound are extracted.

SKHighTemperature targets a high-probability Poincare bound for Gaussian zero-field SK at each beta in (0,1), with the corresponding 1/n discrete gap. The scope lists further restricted dynamics results; this inspected target does not state critical quench universality. Full scope and named Comparator read; other linked Comparators were not inspected. The target contains sorry; no separate solution or Lean build was checked.

The point-process reference filtration includes initial information but no newly revealed future. Posterior contraction uses a test fixed before the observation.

[Batch record](../../batches/B079/README.md)

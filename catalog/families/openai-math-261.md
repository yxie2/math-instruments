---
id: openai-math-261
record_type: family
title: Adaptive randomness and own-site spectral averaging
source_family: '261'
source_collection: openai/math
batch_id: B081
subject: Mathematical physics
source_paper_ids:
- P-000503
instrument_ids:
- MI-000752
- MI-000753
headline: The family claims continuous spectrum at weak disorder in higher dimensions and localization
  in two dimensions.
central_instrument: Retain all observed trial information when reusing an adaptive random environment;
  average a spectral measure over an independent diagonal variable.
novelty_assessment: Classical ingredients are credited; novelty of the source assembly is not established.
formalization_summary: The scope and full PlanarAndersonSpectrum Comparator were read. Its target is the
  almost-sure spectral set [-4-h,4+h] of the planar uniform-potential model, not pure point spectrum or
  the selected higher-dimensional absolutely continuous claim. The target contains sorry; no separate
  solution or Lean build was checked.
statement_faithfulness: Rollback may undo a numerical state but must not erase observed answers. Spectral
  averaging requires the diagonal variable to be independent of the cavity operator.
dependencies: Conditional product measures, stopping-time decomposition, Schur complements, Poisson kernels
  and measure regularity.
antecedents: Classical deferred decisions and rank-one spectral averaging.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Adaptive randomness and own-site spectral averaging

## Source manuscripts and claim

- [Absolutely Continuous Spectrum for Weak-Disorder Anderson Models in Dimensions at Least Three](../papers/P-000503.md): selected passages extracted.

The following companions are inventoried but have no extraction in this batch:

- [Pure-Point Spectrum for the Two-Dimensional Anderson Model at Every Positive Disorder](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Pure-Point-Spectrum-for-the-Two-Dimensional-Anderson-Model-at-Every-Positive-Disorder-September-23-2026)

The family claims continuous spectrum at weak disorder in higher dimensions and localization in two dimensions.

## Extracted instruments

- [MI-000752: Keep failed observations in the filtration when rolling back an adaptive computation](../instruments/MI-000752.md)
- [MI-000753: Average the diagonal spectral measure through an independent cavity](../instruments/MI-000753.md)

## Dependencies and antecedents

Conditional product measures, stopping-time decomposition, Schur complements, Poisson kernels and measure regularity.

Classical deferred decisions and rank-one spectral averaging.

## Review and formalization scope

Read the complete conditional-freshness lemma and the complete spectral-averaging lemma and proof. One companion is inventory-only. Neither spectral-type headline is certified.

The scope and full PlanarAndersonSpectrum Comparator were read. Its target is the almost-sure spectral set [-4-h,4+h] of the planar uniform-potential model, not pure point spectrum or the selected higher-dimensional absolutely continuous claim. The target contains sorry; no separate solution or Lean build was checked.

Rollback may undo a numerical state but must not erase observed answers. Spectral averaging requires the diagonal variable to be independent of the cavity operator.

[Batch record](../../batches/B081/README.md)

---
id: openai-math-073
record_type: family
title: Multiply local fiber bounds and compare positive collision energies
source_family: '073'
source_collection: openai/math
batch_id: B032
subject: Real and complex analysis
source_paper_ids:
- P-000199
instrument_ids:
- MI-000360
- MI-000361
headline: 'The source claims the Falconer distance conjecture in all dimensions: compact sets of Hausdorff
  dimension greater than half the ambient dimension determine a positive-measure distance set.'
central_instrument: Pruning low-density parent cells allows local fiber bounds to multiply. Positive binning
  controls shifted collisions and converts them into bounded-frequency Fourier energy even for singular
  measures.
novelty_assessment: Density pruning, discrete Cauchy-Schwarz and a squared-sinc Fourier majorant are classical
  tools. The extraction records their exact roles and hypotheses without certifying the source distance
  theorem.
formalization_summary: Read PlanarFalconer.lean and FalconerAllDimensions.lean. They state the compact-set
  positive-distance-measure claims in dimension two and every dimension at least two. Both targets contain
  sorry; no Lean build was performed.
statement_faithfulness: The density lower bound is imposed on the pre-deletion pair set, not the final
  pruned set. The radial version needs pin-source separation, whereas the full-line-width version needs
  only bounded distances above and removal of diagonal pairs. Collision measures must be positive.
dependencies: Dyadic cubes, a geometric containment of hit children in one local fiber test, a union bound,
  Cauchy-Schwarz and the Fourier transform of squared sinc.
antecedents: Classical density pruning, positive-measure collision estimates and Fourier majorants; no
  first-priority claim.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Multiply local fiber bounds and compare positive collision energies

## Source manuscript and claim

[The Falconer distance conjecture in all dimensions](../papers/P-000199.md), by OpenAI, September 23, 2026.

The source claims the Falconer distance conjecture in all dimensions: compact sets of Hausdorff dimension greater than half the ambient dimension determine a positive-measure distance set.

## Extracted instruments

- [MI-000360: Prune using the original density before multiplying local fiber bounds](../instruments/MI-000360.md)
- [MI-000361: Control shifted collisions and Fourier energy by positive bin masses](../instruments/MI-000361.md)

## Dependencies and antecedents

Dyadic cubes, a geometric containment of hit children in one local fiber test, a union bound, Cauchy-Schwarz and the Fourier transform of squared sinc.

Classical density pruning, positive-measure collision estimates and Fourier majorants; no first-priority claim. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the complete density-pruning/multiplication proof and positive-measure binning proof. The angular gain, thin-tube upgrade, profile recursion and final distance argument were not audited.

Read PlanarFalconer.lean and FalconerAllDimensions.lean. They state the compact-set positive-distance-measure claims in dimension two and every dimension at least two. Both targets contain sorry; no Lean build was performed.

The density lower bound is imposed on the pre-deletion pair set, not the final pruned set. The radial version needs pin-source separation, whereas the full-line-width version needs only bounded distances above and removal of diagonal pairs. Collision measures must be positive.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/073.md) · [Batch record](../../batches/B032/README.md)

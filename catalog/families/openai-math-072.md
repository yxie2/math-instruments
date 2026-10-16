---
id: openai-math-072
record_type: family
title: Conformal Sobolev pullback and a harmonic equality obstruction
source_family: '072'
source_collection: openai/math
batch_id: B064
subject: Real and complex analysis
source_paper_ids:
- P-000385
- P-000386
instrument_ids:
- MI-000616
- MI-000617
headline: The sources claim Brennan derivative integrability and a strict inverse-first-power integral-means
  bound.
central_instrument: Derivative integrability supplies explicit Sobolev pullback exponents. A rectangular
  harmonic barrier rules out the pointwise equality case of a critical Jacobian.
novelty_assessment: The pullback exponent relation is explicitly due to Goldshtein-Ukhlov. The harmonic
  barrier is classical; its use against the source equality case is recorded without certifying the transport
  law.
formalization_summary: Brennan targets inverse-square means with arbitrary positive exponent loss, spectrum
  value one and the two open derivative-integrability intervals. BrennanSharp states the four Koebe endpoint
  divergences. StrictMeans states one positive, unspecified uniform improvement below exponent 1/4 for
  all normalized univalent disk maps and the bounded-spectrum consequence. None of these targets is a
  proof of the extracted corollary by itself. Both available scope documents and all four distinct linked
  Comparators in this batch were read in full. Target theorems have sorry proof bodies. No separate solution
  or Lean build was checked.
statement_faithfulness: Derivative integrability is an assumption in the extracted pullback implication.
  The harmonic obstruction excludes an identically zero Jacobian, not isolated zeros or near-equality
  without compactness.
dependencies: Conformal chain rule, area change of variables, Holder, harmonic logarithms and the minimum
  principle.
antecedents: Goldshtein-Ukhlov composition theorem and classical harmonic barriers.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Conformal Sobolev pullback and a harmonic equality obstruction

## Source manuscripts and claim

- [Brennan's conjecture and sharp inverse-square integral means](../papers/P-000385.md): selected passages extracted.
- [A strict inverse-first-power bound for univalent functions](../papers/P-000386.md): selected passages extracted.

The sources claim Brennan derivative integrability and a strict inverse-first-power integral-means bound.

## Extracted instruments

- [MI-000616: Translate conformal derivative integrability into a Sobolev pullback bound](../instruments/MI-000616.md)
- [MI-000617: Exclude a critical Jacobian equality by a growing harmonic barrier](../instruments/MI-000617.md)

## Dependencies and antecedents

Conformal chain rule, area change of variables, Holder, harmonic logarithms and the minimum principle.

Goldshtein-Ukhlov composition theorem and classical harmonic barriers.

## Review and formalization scope

Read the full pullback corollary and its primary antecedent, the full harmonic equality-barrier proof, and definitions of the logarithmic derivative and critical Jacobian. Weighted laws, critical-point pairings and global integral-means bounds remain unaudited.

Brennan targets inverse-square means with arbitrary positive exponent loss, spectrum value one and the two open derivative-integrability intervals. BrennanSharp states the four Koebe endpoint divergences. StrictMeans states one positive, unspecified uniform improvement below exponent 1/4 for all normalized univalent disk maps and the bounded-spectrum consequence. None of these targets is a proof of the extracted corollary by itself. Both available scope documents and all four distinct linked Comparators in this batch were read in full. Target theorems have sorry proof bodies. No separate solution or Lean build was checked.

Derivative integrability is an assumption in the extracted pullback implication. The harmonic obstruction excludes an identically zero Jacobian, not isolated zeros or near-equality without compactness.

[Batch record](../../batches/B064/README.md)

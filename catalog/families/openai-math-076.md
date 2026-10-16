---
id: openai-math-076
record_type: family
title: Uniform quadratic waves and defect-controlled sign rounding
source_family: '076'
source_collection: openai/math
batch_id: B071
subject: Real and complex analysis
source_paper_ids:
- P-000445
- P-000446
instrument_ids:
- MI-000676
- MI-000677
headline: The family claims ultraflat real Littlewood polynomials, nearly minimal maxima with positive
  minima, and an earlier all-length maximal-modulus result.
central_instrument: A Fourier-side Gaussian identity controls stationary-phase errors uniformly in the
  frequency. Mass-preserving dyadic rounding converts near-sign coefficients to real signs.
novelty_assessment: Established mechanisms are distinguished from source-specific combinations. Targeted
  primary comparisons are recorded; exhaustive priority is not established and no source headline is certified.
formalization_summary: Read the scope and both complete Comparators. One target asserts all sufficiently
  large lengths admit real signs with maximum at most (1+eta)sqrt(N). The other chooses one all-length
  signing family with normalized modulus converging to one in every fixed finite positive Lp exponent.
  These are existential targets, not effective algorithms or the later uniform lower-modulus conclusion.
  Both target bodies contain sorry. No separate solution or Lean build was checked.
statement_faithfulness: Oscillatory amplitudes are smooth and compactly supported. Rounding is existential
  with an absolute constant and depends on total defect, including the zero-defect endpoint.
dependencies: Fourier inversion, Gaussian regularization, partial coloring, dyadic grids and Cauchy derivative
  estimates.
antecedents: Classical stationary phase and Spencer/Lovett-Meka discrepancy theory.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Uniform quadratic waves and defect-controlled sign rounding

## Source manuscripts and claim

- [Ultraflat real Littlewood polynomials](../papers/P-000445.md): selected passages extracted.
- [Nearly minimal maxima and positive minima of Littlewood polynomials](../papers/P-000446.md): selected passages extracted.

The following companions are inventoried but have no extraction in this batch:

- [Asymptotically minimal maxima of real Littlewood polynomials](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Asymptotically-minimal-maxima-of-real-Littlewood-polynomials-September-23-2026)

The family claims ultraflat real Littlewood polynomials, nearly minimal maxima with positive minima, and an earlier all-length maximal-modulus result.

## Extracted instruments

- [MI-000676: Make the quadratic stationary-phase error uniform in the frequency](../instruments/MI-000676.md)
- [MI-000677: Round near-sign Fourier coefficients with a total-defect budget](../instruments/MI-000677.md)

## Dependencies and antecedents

Fourier inversion, Gaussian regularization, partial coloring, dyadic grids and Cauchy derivative estimates.

Classical stationary phase and Spencer/Lovett-Meka discrepancy theory.

## Review and formalization scope

Read all oscillation estimates in the first manuscript and the full matrix-discrepancy and defect-rounding proofs in the second. Two of three manuscripts receive extractions; the earlier manuscript remains inventory-only. No ultraflatness or global polynomial construction is certified.

Read the scope and both complete Comparators. One target asserts all sufficiently large lengths admit real signs with maximum at most (1+eta)sqrt(N). The other chooses one all-length signing family with normalized modulus converging to one in every fixed finite positive Lp exponent. These are existential targets, not effective algorithms or the later uniform lower-modulus conclusion. Both target bodies contain sorry. No separate solution or Lean build was checked.

Oscillatory amplitudes are smooth and compactly supported. Rounding is existential with an absolute constant and depends on total defect, including the zero-defect endpoint.

[Batch record](../../batches/B071/README.md)

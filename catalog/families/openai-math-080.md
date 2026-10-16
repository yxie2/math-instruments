---
id: openai-math-080
record_type: family
title: Gaussian approximation from local mass and scale-stable packet envelopes
source_family: 080
source_collection: openai/math
batch_id: B064
subject: Real and complex analysis
source_paper_ids:
- P-000389
- P-000390
instrument_ids:
- MI-000620
- MI-000621
headline: The sources claim endpoint pointwise Schrodinger convergence in the plane and higher dimensions.
central_instrument: Uniform mass on unit balls suffices for Gaussian approximation without global integrability.
  An anisotropic lattice split preserves the envelope exponent across packet scales.
novelty_assessment: Both use classical approximate-identity and polynomial-decay convolution arguments.
  Their exact source normalizations and exceptional-set interfaces are recorded without certifying endpoint
  convergence.
formalization_summary: No Lean scope document or linked Comparator is supplied for this family in the
  pinned inventory. No formal solution was built.
statement_faithfulness: The Gaussian hypothesis is a uniform local L1 bound, not just local integrability.
  Packet envelopes use spatial ratio r and time ratio r², so the volume exponent is k+2.
dependencies: Annular coverings, Lebesgue differentiation, radial integration by parts, anisotropic lattice
  sums and positive weights.
antecedents: Classical heat approximate identities and almost-diagonal polynomial-decay estimates.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Gaussian approximation from local mass and scale-stable packet envelopes

## Source manuscripts and claim

- [Endpoint convergence for the planar Schrodinger equation](../papers/P-000389.md): selected passages extracted.
- [Endpoint pointwise convergence for the Schrodinger equation in higher dimensions](../papers/P-000390.md): selected passages extracted.

The sources claim endpoint pointwise Schrodinger convergence in the plane and higher dimensions.

## Extracted instruments

- [MI-000620: Approximate uniformly locally integrable envelopes by Gaussians](../instruments/MI-000620.md)
- [MI-000621: Preserve a polynomial envelope exponent through anisotropic sampling](../instruments/MI-000621.md)

## Dependencies and antecedents

Annular coverings, Lebesgue differentiation, radial integration by parts, anisotropic lattice sums and positive weights.

Classical heat approximate identities and almost-diagonal polynomial-decay estimates.

## Review and formalization scope

Read the complete Gaussian-envelope lemma and the subsequent conditional uniform-in-time comparison, and the complete envelope-convolution proof with native packet coordinates. Maximal, fractal, frame and endpoint estimates remain unaudited.

No Lean scope document or linked Comparator is supplied for this family in the pinned inventory. No formal solution was built.

The Gaussian hypothesis is a uniform local L1 bound, not just local integrability. Packet envelopes use spatial ratio r and time ratio r², so the volume exponent is k+2.

[Batch record](../../batches/B064/README.md)

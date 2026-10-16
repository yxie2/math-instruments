---
id: openai-math-090
record_type: family
title: Density-only Fourier bounds and differentiated Poisson normalization
source_family: 090
source_collection: openai/math
batch_id: B072
subject: Convex and metric geometry
source_paper_ids:
- P-000451
- P-000452
instrument_ids:
- MI-000682
- MI-000683
headline: The family claims triangular-lattice universal optimality, sharp planar Fourier packing certificates
  and Coulomb/logarithmic-energy consequences.
central_instrument: A smooth cutoff forces Fourier mass near zero using only centered density. Differentiating
  a lattice dilation identity fixes normalization from one shell slope.
novelty_assessment: Selected mechanisms are compared with established antecedents where directly checked.
  No exhaustive novelty determination or certification of a source headline is claimed.
formalization_summary: Read the scope and complete AtomicGaussian and PlanarPacking Comparators. They
  target sharp radial Schwartz Gaussian minorants, including the explicit atomic construction for alpha>=1,
  and a normalized sharp planar packing Fourier certificate. The two other listed Comparators, TriangularEnergy
  and TriangularGaussian, were not inspected in this batch. No finite-certificate program from these manuscripts
  was run. Each inspected Comparator has a sorry target body. No separate solution or Lean build was checked.
statement_faithfulness: The energy comparison assumes a nonnegative Fourier transform of a supplied Schwartz
  minorant. The normalization assumes an exact radial Fourier pair and exact node jets; the global certificates
  are not checked.
dependencies: Fourier inversion, Plancherel, positive Fourier transforms, Poisson summation, Schwartz
  convergence and shell multiplicities.
antecedents: Cohn-Kumar Euclidean linear-programming energy bounds and classical differentiated Poisson
  summation.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Density-only Fourier bounds and differentiated Poisson normalization

## Source manuscripts and claim

- [An atomic certificate for triangular-lattice universal optimality](../papers/P-000451.md): selected passages extracted.
- [A sharp Fourier certificate for planar circle packing](../papers/P-000452.md): selected passages extracted.

The following companions are inventoried but have no extraction in this batch:

- [Universal optimality of the triangular lattice](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Universal-optimality-of-the-triangular-lattice-September-23-2026)
- [Triangular minimality for planar Coulomb renormalized energy](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Triangular-minimality-for-planar-Coulomb-renormalized-energy-September-23-2026)

The family claims triangular-lattice universal optimality, sharp planar Fourier packing certificates and Coulomb/logarithmic-energy consequences.

## Extracted instruments

- [MI-000682: Extract a Fourier energy lower bound from centered density alone](../instruments/MI-000682.md)
- [MI-000683: Recover a Fourier certificate normalization from a first-shell slope](../instruments/MI-000683.md)

## Dependencies and antecedents

Fourier inversion, Plancherel, positive Fourier transforms, Poisson summation, Schwartz convergence and shell multiplicities.

Cohn-Kumar Euclidean linear-programming energy bounds and classical differentiated Poisson summation.

## Review and formalization scope

Read the full low-frequency and density-only LP proofs in the atomic manuscript, and the full origin-normalization and second-dilation proofs in the packing manuscript. Two of four manuscripts receive extractions; the earlier universal-optimality and Coulomb manuscripts remain inventory-only. Atomic interpolation, signs and computational certificates are not certified.

Read the scope and complete AtomicGaussian and PlanarPacking Comparators. They target sharp radial Schwartz Gaussian minorants, including the explicit atomic construction for alpha>=1, and a normalized sharp planar packing Fourier certificate. The two other listed Comparators, TriangularEnergy and TriangularGaussian, were not inspected in this batch. No finite-certificate program from these manuscripts was run. Each inspected Comparator has a sorry target body. No separate solution or Lean build was checked.

The energy comparison assumes a nonnegative Fourier transform of a supplied Schwartz minorant. The normalization assumes an exact radial Fourier pair and exact node jets; the global certificates are not checked.

[Batch record](../../batches/B072/README.md)

---
id: openai-math-215
record_type: family
title: Conditional spin dimension reduction and massive kernels
source_family: '215'
source_collection: openai/math
batch_id: B077
subject: Probability and statistical mechanics
source_paper_ids:
- P-000487
- P-000488
instrument_ids:
- MI-000722
- MI-000723
headline: The family claims exponential decay for O(n), canonical O(3) continuum limits, a particle pole
  and exact O(4) mass asymptotics.
central_instrument: Conditioning transverse coordinates reduces the spin dimension with bounded effective
  couplings; a positive spectral representation gives decay without assuming an atom.
novelty_assessment: Selected mechanisms are separated from source headline claims and credited to known
  antecedents where established. Exhaustive priority is not established.
formalization_summary: ClassicalON targets finite-volume exponential correlation decay uniformly over
  square-lattice subgraphs and couplings in [0,beta], for each n>=3. It does not state a continuum limit
  or the O(4) spectral assertions. The complete scope and named Comparators were read. Inspected theorem
  targets contain sorry; no separate solution or Lean build was checked.
statement_faithfulness: Spin reduction uses the free finite-volume sphere law. Massive-kernel decay assumes
  the spectral representation, a positive mass gap and polynomial spectral growth; it does not prove a
  particle pole.
dependencies: Gaussian polar coordinates, conditional Gibbs densities, positive mass-shell measures and
  exponential damping.
antecedents: Conditional O(N) projections and the classical Kallen-Lehmann representation.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Conditional spin dimension reduction and massive kernels

## Source manuscripts and claim

- [Exponential decay in two-dimensional classical O(n) models](../papers/P-000487.md): selected passages extracted.
- [An Isolated Particle Pole for the Two-Dimensional O(3) Spin Field](../papers/P-000488.md): selected passages extracted.

The following companions are inventoried but have no extraction in this batch:

- [The canonical massive continuum limit of the two-dimensional O(3) model](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-canonical-massive-continuum-limit-of-the-two-dimensional-O3-model-October-4-2026)
- [Exact mass asymptotics for the two-dimensional O(4) lattice model](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Exact-mass-asymptotics-for-the-two-dimensional-O4-lattice-model-October-5-2026)
- [Sharp mass bounds for the two-dimensional O(4) model](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Sharp-mass-bounds-for-the-two-dimensional-O4-model-September-23-2026)

The family claims exponential decay for O(n), canonical O(3) continuum limits, a particle pole and exact O(4) mass asymptotics.

## Extracted instruments

- [MI-000722: Condition transverse spin coordinates to inherit a lower-dimensional bound](../instruments/MI-000722.md)
- [MI-000723: Obtain positive off-diagonal decay without presuming a spectral atom](../instruments/MI-000723.md)

## Dependencies and antecedents

Gaussian polar coordinates, conditional Gibbs densities, positive mass-shell measures and exponential damping.

Conditional O(N) projections and the classical Kallen-Lehmann representation.

## Review and formalization scope

Read the full three-component conditional-law proof and its correlation-transfer application, plus the full massive Euclidean kernel proof. Two of five manuscripts receive extractions; three companions are inventory-only. The O(3) gap, continuum construction and isolated-pole arguments are not certified.

ClassicalON targets finite-volume exponential correlation decay uniformly over square-lattice subgraphs and couplings in [0,beta], for each n>=3. It does not state a continuum limit or the O(4) spectral assertions. The complete scope and named Comparators were read. Inspected theorem targets contain sorry; no separate solution or Lean build was checked.

Spin reduction uses the free finite-volume sphere law. Massive-kernel decay assumes the spectral representation, a positive mass gap and polynomial spectral growth; it does not prove a particle pole.

[Batch record](../../batches/B077/README.md)

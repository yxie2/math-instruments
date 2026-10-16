---
id: openai-math-254
record_type: family
title: Positive Cartan data, centralizer characters and finite intersection witnesses
source_family: '254'
source_collection: openai/math
batch_id: B061
subject: Group theory
source_paper_ids:
- P-000359
- P-000360
- P-000361
instrument_ids:
- MI-000590
- MI-000591
- MI-000592
headline: The sources claim the Artin K(pi,1) conjecture, a 116-generator obstruction to geometric CAT(0)
  actions, and general parabolic intersections.
central_instrument: A weighted quadratic-form identity separates positive and null Cartan data. Stable
  lengths yield a character on a whole centralizer. Rank descent reduces arbitrary intersections to finitely
  many witnesses.
novelty_assessment: These selected mechanisms have classical linear-algebra, CAT(0) and parabolic-closure
  antecedents. The finite witness argument is already implicit in earlier rank-descent proofs. No source
  headline is certified.
formalization_summary: HarmonicArtin defines the lifted spherical-cell preorder and its nerve realization,
  including finite empty and disconnected diagrams. ArtinCAT0 gives an explicit 116-generator matrix with
  labels 2,3,infinity and rules out geometric actions on any nonempty proper CAT(0) space. ArtinParabolicIntersections
  states pairwise and arbitrary intersections, a rank-sized witness, closure, and irreducible infinite-label
  dynamical consequences. All three available scope documents and all seven linked Comparators in this
  batch were read in full. Headline targets have sorry proof bodies; supporting definitions sometimes
  have explicit proofs. No separate solution or Lean project was built.
statement_faithfulness: Cartan off-diagonal weights are nonnegative and the null/positive dichotomy assumes
  connectedness and a strictly positive vector. Centralizer elements need not commute with one another.
  Parabolic closure is conditional here on the pairwise intersection input.
dependencies: Perron-Frobenius, Neumann series, weighted squares, CAT(0) comparison, stable lengths, Busemann
  limits and finite integer rank descent.
antecedents: Classical M-matrix and ground-state transform arguments; Rodenhausen parallelogram law; Moeller-Paris-Varghese
  rank and closure propositions.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Positive Cartan data, centralizer characters and finite intersection witnesses

## Source manuscripts and claim

- [Harmonic heights and the Artin K(pi,1) conjecture](../papers/P-000359.md): selected passages extracted.
- [An Artin group with no geometric CAT(0) action](../papers/P-000360.md): selected passages extracted.
- [Parabolic intersections in Artin groups](../papers/P-000361.md): selected passages extracted.

The sources claim the Artin K(pi,1) conjecture, a 116-generator obstruction to geometric CAT(0) actions, and general parabolic intersections.

## Extracted instruments

- [MI-000590: Separate positive and null Cartan data by weighted squares](../instruments/MI-000590.md)
- [MI-000591: Turn stable-length polarization into a character on a centralizer](../instruments/MI-000591.md)
- [MI-000592: Bound the number of witnesses in an arbitrary intersection by rank descent](../instruments/MI-000592.md)

## Dependencies and antecedents

Perron-Frobenius, Neumann series, weighted squares, CAT(0) comparison, stable lengths, Busemann limits and finite integer rank descent.

Classical M-matrix and ground-state transform arguments; Rodenhausen parallelogram law; Moeller-Paris-Varghese rank and closure propositions.

## Review and formalization scope

Read the complete positive/null Cartan proof and all stable-length/centralizer proofs. Read the full finite-intersection descent proof and its introductory formulation. Global categorical filtrations and the pairwise parabolic intersection theorem remain unaudited.

HarmonicArtin defines the lifted spherical-cell preorder and its nerve realization, including finite empty and disconnected diagrams. ArtinCAT0 gives an explicit 116-generator matrix with labels 2,3,infinity and rules out geometric actions on any nonempty proper CAT(0) space. ArtinParabolicIntersections states pairwise and arbitrary intersections, a rank-sized witness, closure, and irreducible infinite-label dynamical consequences. All three available scope documents and all seven linked Comparators in this batch were read in full. Headline targets have sorry proof bodies; supporting definitions sometimes have explicit proofs. No separate solution or Lean project was built.

Cartan off-diagonal weights are nonnegative and the null/positive dichotomy assumes connectedness and a strictly positive vector. Centralizer elements need not commute with one another. Parabolic closure is conditional here on the pairwise intersection input.

[Batch record](../../batches/B061/README.md)

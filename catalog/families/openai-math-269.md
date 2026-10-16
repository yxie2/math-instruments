---
id: openai-math-269
record_type: family
title: Fermionic normal ordering and polynomial zero modes
source_family: '269'
source_collection: openai/math
batch_id: B082
subject: Mathematical physics
source_paper_ids:
- P-000506
instrument_ids:
- MI-000758
- MI-000759
headline: The family claims a uniform spherical Laughlin gap and stability under scalar disorder.
central_instrument: Determine normal-ordered coefficients in low particle sectors; identify a zero-mode
  line through pairwise polynomial divisibility.
novelty_assessment: Classical mechanisms are credited. Novelty of the source-specific assembly is not
  established.
formalization_summary: The scope and full LaughlinFock and LaughlinGap Comparators were read. They target
  unperturbed gap inequalities, not disorder stability. Other linked Comparators were not inspected. The
  inspected targets contain sorry; no separate solution or Lean build was checked.
statement_faithfulness: The pair interaction is the lift of an orthogonal projection. Wedges of increasing
  orthonormal vectors have norm one. Kernel uniqueness does not imply a gap uniform in particle number.
dependencies: Canonical anticommutation relations, positivity of fermionic lifts, pair-spin decomposition
  and unique factorization.
antecedents: Classical Wick ordering and the established Laughlin parent-Hamiltonian zero-mode characterization.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Fermionic normal ordering and polynomial zero modes

## Source manuscripts and claim

- [A Fock-space inequality and the Laughlin spectral gap](../papers/P-000506.md): selected passages extracted.

The following companions are inventoried but have no extraction in this batch:

- [Uniform Stability of the Spherical Laughlin Gap](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Uniform-Stability-of-the-Spherical-Laughlin-Gap-October-5-2026)

The family claims a uniform spherical Laughlin gap and stability under scalar disorder.

## Extracted instruments

- [MI-000758: Recover the square of a pair interaction from its low-particle restrictions](../instruments/MI-000758.md)
- [MI-000759: Turn pair exclusions into a unique polynomial zero-mode line](../instruments/MI-000759.md)

## Dependencies and antecedents

Canonical anticommutation relations, positivity of fermionic lifts, pair-spin decomposition and unique factorization.

Classical Wick ordering and the established Laughlin parent-Hamiltonian zero-mode characterization.

## Review and formalization scope

Read the complete normal-ordering and Laughlin kernel proofs in the Fock-space companion. The stability lead manuscript is inventory-only. The finite rational certificate and its asymptotic transfer are not certified.

The scope and full LaughlinFock and LaughlinGap Comparators were read. They target unperturbed gap inequalities, not disorder stability. Other linked Comparators were not inspected. The inspected targets contain sorry; no separate solution or Lean build was checked.

The pair interaction is the lift of an orthogonal projection. Wedges of increasing orthonormal vectors have norm one. Kernel uniqueness does not imply a gap uniform in particle number.

[Batch record](../../batches/B082/README.md)

---
id: openai-math-256
record_type: family
title: Weighted spectral cycles and a unitary fixed-plane incidence argument
source_family: '256'
source_collection: openai/math
batch_id: B061
subject: Group theory
source_paper_ids:
- P-000362
- P-000363
instrument_ids:
- MI-000593
- MI-000594
headline: The sources claim solvability of nonsingular systems over arbitrary groups and coefficient injectivity
  for unimodular one-relator quotients.
central_instrument: Rotational symmetry computes the phase trace of a weighted block cycle. A fixed-plane
  incidence manifold matches dimensions and provides a unique regular fiber for a mod-two degree argument.
novelty_assessment: Spectral cyclic symmetry is elementary, and compact-unitary degree methods originate
  in Gerstenhaber-Rothaus. The exact fixed-plane incidence lemma was not identified in the inspected antecedent;
  its independent priority remains unresolved.
formalization_summary: The only linked target Kervaire is coefficient-group injectivity for a relator
  of exponent sum plus or minus one in A free-product Z. It does not state the systems companion theorem
  or all formulations of Kervaire normal generation. All three available scope documents and all seven
  linked Comparators in this batch were read in full. Headline targets have sorry proof bodies; supporting
  definitions sometimes have explicit proofs. No separate solution or Lean project was built.
statement_faithfulness: The phase is the fractional angle in [0,1), with value zero at identity. The coefficient
  trace is normalized while the block-matrix trace is unnormalized. The degree lemma needs sign sum exactly
  plus or minus one and asserts existence for each fixed P, not a continuous choice.
dependencies: Finite tracial von Neumann algebras, bounded Borel functional calculus, cyclic conjugacy,
  unitary homotopy, Grassmannians and mod-two degree.
antecedents: Gerstenhaber-Rothaus compact-unitary degree strategy; Klyachko-Thom coefficient-removing
  homotopies.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Weighted spectral cycles and a unitary fixed-plane incidence argument

## Source manuscripts and claim

- [Nonsingular systems of equations over arbitrary groups](../papers/P-000362.md): selected passages extracted.
- [The Kervaire theorem for groups](../papers/P-000363.md): selected passages extracted.

The sources claim solvability of nonsingular systems over arbitrary groups and coefficient injectivity for unimodular one-relator quotients.

## Extracted instruments

- [MI-000593: Compute a weighted cycle phase from its monodromy](../instruments/MI-000593.md)
- [MI-000594: Force a fixed k-plane by a unitary incidence manifold of degree one](../instruments/MI-000594.md)

## Dependencies and antecedents

Finite tracial von Neumann algebras, bounded Borel functional calculus, cyclic conjugacy, unitary homotopy, Grassmannians and mod-two degree.

Gerstenhaber-Rothaus compact-unitary degree strategy; Klyachko-Thom coefficient-removing homotopies.

## Review and formalization scope

Read the entire spectral-phase section in the systems paper and the complete fixed-plane incidence proof in the Kervaire companion. The planar operator assembly and full arbitrary-group injectivity arguments are not certified.

The only linked target Kervaire is coefficient-group injectivity for a relator of exponent sum plus or minus one in A free-product Z. It does not state the systems companion theorem or all formulations of Kervaire normal generation. All three available scope documents and all seven linked Comparators in this batch were read in full. Headline targets have sorry proof bodies; supporting definitions sometimes have explicit proofs. No separate solution or Lean project was built.

The phase is the fractional angle in [0,1), with value zero at identity. The coefficient trace is normalized while the block-matrix trace is unnormalized. The degree lemma needs sign sum exactly plus or minus one and asserts existence for each fixed P, not a continuous choice.

[Batch record](../../batches/B061/README.md)

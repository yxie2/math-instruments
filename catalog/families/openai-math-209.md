---
id: openai-math-209
record_type: family
title: Testing strict functoriality and designing a residue-degree barrier
source_family: '209'
source_collection: openai/math
batch_id: B057
subject: Algebra
source_paper_ids:
- P-000327
- P-000328
instrument_ids:
- MI-000558
- MI-000559
headline: The manuscripts claim integral mixed-characteristic counterexamples to Gersten injectivity,
  including a degree-three example.
central_instrument: A two-by-two chain-map square isolates failure of a proposed strict functor. An Artin-Schreier
  special fiber and an Eisenstein divisor separate residue degrees away from one point from the norm at
  that point.
novelty_assessment: Naturality tests, Artin-Schreier orbits, regular local hypersurfaces and Eisenstein
  norms are classical. The explicit matrix obstruction is checked against the cited preprint version.
  The specific geometric data are verified algebraically; the K-theoretic nonzero classes are not certified.
formalization_summary: Only the selected manuscript arguments are reviewed. No scope document or Comparator
  is listed for this family in the pinned inventory. No Lean solution was built.
statement_faithfulness: Failure of the specified strict functor does not by itself disprove its intended
  vanishing theorem. The local ring is regular but ramified and not smooth over the DVR. No order or rational
  nonvanishing of a K-class is inferred.
dependencies: Two-term complexes, strict commuting diagrams, split exact sequences, Artin-Schreier extensions,
  properness, regular local rings, Eisenstein polynomials and field norms.
antecedents: Mochizuki arXiv:1503.07966v8, Conventions 11, Definition 12 and Lemma 13(III); classical
  finite-field and local-algebra constructions.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Testing strict functoriality and designing a residue-degree barrier

## Source manuscripts and claim

- [An integral counterexample to Gersten's conjecture](../papers/P-000327.md): selected passages extracted.
- [An integral degree-three Gersten counterexample](../papers/P-000328.md): selected passages extracted.

The manuscripts claim integral mixed-characteristic counterexamples to Gersten injectivity, including a degree-three example.

## Extracted instruments

- [MI-000558: Test mixed commuting squares before asserting a block projection is a functor](../instruments/MI-000558.md)
- [MI-000559: Combine an Artin-Schreier residue barrier with a distinguished uniformizer norm](../instruments/MI-000559.md)

## Dependencies and antecedents

Two-term complexes, strict commuting diagrams, split exact sequences, Artin-Schreier extensions, properness, regular local rings, Eisenstein polynomials and field norms.

Mochizuki arXiv:1503.07966v8, Conventions 11, Definition 12 and Lemma 13(III); classical finite-field and local-algebra constructions.

## Review and formalization scope

Read the complete strict-naturality counterexample and compared it with the actual cited version, pages 9-11. Read the full mixed-characteristic model and divisor proof. The higher K-theory comparisons, integral lifts and global detection arguments remain unaudited.

Only the selected manuscript arguments are reviewed. No scope document or Comparator is listed for this family in the pinned inventory. No Lean solution was built.

Failure of the specified strict functor does not by itself disprove its intended vanishing theorem. The local ring is regular but ramified and not smooth over the DVR. No order or rational nonvanishing of a K-class is inferred.

[Batch record](../../batches/B057/README.md)

---
id: openai-math-288
record_type: family
title: Rectangular derivations through triangular metrics and cyclic columns
source_family: '288'
source_collection: openai/math
batch_id: B018
subject: Operator algebras
source_paper_ids:
- P-000143
instrument_ids:
- MI-000246
- MI-000247
headline: The source claims similarity to a star homomorphism for every bounded unital homomorphism from
  a unital complex C*-algebra to operators on an arbitrary Hilbert space, together with universal amplified
  commutator and hyperreflexivity bounds.
central_instrument: Triangular metric blocks recover a rectangular implementer; cyclic-domain column factorization
  and quotient lifts turn a column bound into a completely bounded estimate.
novelty_assessment: The metric argument is explicitly adapted from Ozawa and Paulsen, and the row estimate
  is attributed to Dickson and Christensen. The useful extracted detail is the rectangular, nonfaithful-domain
  bookkeeping. The global similarity claim was not audited.
formalization_summary: 'The scope document, KadisonSimilarity.lean and UniformCommutator.lean were read
  at their definitions and targets. They quantify over arbitrary Hilbert spaces and use one constant for
  all finite amplifications. Comparator statements were inspected, not proof builds: no Lean solution
  was built or kernel-checked. The auxiliary cards are not all separate formalization targets.'
statement_faithfulness: Cyclicity belongs to the domain representation alone. The derivation need not
  annihilate its kernel; identities must be applied to actual lifts in the original algebra. Complete
  boundedness is an assumption in the first card and a conclusion under cyclicity in the second.
dependencies: Paulsen similarity, standard-form vector realization, matrix Kaplansky density, C*-quotient
  matrix norms and uniform row/column bounds.
antecedents: Ozawa, An invitation to the similarity problems, Lemma 1.2; Paulsen, Completely bounded homomorphisms
  of operator algebras; Dickson, A Kadison Kastler row metric and intermediate subalgebras, Lemma 2.9;
  Haagerup standard-form theory.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Rectangular derivations through triangular metrics and cyclic columns

## Source manuscript and claim

[Kadison's similarity theorem through uniform derivation estimates](../papers/P-000143.md), by OpenAI, September 23, 2026.

The source claims similarity to a star homomorphism for every bounded unital homomorphism from a unital complex C*-algebra to operators on an arbitrary Hilbert space, together with universal amplified commutator and hyperreflexivity bounds.

## Extracted instruments

- [MI-000246: A positive triangular metric gives an explicit rectangular derivation implementer](../instruments/MI-000246.md)
- [MI-000247: Cyclic column factorization upgrades derivation bounds without descending through a kernel](../instruments/MI-000247.md)

## Dependencies and antecedents

Paulsen similarity, standard-form vector realization, matrix Kaplansky density, C*-quotient matrix norms and uniform row/column bounds.

Ozawa, An invitation to the similarity problems, Lemma 1.2; Paulsen, Completely bounded homomorphisms of operator algebras; Dickson, A Kadison Kastler row metric and intermediate subalgebras, Lemma 2.9; Haagerup standard-form theory. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the complete preliminary derivation arguments. The free-product corner, finite-factor propagation and global similarity argument were not audited.

The scope document, KadisonSimilarity.lean and UniformCommutator.lean were read at their definitions and targets. They quantify over arbitrary Hilbert spaces and use one constant for all finite amplifications. Comparator statements were inspected, not proof builds: no Lean solution was built or kernel-checked. The auxiliary cards are not all separate formalization targets.

Cyclicity belongs to the domain representation alone. The derivation need not annihilate its kernel; identities must be applied to actual lifts in the original algebra. Complete boundedness is an assumption in the first card and a conclusion under cyclicity in the second.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/288.md) · [Batch record](../../batches/B018/README.md)

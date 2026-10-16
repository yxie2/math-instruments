---
id: openai-math-145
record_type: family
title: Entropy cancellation and parameter-independent operator squares
source_family: '145'
source_collection: openai/math
batch_id: B014
subject: Dynamical systems and ergodic theory
source_paper_ids:
- P-000128
instrument_ids:
- MI-000215
- MI-000216
headline: The source claims that ordinary mixing of an invertible probability-preserving transformation
  implies mixing of all finite orders as successive gaps tend to infinity.
central_instrument: A dissociated exponential estimate combines with a small word-entropy bound without
  independence of the observables. Triple independence and two operator rectangle identities make positive
  squares constant and permit polar normalization.
novelty_assessment: Dissociated exponential bounds, entropy typical-set arguments and polar decomposition
  are established. The selected combinations and their exact dependence assumptions are candidate reusable
  interfaces, not a certification of the multiple-mixing claim.
formalization_summary: Rokhlin.lean formulates the implication for measurable probability spaces and invertible
  measure-preserving transformations, with all positive successive gaps tending to infinity. Scope text
  and Comparator statements were read. No Lean solution was built or kernel-checked; the extracted auxiliary
  lemmas are not separately certified targets.
statement_faithfulness: The cancellation lemma allows arbitrary dependence between the word and characters.
  The operator lemma instead requires product law for each triple and full essential spans for the families
  and their adjoints.
dependencies: Dissociation, Fourier orthogonality, exponential Markov bounds, word entropy, Fubini, separability,
  positive square roots and polar uniqueness.
antecedents: Green, Structure theory of set addition, Proposition 17 gives an earlier dissociated exponential
  estimate. Spectral and polar functional calculus are classical.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Entropy cancellation and parameter-independent operator squares

## Source manuscript and claim

[Rokhlin's multiple-mixing problem for one transformation](../papers/P-000128.md), by OpenAI, September 23, 2026.

The source claims that ordinary mixing of an invertible probability-preserving transformation implies mixing of all finite orders as successive gaps tend to infinity.

## Extracted instruments

- [MI-000215: Sublinear word entropy forces cancellation against dissociated characters under arbitrary coupling](../instruments/MI-000215.md)
- [MI-000216: Triple independence fixes positive squares and preserves an operator rectangle under polar normalization](../instruments/MI-000216.md)

## Dependencies and antecedents

Dissociation, Fourier orthogonality, exponential Markov bounds, word entropy, Fubini, separability, positive square roots and polar uniqueness.

Green, Structure theory of set addition, Proposition 17 gives an earlier dissociated exponential estimate. Spectral and polar functional calculus are classical. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the full entropy cancellation and fixed-squares proofs, including the preceding rectangle setup. The array structure, subsequent cancellation and global mixing implication were not audited.

Rokhlin.lean formulates the implication for measurable probability spaces and invertible measure-preserving transformations, with all positive successive gaps tending to infinity. Scope text and Comparator statements were read. No Lean solution was built or kernel-checked; the extracted auxiliary lemmas are not separately certified targets.

The cancellation lemma allows arbitrary dependence between the word and characters. The operator lemma instead requires product law for each triple and full essential spans for the families and their adjoints.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/145.md) · [Batch record](../../batches/B014/README.md)

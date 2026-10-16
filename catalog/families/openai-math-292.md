---
id: openai-math-292
record_type: family
title: Density operators, varying matrix dimensions and finite predecessor obstructions
source_family: '292'
source_collection: openai/math
batch_id: B018
subject: Operator algebras
source_paper_ids:
- P-000144
instrument_ids:
- MI-000248
- MI-000249
- MI-000250
headline: The source claims an explicit separable unital full group C*-algebra with no unital embedding
  into a norm ultrapower of any nonzero unital nuclear C*-algebra, for any free ultrafilter on the natural
  numbers.
central_instrument: Reduced density operators remove arbitrary tensor-factor unitaries, norm ultraproducts
  retain spectral minima in varying dimensions, and a finite predecessor relation forces periodic irreducible
  representations.
novelty_assessment: Powers-Stormer and property-(T) representation methods are established. The varying-dimension
  and finite-predecessor formulations are candidate reusable interfaces in this source. No exhaustive
  priority or global nonembedding proof certification was performed.
formalization_summary: 'The scope document and NuclearUltrapower.lean target were inspected, including
  the full-group universal property, nuclear tensor-norm convention and Cuntz corollary. Comparator statements
  were inspected, not proof builds: no Lean solution was built or kernel-checked. The auxiliary cards
  are not all separate formalization targets.'
statement_faithfulness: First-factor unitaries need not satisfy group relations. The weak-mixing spectral
  bound requires no finite-dimensional subrepresentations. Varying representations have no common dimension
  bound. The finite-cycle conclusion needs representation pullback structure, not merely a finite directed
  graph.
dependencies: Property-(T) spectral gaps, Powers-Stormer, partial traces, norm ultraproducts, finite-dimensional
  representation inclusions and invariant subspaces.
antecedents: Powers-Stormer 1970, Lemma 4.1; Bekka 1990 on amenable unitary representations; Valette 1997,
  Proposition 2; Wassermann property-(T) quotient methods.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Density operators, varying matrix dimensions and finite predecessor obstructions

## Source manuscript and claim

[An explicit obstruction to nuclear norm-ultrapower embeddings](../papers/P-000144.md), by OpenAI, September 23, 2026.

The source claims an explicit separable unital full group C*-algebra with no unital embedding into a norm ultrapower of any nonzero unital nuclear C*-algebra, for any free ultrafilter on the natural numbers.

## Extracted instruments

- [MI-000248: Reduced density operators remove arbitrary unitaries from a tensor spectral bound](../instruments/MI-000248.md)
- [MI-000249: A norm ultraproduct preserves spectral minima with unbounded representation dimensions](../instruments/MI-000249.md)
- [MI-000250: Finite predecessor families force every irreducible class to be periodic](../instruments/MI-000250.md)

## Dependencies and antecedents

Property-(T) spectral gaps, Powers-Stormer, partial traces, norm ultraproducts, finite-dimensional representation inclusions and invariant subspaces.

Powers-Stormer 1970, Lemma 4.1; Bekka 1990 on amenable unitary representations; Valette 1997, Proposition 2; Wassermann property-(T) quotient methods. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the square-root trace proof, weak-mixing estimate, varying-dimension gap and finite predecessor cycle in full. Nuclear finiteness, uniform predecessor construction and the complete nonembedding proof were not audited.

The scope document and NuclearUltrapower.lean target were inspected, including the full-group universal property, nuclear tensor-norm convention and Cuntz corollary. Comparator statements were inspected, not proof builds: no Lean solution was built or kernel-checked. The auxiliary cards are not all separate formalization targets.

First-factor unitaries need not satisfy group relations. The weak-mixing spectral bound requires no finite-dimensional subrepresentations. Varying representations have no common dimension bound. The finite-cycle conclusion needs representation pullback structure, not merely a finite directed graph.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/292.md) · [Batch record](../../batches/B018/README.md)

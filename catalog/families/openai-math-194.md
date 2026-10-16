---
id: openai-math-194
record_type: family
title: Normalized length limits and bundles with prescribed cohomological roots
source_family: '194'
source_collection: openai/math
batch_id: B019
subject: Algebra
source_paper_ids:
- P-000147
instrument_ids:
- MI-000255
- MI-000256
headline: The source claims e(R)<=e(S) for every flat local homomorphism of nonzero Noetherian local rings,
  without restrictions on dimensions, residue fields or characteristics.
central_instrument: A supremum-over-finite-submodules length theory controls noninjective limits, while
  a product-of-projective-lines construction places cohomology in a prescribed degree over every base
  ring.
novelty_assessment: The normalized length formalism is established work of Faltings and successors. The
  root-bundle construction is explicitly Eisenbud-Schreyer. The extracted source detail is their use over
  auxiliary non-Noetherian rings with uniform annihilator and base-change bookkeeping; the full multiplicity
  comparison was not audited.
formalization_summary: Read the scope document and DuttaDomain.lean definitions and target. They cover
  the complete positive-characteristic domain Dutta comparison for short finite-free complexes, including
  convergence and finite-length Frobenius homology; the full flat-local theorem is outside that target.
  These are target statements; no Lean solution was built or kernel-checked. The auxiliary cards are not
  separately certified formal results.
statement_faithfulness: All modules in each limit argument must belong to the same length category, with
  a common annihilating power. Zero normalized length does not imply the module is zero. Root-bundle cohomology
  is free over an arbitrary base ring; its extension to the exceptional divisor is a separate source comparison.
dependencies: Additive normalized length, finite generation, directed colimits, finite flat maps, cohomology
  of line bundles on P1 and tensor products of split complexes.
antecedents: Faltings normalized length; Cai-Lee-Ma-Schwede-Tucker, Section 2.2; Eisenbud-Schreyer, Betti
  numbers of graded modules and cohomology of vector bundles, Theorem 6.1.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Normalized length limits and bundles with prescribed cohomological roots

## Source manuscript and claim

[Lech's multiplicity conjecture](../papers/P-000147.md), by OpenAI, September 23, 2026.

The source claims e(R)<=e(S) for every flat local homomorphism of nonzero Noetherian local rings, without restrictions on dimensions, residue fields or characteristics.

## Extracted instruments

- [MI-000255: Vanishing normalized lengths pass through noninjective directed limits](../instruments/MI-000255.md)
- [MI-000256: A finite flat product map realizes prescribed cohomological roots over every base ring](../instruments/MI-000256.md)

## Dependencies and antecedents

Additive normalized length, finite generation, directed colimits, finite flat maps, cohomology of line bundles on P1 and tensor products of split complexes.

Faltings normalized length; Cai-Lee-Ma-Schwede-Tucker, Section 2.2; Eisenbud-Schreyer, Betti numbers of graded modules and cohomology of vector bundles, Theorem 6.1. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the normalized-length definitions and limit lemma, plus the complete integral root-bundle construction. The uniform complex estimate, characteristic reductions, perfectoid inputs and global Lech theorem were not audited.

Read the scope document and DuttaDomain.lean definitions and target. They cover the complete positive-characteristic domain Dutta comparison for short finite-free complexes, including convergence and finite-length Frobenius homology; the full flat-local theorem is outside that target. These are target statements; no Lean solution was built or kernel-checked. The auxiliary cards are not separately certified formal results.

All modules in each limit argument must belong to the same length category, with a common annihilating power. Zero normalized length does not imply the module is zero. Root-bundle cohomology is free over an arbitrary base ring; its extension to the exceptional divisor is a separate source comparison.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/194.md) · [Batch record](../../batches/B019/README.md)

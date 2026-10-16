---
id: openai-math-245
record_type: family
title: Finite syntactic support and mixed-order fixed points in type systems
source_family: '245'
source_collection: openai/math
batch_id: B021
subject: Mathematical logic
source_paper_ids:
- P-000158
instrument_ids:
- MI-000278
- MI-000279
headline: The source claims that system-wide weak normalization implies system-wide strong normalization
  for every pure type system, allowing arbitrary sorts, nonfunctional axioms/rules and reduction inside
  annotations.
central_instrument: A finite derivation and its conversion witnesses retain any hypothetical failure in
  a finite specification. Balanced signed dependencies turn contravariant and covariant candidate equations
  into one monotone operator on a mixed-order complete lattice.
novelty_assessment: Finite-support reduction, reducibility candidates and Tarski fixed points are established
  methods. The source applies them with explicit annotation and variance bookkeeping. The observation-space
  and diagonal arguments handling the remaining components were not audited.
formalization_summary: Read TypeSystemNormalization.lean, including full annotated syntax, substitution,
  reduction, legality, weak and strong normalization and the unrestricted target. These are target statements
  with sorry placeholders; no Lean solution was built or kernel-checked.
statement_faithfulness: Weak normalization is assumed for every legal expression, not for a single term.
  Conversion witness chains contribute to finite support. Parity counts negative dependency edges, and
  the signed fixed-point construction applies only when every closed walk in the component has even parity.
dependencies: Finite typing derivations, capture-avoiding substitution, correctness of types, raw beta
  syntax, complete candidate lattices, signed dependency graphs and Tarski monotonicity.
antecedents: Standard pure-type-system metatheory and reducibility candidates; Tarski, A lattice-theoretical
  fixpoint theorem and its applications (1955), Theorem 1.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Finite syntactic support and mixed-order fixed points in type systems

## Source manuscript and claim

[Weak and strong normalization in pure type systems](../papers/P-000158.md), by OpenAI, September 25, 2026.

The source claims that system-wide weak normalization implies system-wide strong normalization for every pure type system, allowing arbitrary sorts, nonfunctional axioms/rules and reduction inside annotations.

## Extracted instruments

- [MI-000278: Finite derivations retain a system-wide normalization counterexample in a finite specification](../instruments/MI-000278.md)
- [MI-000279: Balanced signed dependencies turn mixed-variance equations into a Tarski operator](../instruments/MI-000279.md)

## Dependencies and antecedents

Finite typing derivations, capture-avoiding substitution, correctness of types, raw beta syntax, complete candidate lattices, signed dependency graphs and Tarski monotonicity.

Standard pure-type-system metatheory and reducibility candidates; Tarski, A lattice-theoretical fixpoint theorem and its applications (1955), Theorem 1. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the full finite-restriction proof, candidate lattice lemma and signed-component proof. The general observation interpretation, typed channels, relational diagonal construction and final exclusion theorem were not audited.

Read TypeSystemNormalization.lean, including full annotated syntax, substitution, reduction, legality, weak and strong normalization and the unrestricted target. These are target statements with sorry placeholders; no Lean solution was built or kernel-checked.

Weak normalization is assumed for every legal expression, not for a single term. Conversion witness chains contribute to finite support. Parity counts negative dependency edges, and the signed fixed-point construction applies only when every closed walk in the component has even parity.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/245.md) · [Batch record](../../batches/B021/README.md)

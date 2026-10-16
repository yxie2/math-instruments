---
id: openai-math-198
record_type: family
title: Shifted central selection and derived square-zero extensions
source_family: '198'
source_collection: openai/math
batch_id: B019
subject: Algebra
source_paper_ids:
- P-000148
instrument_ids:
- MI-000257
- MI-000258
headline: The source claims a fixed finite-dimensional complex algebra with finite-dimensional modules
  of finite projective dimension at least 2m-2 for every positive m, and an auxiliary extreme left/right
  finitistic-dimension asymmetry.
central_instrument: Iterating a twisted central idempotent reads successive sign constraints. A bar decomposition
  of a split square-zero extension turns genuinely derived tensor survival into projective-dimension information.
novelty_assessment: Central character projections and bar decompositions are established. The square-zero
  projective-dimension formulas are explicitly prior work of Minamoto-Yamaura. The source-specific finite-presentation,
  lifting and simulation that would combine them into a fixed counterexample were not audited.
formalization_summary: Read the scope document, LittleFinitistic.lean and FinitisticAsymmetry.lean targets.
  They assert a fixed complex algebra, unbounded finite module projective dimensions, and left/right asymmetry
  including injective generation. These are target statements; no Lean solution was built or kernel-checked.
  The auxiliary cards are not separately certified formal results.
statement_faithfulness: The selection algebra is finitely presented, not asserted finite-dimensional at
  that stage. Twisting need not preserve a finite quotient kernel. Tensor powers in the extension formula
  are derived; ordinary tensors may miss higher Tor.
dependencies: Central idempotents, scalar restriction, character projections, bar resolutions, derived
  tensors, minimal projective resolutions and Nakayama.
antecedents: Classical finite-group character projectors and twisted modules; Minamoto-Yamaura, Homological
  dimension formulas for trivial extension algebras, Corollary 4.11, Lemma 4.13 and Theorem 4.17.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Shifted central selection and derived square-zero extensions

## Source manuscript and claim

[An algebra of infinite little finitistic dimension](../papers/P-000148.md), by OpenAI, September 23, 2026.

The source claims a fixed finite-dimensional complex algebra with finite-dimensional modules of finite projective dimension at least 2m-2 for every positive m, and an auxiliary extreme left/right finitistic-dimension asymmetry.

## Extracted instruments

- [MI-000257: Twisted central-idempotent selection reads a prescribed extinction time](../instruments/MI-000257.md)
- [MI-000258: Derived tensor survival appears as separate bar summands in a square-zero extension](../instruments/MI-000258.md)

## Dependencies and antecedents

Central idempotents, scalar restriction, character projections, bar resolutions, derived tensors, minimal projective resolutions and Nakayama.

Classical finite-group character projectors and twisted modules; Minamoto-Yamaura, Homological dimension formulas for trivial extension algebras, Corollary 4.11, Lemma 4.13 and Theorem 4.17. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the selection functor and final character-module argument, the full bar decomposition and projective-dimension corollary. The fixed finitely presented group, localization, bimodule rectification and ordinary simulation were not audited.

Read the scope document, LittleFinitistic.lean and FinitisticAsymmetry.lean targets. They assert a fixed complex algebra, unbounded finite module projective dimensions, and left/right asymmetry including injective generation. These are target statements; no Lean solution was built or kernel-checked. The auxiliary cards are not separately certified formal results.

The selection algebra is finitely presented, not asserted finite-dimensional at that stage. Twisting need not preserve a finite quotient kernel. Tensor powers in the extension formula are derived; ordinary tensors may miss higher Tor.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/198.md) · [Batch record](../../batches/B019/README.md)

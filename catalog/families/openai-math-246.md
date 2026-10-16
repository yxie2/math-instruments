---
id: openai-math-246
record_type: family
title: Crossing duality and energy-controlled probability flows
source_family: '246'
source_collection: openai/math
batch_id: B030
subject: Group theory
source_paper_ids:
- P-000191
instrument_ids:
- MI-000344
- MI-000345
headline: The source claims that a word-hyperbolic group with two-sphere boundary admits a proper cocompact
  isometric action on hyperbolic three-space with finite kernel.
central_instrument: A minimum-norm convex combination of crossing vectors supplies dual weights. A tree
  energy budget then bounds the average number of unfavorable ancestors by Jensen inequality.
novelty_assessment: The convex-hull modulus formula is explicitly established in Albin and Poggi-Corradini,
  Theorem 5.1. The flow lemma is a reusable application of Jensen inequality; neither is a certification
  of the source Cannon claim.
formalization_summary: Read CannonGeometricAction.lean. It defines thin Cayley triangles, a ray-quotient
  boundary and a proper cocompact action on the upper-half-space model, with finite kernel. The inspected
  Comparator contains a sorry target; no Lean build or kernel verification was performed.
statement_faithfulness: Crossing intersection yields an upper bound for the dual energy, not an automatic
  equality of two arbitrary crossing moduli. The flow conclusion provides infinitely many good levels
  rather than a uniform bound at every level.
dependencies: Finite-dimensional convex optimization, a planar crossing/blocker input, conservation of
  tree probability and Jensen inequality.
antecedents: Albin and Poggi-Corradini, Minimal subfamilies and the probabilistic interpretation for modulus
  on graphs, Theorem 5.1; classical blocking duality and Jensen inequality.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Crossing duality and energy-controlled probability flows

## Source manuscript and claim

[A Modulus Proof of Cannon’s Conjecture](../papers/P-000191.md), by OpenAI, September 23, 2026.

The source claims that a word-hyperbolic group with two-sphere boundary admits a proper cocompact isometric action on hyperbolic three-space with finite kernel.

## Extracted instruments

- [MI-000344: Turn a minimum-norm mixture of crossings into dual weights](../instruments/MI-000344.md)
- [MI-000345: Use a tree energy budget to bound the frequency of unfavorable ancestors](../instruments/MI-000345.md)

## Dependencies and antecedents

Finite-dimensional convex optimization, a planar crossing/blocker input, conservation of tree probability and Jensen inequality.

Albin and Poggi-Corradini, Minimal subfamilies and the probabilistic interpretation for modulus on graphs, Theorem 5.1; classical blocking duality and Jensen inequality. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the complete crossing/blocker and dual-weight proofs and the tree good-level proof. The scalar limit, magnification comparisons, capacity construction and global uniformization argument were not audited.

Read CannonGeometricAction.lean. It defines thin Cayley triangles, a ray-quotient boundary and a proper cocompact action on the upper-half-space model, with finite kernel. The inspected Comparator contains a sorry target; no Lean build or kernel verification was performed.

Crossing intersection yields an upper bound for the dual energy, not an automatic equality of two arbitrary crossing moduli. The flow conclusion provides infinitely many good levels rather than a uniform bound at every level.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/246.md) · [Batch record](../../batches/B030/README.md)

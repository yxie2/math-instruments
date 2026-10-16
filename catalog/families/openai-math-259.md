---
id: openai-math-259
record_type: family
title: Small complete sets and low-cost graphings from markers
source_family: '259'
source_collection: openai/math
batch_id: B031
subject: Group theory
source_paper_ids:
- P-000197
instrument_ids:
- MI-000356
- MI-000357
headline: The source claims a group with free probability-measure-preserving actions of different costs,
  hence without fixed price.
central_instrument: Random finite-partition markers meet every infinite equivalence class after adding
  the unhit remainder. A commuting generator can be restricted to a small complete marker set without
  losing generated edges.
novelty_assessment: Small complete sections and product graphing compression are established measured-equivalence
  methods. The commuting-marker construction is explicit in Gaboriau 2000, Proposition VI.23. The extracted
  height propagation supplies a concrete cost upper bound, not the distinct-cost lower bound.
formalization_summary: The pinned release inventory lists no linked formalization scope or Comparator
  for this family. No Lean project was inspected or built.
statement_faithfulness: Exceptional unhit orbits are included even when they have measure zero. Finite
  equivalence classes contribute the reciprocal-class-size integral. A cost upper bound alone cannot establish
  failure of fixed price.
dependencies: Countable Borel relation enumeration, measure-preserving partial isomorphisms, separating
  partitions, independent marking, dominated convergence and commuting generator paths.
antecedents: Gaboriau 2000, Proposition VI.23, for commuting-generator graphings; classical complete-section
  and finite-class counting arguments.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Small complete sets and low-cost graphings from markers

## Source manuscript and claim

[A group without fixed price](../papers/P-000197.md), by OpenAI, October 5, 2026.

The source claims a group with free probability-measure-preserving actions of different costs, hence without fixed price.

## Extracted instruments

- [MI-000356: Build a complete Borel set at the finite-class mass threshold](../instruments/MI-000356.md)
- [MI-000357: Generate commuting edges from sparse markers and propagate a height window](../instruments/MI-000357.md)

## Dependencies and antecedents

Countable Borel relation enumeration, measure-preserving partial isomorphisms, separating partitions, independent marking, dominated convergence and commuting generator paths.

Gaboriau 2000, Proposition VI.23, for commuting-generator graphings; classical complete-section and finite-class counting arguments. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the full finite-class counting and small complete-set proofs, Bernoulli marker proof and height-extension upper-bound proof. Compression, deployment, finite-model transfer and cost lower bounds were not audited.

The pinned release inventory lists no linked formalization scope or Comparator for this family. No Lean project was inspected or built.

Exceptional unhit orbits are included even when they have measure zero. Finite equivalence classes contribute the reciprocal-class-size integral. A cost upper bound alone cannot establish failure of fixed price.

[Batch record](../../batches/B031/README.md)

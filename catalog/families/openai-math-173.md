---
id: openai-math-173
record_type: family
title: Rank-charged pruning and transitive blowup deficits
source_family: '173'
source_collection: openai/math
batch_id: B012
subject: Combinatorics
source_paper_ids:
- P-000119
instrument_ids:
- MI-000196
- MI-000197
headline: The source claims that every nonempty finite oriented graph has a vertex with at least as many
  strict second out-neighbors as first out-neighbors.
central_instrument: An augmented bipartite cover charges conflict deletion to a second corner set through
  a commuting matrix square. Transitive blocks amplify a strict subset deficit while costing at most one
  unit per original vertex.
novelty_assessment: Matching-cover duality and generic rank are classical. The candidate packages are
  the corner-specific pruning charge and the exact blowup accounting; the complete second-neighborhood
  theorem is not certified here.
formalization_summary: SeymourSecondNeighborhood.lean states the finite nonempty loopless asymmetric relation
  theorem with strict second neighbors excluding the initial vertex and its first neighbors. Scope documents
  and Comparator declarations were compared. No Lean solution was built or kernel-checked; the extracted
  auxiliary results are not separately certified targets.
statement_faithfulness: The pruning lemma permits an arbitrary relation. The blowup uses raw image iteration
  F squared, which must not be confused with the strict second neighborhood in the headline statement.
dependencies: Bipartite matching and covers; generic matrices with fixed zero patterns; a maximum-rank
  kernel observation; rank of a composition; transitive tournaments and integer subset deficits.
antecedents: Edmonds identifies matching size with generic matrix rank. Seacrest supplies an earlier minimal-counterexample
  subset reduction. These do not by themselves establish the selected pruning or blowup conclusions.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Rank-charged pruning and transitive blowup deficits

## Source manuscript and claim

[A proof of Seymour’s second-neighborhood conjecture](../papers/P-000119.md), by OpenAI, September 23, 2026.

The source claims that every nonempty finite oriented graph has a vertex with at least as many strict second out-neighbors as first out-neighbors.

## Extracted instruments

- [MI-000196: An augmented matching cover charges rectangular conflict pruning to corner sets](../instruments/MI-000196.md)
- [MI-000197: Transitive blowups amplify integer subset deficits with bounded block error](../instruments/MI-000197.md)

## Dependencies and antecedents

Bipartite matching and covers; generic matrices with fixed zero patterns; a maximum-rank kernel observation; rank of a composition; transitive tournaments and integer subset deficits.

Edmonds identifies matching size with generic matrix rank. Seacrest supplies an earlier minimal-counterexample subset reduction. These do not by themselves establish the selected pruning or blowup conclusions. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the full pruning proof and transitive-blowup argument. The preceding minimal-counterexample reduction and subsequent incompatibility argument were not completely audited.

SeymourSecondNeighborhood.lean states the finite nonempty loopless asymmetric relation theorem with strict second neighbors excluding the initial vertex and its first neighbors. Scope documents and Comparator declarations were compared. No Lean solution was built or kernel-checked; the extracted auxiliary results are not separately certified targets.

The pruning lemma permits an arbitrary relation. The blowup uses raw image iteration F squared, which must not be confused with the strict second neighborhood in the headline statement.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/173.md) · [Batch record](../../batches/B012/README.md)

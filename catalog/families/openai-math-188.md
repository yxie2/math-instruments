---
id: openai-math-188
record_type: family
title: Paired survival queries and occurrence-level independent unfolding
source_family: '188'
source_collection: openai/math
batch_id: B013
subject: Combinatorics
source_paper_ids:
- P-000123
instrument_ids:
- MI-000204
- MI-000205
headline: The source claims that uniform triangle removal from the complete graph leaves an edge count
  whose normalization by n^(3/2) converges in L2 to 1/(2 sqrt(2)), with corresponding probability and
  expectation convergence.
central_instrument: A chronological two-edge recursive query exactly represents finite survival. Fresh
  randomness per occurrence gives exact product equations, and an exposure-based coupling separates these
  auxiliary products from correlated finite survival.
novelty_assessment: Random-priority greedy packing, backward branching and decreasing-priority termination
  are established. The selected candidate refinement is the paired query and complete-list exposure bookkeeping.
  The sharp terminal constant is not certified by this extraction.
formalization_summary: TriangleRemoval.lean states the L2, probability and expectation conclusions for
  the complete-graph process, using its absorbing continuation to define the terminal law. Scope text
  and Comparator statements were compared. No Lean solution was built or kernel-checked; the auxiliary
  instruments are not separate certified targets.
statement_faithfulness: A triangle type has one priority in the finite process but fresh priorities at
  different occurrences in the unfolding. Pair survival is factored only in the latter. Collision events
  count every exposed candidate, including candidates never visited.
dependencies: Uniform random permutations; decreasing recursive thresholds; finite branching and factorial
  tails; independent occurrence trees; deferred decisions and coupling.
antecedents: Spencer studies random-priority packing and backward branching. Penrose and Sudbury construct
  graph adsorption processes using decreasing-time dependency paths.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Paired survival queries and occurrence-level independent unfolding

## Source manuscript and claim

[The sharp terminal leave in random triangle removal](../papers/P-000123.md), by OpenAI, September 25, 2026.

The source claims that uniform triangle removal from the complete graph leaves an edge count whose normalization by n^(3/2) converges in L2 to 1/(2 sqrt(2)), with corresponding probability and expectation convergence.

## Extracted instruments

- [MI-000204: A chronological paired query exactly represents survival in greedy triangle removal](../instruments/MI-000204.md)
- [MI-000205: Fresh occurrence randomness yields product equations with an explicit collision coupling](../instruments/MI-000205.md)

## Dependencies and antecedents

Uniform random permutations; decreasing recursive thresholds; finite branching and factorial tails; independent occurrence trees; deferred decisions and coupling.

Spencer studies random-priority packing and backward branching. Penrose and Sudbury construct graph adsorption processes using decreasing-time dependency paths. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the full exact-query and independent-unfolding section and the exposure coupling lemma. Prefix concentration, spectral stability, collision-witness summation and the terminal moment conclusion were not audited.

TriangleRemoval.lean states the L2, probability and expectation conclusions for the complete-graph process, using its absorbing continuation to define the terminal law. Scope text and Comparator statements were compared. No Lean solution was built or kernel-checked; the auxiliary instruments are not separate certified targets.

A triangle type has one priority in the finite process but fresh priorities at different occurrences in the unfolding. Pair survival is factored only in the latter. Collision events count every exposed candidate, including candidates never visited.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/188.md) · [Batch record](../../batches/B013/README.md)

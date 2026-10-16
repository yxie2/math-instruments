---
id: openai-math-128
record_type: family
title: Period-aware occurrence bounds and ordered layers in superstring graphs
source_family: '128'
source_collection: openai/math
batch_id: B010
subject: Theoretical computer science
source_paper_ids:
- P-000113
instrument_ids:
- MI-000184
- MI-000185
headline: The source claims a deterministic polynomial-time factor-two approximation for shortest common
  superstring over explicitly encoded finite alphabets.
central_instrument: Nearest-mismatch brackets create valid forced occurrence lower bounds. Closed walks
  on a substring graph can then be reorganized into ordered layers of primitive periodic texts without
  changing edge multiplicities.
novelty_assessment: The hierarchical substring graph and collapsing framework have prior sources. The
  selected candidate mechanisms are the multiplicity-aware periodic forcing rule and the ordered-layer
  representation. The complete approximation algorithm is not certified.
formalization_summary: Superstring.lean states existence of an explicitly bit-polynomial deterministic
  finite-stack-machine implementation, contiguous coverage of every input word and output symbol length
  at most twice unrestricted optimum. The scope documents and Comparator statements were compared; no
  Lean solution was built or kernel-checked. The auxiliary instruments are not separate certified Comparator
  results.
statement_faithfulness: The approximation factor concerns symbol length, while computation time is measured
  in the explicit bit encoding. The result is not stated as a factor-two guarantee for the usual greedy
  overlap algorithm. The base graph may be disconnected.
dependencies: Substring-closed vertex sets; nearest mismatch brackets; descending integer recursion; nonleast
  periods as well as primitive ones; balanced up/down multigraphs; cyclic window representations; monotone
  order statistics.
antecedents: Golovnev-Kulikov-Mihajlin introduced a hierarchical graph for bounded-length instances; Golovnev
  and coauthors developed the all-substrings collapsing framework. Periodic matching and sorting monotone
  coordinates are classical ingredients.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Period-aware occurrence bounds and ordered layers in superstring graphs

## Source manuscript and claim

[A Polynomial-Time 2-Approximation for Shortest Common Superstring](../papers/P-000113.md), by OpenAI, September 24, 2026.

The source claims a deterministic polynomial-time factor-two approximation for shortest common superstring over explicitly encoded finite alphabets.

## Extracted instruments

- [MI-000184: Nearest-mismatch brackets make periodic occurrence lower bounds sound](../instruments/MI-000184.md)
- [MI-000185: Sorting periodic windows preserves a closed-walk edge multiset](../instruments/MI-000185.md)

## Dependencies and antecedents

Substring-closed vertex sets; nearest mismatch brackets; descending integer recursion; nonleast periods as well as primitive ones; balanced up/down multigraphs; cyclic window representations; monotone order statistics.

Golovnev-Kulikov-Mihajlin introduced a hierarchical graph for bounded-length instances; Golovnev and coauthors developed the all-substrings collapsing framework. Periodic matching and sorting monotone coordinates are classical ingredients. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read all forced-count and ordered-layer arguments, including the two cases needed to justify periodic forcing. The later connection, processing, cycle-budget and algorithmic bit-complexity proofs were not audited.

Superstring.lean states existence of an explicitly bit-polynomial deterministic finite-stack-machine implementation, contiguous coverage of every input word and output symbol length at most twice unrestricted optimum. The scope documents and Comparator statements were compared; no Lean solution was built or kernel-checked. The auxiliary instruments are not separate certified Comparator results.

The approximation factor concerns symbol length, while computation time is measured in the explicit bit encoding. The result is not stated as a factor-two guarantee for the usual greedy overlap algorithm. The base graph may be disconnected.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/128.md) · [Batch record](../../batches/B010/README.md)

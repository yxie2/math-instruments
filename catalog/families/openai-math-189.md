---
id: openai-math-189
record_type: family
title: Clique path budgets and complete weighted-forest enumeration
source_family: '189'
source_collection: openai/math
batch_id: B013
subject: Combinatorics
source_paper_ids:
- P-000124
instrument_ids:
- MI-000206
- MI-000207
headline: The source claims R(C_m,K_n)=(m-1)(n-1)+1 for m>=n>=3 except (3,3), where the value is six.
central_instrument: Paths with clique endpoints turn cycle avoidance into a forbidden amount interval.
  Weighted path components have a canonical tuple encoding with a separate generating-function count.
novelty_assessment: Joining paths through a clique, lexicographic optimization and reversal-orbit counting
  are elementary established ideas. Their precise budget and enumeration interface is useful for reuse;
  the complete Ramsey proof is not certified.
formalization_summary: CycleCliqueRamsey.lean states the exact full parameter range and the separate value
  R(C3,K3)=6. Scope text and Comparator statements were compared. No Lean solution was built or kernel-checked;
  the auxiliary instruments are not separate certified targets.
statement_faithfulness: Amounts count internal vertices, not edges. The represented endpoint graph must
  be a linear forest with distinct edges. Empty component tuples encode singleton vertices; an empty outer
  list encodes no vertices.
dependencies: Simple paths with disjoint interiors; clique completion; lexicographic optimality; reversal
  classes of compositions; multiset generating functions.
antecedents: Keevash, Long and Skokan provide earlier cycle-complete Ramsey results. The extracted finite
  normalization and counting use standard graph isomorphism and composition principles.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Clique path budgets and complete weighted-forest enumeration

## Source manuscript and claim

[Cycle--clique Ramsey numbers](../papers/P-000124.md), by OpenAI, September 25, 2026.

The source claims R(C_m,K_n)=(m-1)(n-1)+1 for m>=n>=3 except (3,3), where the value is six.

## Extracted instruments

- [MI-000206: Clique-ended path systems turn a forbidden cycle length into an amount interval](../instruments/MI-000206.md)
- [MI-000207: Reversal-normalized compositions enumerate weighted linear forests without duplicates](../instruments/MI-000207.md)

## Dependencies and antecedents

Simple paths with disjoint interiors; clique completion; lexicographic optimality; reversal classes of compositions; multiset generating functions.

Keevash, Long and Skokan provide earlier cycle-complete Ramsey results. The extracted finite normalization and counting use standard graph isomorphism and composition principles. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the path-system closure, optimality and separation arguments, plus complete pattern coverage and count formulas. The large-clique argument, full finite deduction rules and supplied certificate implementations were not audited or rerun.

CycleCliqueRamsey.lean states the exact full parameter range and the separate value R(C3,K3)=6. Scope text and Comparator statements were compared. No Lean solution was built or kernel-checked; the auxiliary instruments are not separate certified targets.

Amounts count internal vertices, not edges. The represented endpoint graph must be a linear forest with distinct edges. Empty component tuples encode singleton vertices; an empty outer list encodes no vertices.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/189.md) · [Batch record](../../batches/B013/README.md)

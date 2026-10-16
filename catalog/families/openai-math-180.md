---
id: openai-math-180
record_type: family
title: Disjoint planar states and a matched disk identity
source_family: '180'
source_collection: openai/math
batch_id: B012
subject: Combinatorics
source_paper_ids:
- P-000120
instrument_ids:
- MI-000198
- MI-000199
headline: The source claims that every finite cubic, bipartite, planar, three-vertex-connected graph is
  Hamiltonian.
central_instrument: A capacitated incidence matching is certified by planar face imbalance. A bijection
  between black triangles and nonroot vertices fixes the signed boundary sum of every selected directed
  cycle.
novelty_assessment: Planar states, matching flows and Euler counting are established. The selected candidate
  packages are the two-disjoint-state certificate and the exact disk identity. The later cancellation
  and Hamiltonian construction were not audited.
formalization_summary: BarnetteHamiltonian.lean states existence of a Hamiltonian cycle for finite simple
  cubic bipartite planar graphs satisfying its three-vertex-connectivity predicate; this is a single spanning
  cycle, not merely a two-factor. Scope documents and Comparator declarations were compared. No Lean solution
  was built or kernel-checked; the extracted auxiliary results are not separately certified targets.
statement_faithfulness: The paired-state existence result excludes separating triangles. The disk identity
  requires edges chosen from a state bijection; arbitrary oriented cycles need not satisfy it.
dependencies: Proper face coloring of a sphere triangulation; capacitated integral flow; boundary edge-side
  counts; Euler formula; state bijections.
antecedents: Hine and Kalman develop triangulation states and clock moves. Integral max flow and planar
  face counting provide classical ingredients.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Disjoint planar states and a matched disk identity

## Source manuscript and claim

[Paired states and Hamiltonian cycles in cubic bipartite planar graphs](../papers/P-000120.md), by OpenAI, September 24, 2026.

The source claims that every finite cubic, bipartite, planar, three-vertex-connected graph is Hamiltonian.

## Extracted instruments

- [MI-000198: Planar face imbalance certifies two disjoint incidence states](../instruments/MI-000198.md)
- [MI-000199: A state bijection fixes directed-cycle boundary weight at three](../instruments/MI-000199.md)

## Dependencies and antecedents

Proper face coloring of a sphere triangulation; capacitated integral flow; boundary edge-side counts; Euler formula; state bijections.

Hine and Kalman develop triangulation states and clock moves. Integral max flow and planar face counting provide classical ingredients. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the complete paired-state and disk-identity proofs. The weighted cancellation, nonvanishing and final spanning-forest construction were not audited.

BarnetteHamiltonian.lean states existence of a Hamiltonian cycle for finite simple cubic bipartite planar graphs satisfying its three-vertex-connectivity predicate; this is a single spanning cycle, not merely a two-factor. Scope documents and Comparator declarations were compared. No Lean solution was built or kernel-checked; the extracted auxiliary results are not separately certified targets.

The paired-state existence result excludes separating triangles. The disk identity requires edges chosen from a state bijection; arbitrary oriented cycles need not satisfy it.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/180.md) · [Batch record](../../batches/B012/README.md)

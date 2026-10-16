---
id: openai-math-161
record_type: family
title: Transferring a density deficit to finite witnesses and nonconstant equalities
source_family: '161'
source_collection: openai/math
batch_id: B020
subject: Combinatorics
source_paper_ids:
- P-000152
instrument_ids:
- MI-000265
- MI-000266
headline: The source claims a fixed bipartite graph H with 35 vertices and 66 edges and a finite nonempty
  simple graph G satisfying t(H,G)<p(G)^66.
central_instrument: A collision estimate and Jensen inequality give an explicit finite-host threshold.
  Orthogonal interpolation at fixed edge density turns a supplied strict deficit into a nonconstant exact-density
  equality.
novelty_assessment: Kernel sampling, collision bounds, rank-one sign expansions and continuous interpolation
  are established mechanisms. The selected consequences are conditional on a strict deficit. The source-specific
  negative-correlation construction providing that deficit was not audited.
formalization_summary: Read the scope document and SidorenkoCounterexample.lean pattern, density definitions
  and main target. The pattern is the incidence graph of 22 triples on 13 points; the forcing consequence
  is outside the selected target. These files specify targets with sorry placeholders; no Lean solution
  was built or kernel-checked.
statement_faithfulness: Densities count all maps and use p=2|E|/n^2. Repeated host edges are not independent
  under sampling. The forcing transfer requires a cycle and supplies one density, not every density.
dependencies: Independent vertex labels and edge trials, collision probability, convexity, even-subgraph
  expansions, polynomial continuity and the C4 equality case.
antecedents: Lovasz-Szegedy dense graph limits and finite-kernel sampling; classical tensor-power and
  graph-density methods.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Transferring a density deficit to finite witnesses and nonconstant equalities

## Source manuscript and claim

[A counterexample to Sidorenko's conjecture](../papers/P-000152.md), by OpenAI, September 23, 2026.

The source claims a fixed bipartite graph H with 35 vertices and 66 edges and a finite nonempty simple graph G satisfying t(H,G)<p(G)^66.

## Extracted instruments

- [MI-000265: A strict kernel-density deficit gives an explicit finite-host threshold](../instruments/MI-000265.md)
- [MI-000266: Orthogonal fixed-density interpolation preserves nonconstancy at an exact equality](../instruments/MI-000266.md)

## Dependencies and antecedents

Independent vertex labels and edge trials, collision probability, convexity, even-subgraph expansions, polynomial continuity and the C4 equality case.

Lovasz-Szegedy dense graph limits and finite-kernel sampling; classical tensor-power and graph-density methods. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the complete finite-host lemma and both consequence proofs. The kernel, pinning, orbit and tail construction establishing the strict bipartite deficit was not audited.

Read the scope document and SidorenkoCounterexample.lean pattern, density definitions and main target. The pattern is the incidence graph of 22 triples on 13 points; the forcing consequence is outside the selected target. These files specify targets with sorry placeholders; no Lean solution was built or kernel-checked.

Densities count all maps and use p=2|E|/n^2. Repeated host edges are not independent under sampling. The forcing transfer requires a cycle and supplies one density, not every density.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/161.md) · [Batch record](../../batches/B020/README.md)

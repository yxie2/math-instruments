---
id: openai-math-213
record_type: family
title: Cluster resampling and finite relay inequalities
source_family: '213'
source_collection: openai/math
batch_id: B077
subject: Probability and statistical mechanics
source_paper_ids:
- P-000486
instrument_ids:
- MI-000720
- MI-000721
headline: The family claims no critical infinite clusters on the cubic lattice and on every locally finite
  quasi-transitive graph with pc<1.
central_instrument: Ordered cluster columns form a cone with nonnegative coefficients; their inverse supplies
  relay weights for a joint connection comparison.
novelty_assessment: Selected mechanisms are separated from source headline claims and credited to known
  antecedents where established. Exhaustive priority is not established.
formalization_summary: CriticalZ3 targets bond and site critical clusters on Z3. CriticalPercolation targets
  independent bonds on infinite connected locally finite quasi-transitive graphs with pc<1, allowing multiplicities.
  The complete scope and named Comparators were read. Inspected theorem targets contain sorry; no separate
  solution or Lean build was checked.
statement_faithfulness: The finite model is independent undirected hyperedge percolation. Cone arguments
  use probabilities below one; the final event inequality extends to deterministic bits by continuity.
dependencies: Exact-cluster conditioning, deletion couplings, alternating conditional resampling, finite
  triangular matrices and a common-atom contraction.
antecedents: van den Berg-Haggstrom-Kahn conditional cluster resampling and elementary Markov-chain minorization.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Cluster resampling and finite relay inequalities

## Source manuscripts and claim

- [Critical bond and site percolation on the cubic lattice](../papers/P-000486.md): selected passages extracted.

The following companions are inventoried but have no extraction in this batch:

- [No percolation at criticality on quasi-transitive graphs](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/No-percolation-at-criticality-on-quasi-transitive-graphs-September-24-2026)

The family claims no critical infinite clusters on the cubic lattice and on every locally finite quasi-transitive graph with pc<1.

## Extracted instruments

- [MI-000720: Recover nonnegative cluster-column coordinates by conditional resampling](../instruments/MI-000720.md)
- [MI-000721: Transfer relay reliability through a joint connection inequality](../instruments/MI-000721.md)

## Dependencies and antecedents

Exact-cluster conditioning, deletion couplings, alternating conditional resampling, finite triangular matrices and a common-atom contraction.

van den Berg-Haggstrom-Kahn conditional cluster resampling and elementary Markov-chain minorization.

## Review and formalization scope

Read the entire finite connection section, including the residual coupling, resampling convergence, cone iteration, relay comparison and site-incidence proof. The quasi-transitive companion is inventory-only. The infinite-volume exploration arguments are not certified.

CriticalZ3 targets bond and site critical clusters on Z3. CriticalPercolation targets independent bonds on infinite connected locally finite quasi-transitive graphs with pc<1, allowing multiplicities. The complete scope and named Comparators were read. Inspected theorem targets contain sorry; no separate solution or Lean build was checked.

The finite model is independent undirected hyperedge percolation. Cone arguments use probabilities below one; the final event inequality extends to deterministic bits by continuity.

[Batch record](../../batches/B077/README.md)

---
id: openai-math-312
record_type: family
title: Coskeletal reflection and finite globular spines
source_family: '312'
source_collection: openai/math
batch_id: B037
subject: Topology
source_paper_ids:
- P-000220
instrument_ids:
- MI-000402
- MI-000403
headline: The source claims the Grothendieck homotopy hypothesis through elementary expansions of cellular
  coherator models.
central_instrument: A cutoff adds unique fillers above a fixed dimension while retaining lower cells;
  recursive spines isolate the dimensions needed for a particular homotopy test.
novelty_assessment: Coskeletal models and free-shape contractibility have explicit Henry-Lanari and Lanari
  antecedents. The extraction emphasizes the fixed presentation order and the separation from the unaudited
  elementary-expansion theorem.
formalization_summary: Inspected the elementary-expansion target and selected coherator/weak-equivalence
  definitions in GrothendieckElementaryExpansion.lean. Its target contains sorry. The scope excludes the
  later semi-model structure and full comparison. No full support audit or Lean build.
statement_faithfulness: Generating arities have height at most the output dimension, but composite operations
  can have greater arity height. The original free cellular order is retained. Distinct parallel q-cells
  survive R_q.
dependencies: Globular boundaries, free cellular theories, reflectors, colimit preservation and recursive
  suspension of globular shapes.
antecedents: Henry-Lanari, On the homotopy hypothesis for 3-groupoids, Section 2; Lanari free-shape contractibility
  cited by the source.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Coskeletal reflection and finite globular spines

## Source manuscript and claim

[The Grothendieck homotopy hypothesis via elementary expansions](../papers/P-000220.md), by OpenAI, None.

The source claims the Grothendieck homotopy hypothesis through elementary expansions of cellular coherator models.

## Extracted instruments

- [MI-000402: Reflect to unique high-dimensional fillers without changing low cells](../instruments/MI-000402.md)
- [MI-000403: Replace a globular pasting shape by a finite spine of controlled height](../instruments/MI-000403.md)

## Dependencies and antecedents

Globular boundaries, free cellular theories, reflectors, colimit preservation and recursive suspension of globular shapes.

Henry-Lanari, On the homotopy hypothesis for 3-groupoids, Section 2; Lanari free-shape contractibility cited by the source. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the coherator convention, cutoff reflector, higher-attachment invariance, finite-spine and free-shape contractibility proofs. Partial cylinders and the descending elementary-expansion induction were not audited.

Inspected the elementary-expansion target and selected coherator/weak-equivalence definitions in GrothendieckElementaryExpansion.lean. Its target contains sorry. The scope excludes the later semi-model structure and full comparison. No full support audit or Lean build.

Generating arities have height at most the output dimension, but composite operations can have greater arity height. The original free cellular order is retained. Distinct parallel q-cells survive R_q.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/312.md) · [Batch record](../../batches/B037/README.md)

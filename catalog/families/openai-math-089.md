---
id: openai-math-089
record_type: family
title: Fresh-noise branch stability and Markov gluing of cuts
source_family: 089
source_collection: openai/math
batch_id: B048
subject: Convex and metric geometry
source_paper_ids:
- P-000261
- P-000262
instrument_ids:
- MI-000482
- MI-000483
headline: The two source manuscripts claim uniform L1 embeddings for planar and bounded-treewidth graph
  metrics.
central_instrument: Condition on all but a fresh atom noise to control ties in a predetermined list. Consistent
  bag laws glue along a tree to a root-independent global cut measure.
novelty_assessment: Classical conditional anti-concentration and junction-tree sampling. The Markov gluing
  antecedent is explicit in Chlamtac-Krauthgamer-Raghavendra.
formalization_summary: The supplied targets assert a universal planar distortion constant and a constant
  depending only on the bag-size bound for treewidth. The scope document and linked Comparator definitions
  and target statements were read. The inspected targets contain sorry; no solution or Lean project was
  built.
statement_faithfulness: The atom list and geometric inputs precede the tested noises. Bag laws must agree
  on overlaps and satisfy the tree running-intersection property; arbitrary pairwise consistency on a
  cyclic family is insufficient.
dependencies: Independent uniform noises, deterministic finite candidate list, Lipschitz variation and
  connected paths; consistent finite bag measures and conditional sampling.
antecedents: Elementary interval anti-concentration; Chlamtac-Krauthgamer-Raghavendra, Section 3.2, Lemmas
  3.3 and 3.4.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Fresh-noise branch stability and Markov gluing of cuts

## Source manuscripts and claim

- [Planar Graph Metrics Embed into L1 with Constant Distortion](../papers/P-000261.md): selected passages extracted.
- [L1 Embeddings of Graphs of Bounded Treewidth](../papers/P-000262.md): selected passages extracted.

The two source manuscripts claim uniform L1 embeddings for planar and bounded-treewidth graph metrics.

## Extracted instruments

- [MI-000482: Stabilize a selected branch by exposing one fresh noise per comparison](../instruments/MI-000482.md)
- [MI-000483: Glue consistent bag laws into a global cut metric](../instruments/MI-000483.md)

## Dependencies and antecedents

Independent uniform noises, deterministic finite candidate list, Lipschitz variation and connected paths; consistent finite bag measures and conditional sampling.

Elementary interval anti-concentration; Chlamtac-Krauthgamer-Raghavendra, Section 3.2, Lemmas 3.3 and 3.4.

## Review and formalization scope

Read the full fresh-noise lemma, branch-comparison corollary and conditional-scope remark in the planar manuscript, and the separator and full Markov-gluing proofs in the treewidth manuscript. The source geometry producing the bounded list and the global lower-distortion constructions were not audited.

The supplied targets assert a universal planar distortion constant and a constant depending only on the bag-size bound for treewidth. The scope document and linked Comparator definitions and target statements were read. The inspected targets contain sorry; no solution or Lean project was built.

The atom list and geometric inputs precede the tested noises. Bag laws must agree on overlaps and satisfy the tree running-intersection property; arbitrary pairwise consistency on a cyclic family is insufficient.

[Batch record](../../batches/B048/README.md)

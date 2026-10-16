---
id: openai-math-317
record_type: family
title: Relative poset homotopies and nerve covers
source_family: '317'
source_collection: openai/math
batch_id: B037
subject: Topology
source_paper_ids:
- P-000222
instrument_ids:
- MI-000406
- MI-000407
headline: The source claims proper combinatorial Thomason model structures in every positive finite strict
  dimension and in dimension omega.
central_instrument: A common upper monotone map produces a relative homotopy zigzag when direct pointwise
  comparison fails. Sieve or cosieve covers become exact nerve unions.
novelty_assessment: Poset adjunctions, nerve homotopies and simplicial gluing are classical. The source
  higher-dimensional prism and model-transfer construction is not certified by these selected interfaces.
formalization_summary: Inspected FullMain, ExactModelEndpoint and final targets in ThomasonModelStructures.lean.
  They specify model structures, properness and Quillen equivalence in positive finite and omega dimensions;
  the targets contain sorry. The long support development was not audited and no Lean build was performed.
statement_faithfulness: The greatest-new-element construction gives a zigzag id<=g>=k, not necessarily
  id comparable with k. The nerve union requires both pieces to be full sieves or both full cosieves,
  not arbitrary full subcategories.
dependencies: Sieve poset inclusions, right adjoint retractions, monotone natural transformations, oriental
  endpoint arrows and monomorphic simplicial gluing.
antecedents: Classical poset nerve homotopies and Thomason-style gluing; no first-priority claim.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Relative poset homotopies and nerve covers

## Source manuscript and claim

[Thomason Model Structures in Every Strict Higher Dimension](../papers/P-000222.md), by OpenAI, None.

The source claims proper combinatorial Thomason model structures in every positive finite strict dimension and in dimension omega.

## Extracted instruments

- [MI-000406: Build a relative monotone zigzag through a greatest new element](../instruments/MI-000406.md)
- [MI-000407: Turn a full sieve cover into an exact Street-nerve union](../instruments/MI-000407.md)

## Dependencies and antecedents

Sieve poset inclusions, right adjoint retractions, monotone natural transformations, oriental endpoint arrows and monomorphic simplicial gluing.

Classical poset nerve homotopies and Thomason-style gluing; no first-priority claim. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the greatest-new-element proof and the complete two-piece nerve-cover lemma. The relative Gray-prism lemma used to transport the zigzag through arbitrary strict-category pushouts was not audited; neither was the model-transfer theorem.

Inspected FullMain, ExactModelEndpoint and final targets in ThomasonModelStructures.lean. They specify model structures, properness and Quillen equivalence in positive finite and omega dimensions; the targets contain sorry. The long support development was not audited and no Lean build was performed.

The greatest-new-element construction gives a zigzag id<=g>=k, not necessarily id comparable with k. The nerve union requires both pieces to be full sieves or both full cosieves, not arbitrary full subcategories.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/317.md) · [Batch record](../../batches/B037/README.md)

---
id: openai-math-106
record_type: family
title: Junta influence extraction and local list decoding
source_family: '106'
source_collection: openai/math
batch_id: B040
subject: Theoretical computer science
source_paper_ids:
- P-000232
instrument_ids:
- MI-000426
- MI-000427
headline: The source claims hardness of finding large independent sets in three-colorable graphs.
central_instrument: Dimension-free junta approximation locates and bounds influential coordinates. Deterministically
  chosen local lists convert collisions into ordinary game strategies.
novelty_assessment: Austin supplies the key continuous junta theorem. Influence extraction and the d-squared
  list bound are standard projection and union-bound consequences.
formalization_summary: Read IndependentSets.lean including binary input/output encodings and the real-threshold
  reduction target. mainTheoremReal contains sorry. No Lean build.
statement_faithfulness: The junta lists are soundness-analysis choices, not an efficiently computed part
  of the reduction. A list must depend only on its own question and fixed background for the strategy
  bound to apply.
dependencies: Austin junta approximation, conditional expectation, orthogonal product decompositions and
  projection-game soundness.
antecedents: Austin Theorem 1.1, extending Friedgut-type junta approximation; classical list decoding.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Junta influence extraction and local list decoding

## Source manuscript and claim

[Hardness of finding large independent sets in three-colorable graphs](../papers/P-000232.md), by OpenAI, September 24, 2026.

The source claims hardness of finding large independent sets in three-colorable graphs.

## Extracted instruments

- [MI-000426: Extract a large influence and bound all moderately large influences from juntas](../instruments/MI-000426.md)
- [MI-000427: Make subchain coordinate lists local before using a game soundness bound](../instruments/MI-000427.md)

## Dependencies and antecedents

Austin junta approximation, conditional expectation, orthogonal product decompositions and projection-game soundness.

Austin Theorem 1.1, extending Friedgut-type junta approximation; classical list decoding. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the complete influence, bounded-subchain-list and separated-list proofs, and the grid-extension setup. Global alignment and graph soundness were not audited.

Read IndependentSets.lean including binary input/output encodings and the real-threshold reduction target. mainTheoremReal contains sorry. No Lean build.

The junta lists are soundness-analysis choices, not an efficiently computed part of the reduction. A list must depend only on its own question and fixed background for the strategy bound to apply.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/106.md) · [Batch record](../../batches/B040/README.md)

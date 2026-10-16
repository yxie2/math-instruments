---
id: openai-math-183
record_type: family
title: Activity-to-distance conversion and fixed-scale power gains
source_family: '183'
source_collection: openai/math
batch_id: B044
subject: Combinatorics
source_paper_ids:
- P-000250
instrument_ids:
- MI-000462
- MI-000463
headline: The source claims a power saving for planar halving lines and k-sets.
central_instrument: Changing rank converts hidden membership activity into endpoint distance. A uniform
  small-constant packing hypothesis gives one fixed contraction scale and a genuine exponent saving.
novelty_assessment: The second step is a classical scale-induction mechanism. The source all-rank activity
  input is the substantial separate hypothesis; no halving-line novelty or correctness certification.
formalization_summary: Read HalvingLines.lean in full and the scope document. power_bounds contains sorry;
  it states existential positive exponent savings, with generic assumptions for all ranks. No Lean build.
statement_faithfulness: Activity counts distinct participating points, not endpoint distance or switches.
  The packing estimate must be uniform in size and rank; the selected argument provides no numerical exponent
  without an explicit scale.
dependencies: Single-crossing affine comparisons, complementary ranks, greedy activity blocks, hereditary
  restriction and induction at one fixed scale.
antecedents: Classical sweep and crossing-number framework; fixed-scale recurrence improvement.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Activity-to-distance conversion and fixed-scale power gains

## Source manuscript and claim

[A power saving for planar halving lines](../papers/P-000250.md), by OpenAI, September 25, 2026.

The source claims a power saving for planar halving lines and k-sets.

## Extracted instruments

- [MI-000462: Expose returning sweep activity by shifting the rank](../instruments/MI-000462.md)
- [MI-000463: Turn uniform small packing constants into a fixed exponent saving](../instruments/MI-000463.md)

## Dependencies and antecedents

Single-crossing affine comparisons, complementary ranks, greedy activity blocks, hereditary restriction and induction at one fixed scale.

Classical sweep and crossing-number framework; fixed-scale recurrence improvement. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the complete finite activity and greedy lemmas and packing-to-power proof, including the subsequent conditional k-sensitive reduction. The uniform activity-packing theorem was not audited.

Read HalvingLines.lean in full and the scope document. power_bounds contains sorry; it states existential positive exponent savings, with generic assumptions for all ranks. No Lean build.

Activity counts distinct participating points, not endpoint distance or switches. The packing estimate must be uniform in size and rank; the selected argument provides no numerical exponent without an explicit scale.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/183.md) · [Batch record](../../batches/B044/README.md)

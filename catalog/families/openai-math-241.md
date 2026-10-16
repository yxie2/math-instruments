---
id: openai-math-241
record_type: family
title: Bounded feedback recovery and removal of generic oracle parameters
source_family: '241'
source_collection: openai/math
batch_id: B021
subject: Mathematical logic
source_paper_ids:
- P-000155
instrument_ids:
- MI-000271
- MI-000272
headline: The source claims that every order automorphism of the full Turing degrees is the identity,
  with no definability assumption on the automorphism.
central_instrument: A bounded binary feedback recurrence recovers an irrational slope from four function
  values. A category argument removes auxiliary cut oracles even when the successful reduction index varies
  with the parameters.
novelty_assessment: Category cone avoidance is classical. The prescribed-affine four-value recovery is
  a source-specific construction with different hypotheses from prior perfect-set coding. This targeted
  comparison is not an exhaustive novelty audit; the external all-input representation theorem was not
  independently audited.
formalization_summary: Read DegreeRigidity.lean, including its oracle reducibility, antisymmetrized degree
  order and unrestricted rigidity target. Representation and biinterpretability corollaries are outside
  the selected target. These are target statements with sorry placeholders; no Lean solution was built
  or kernel-checked.
statement_faithfulness: F is Borel with countable fibers and satisfies a pointwise addition reduction.
  The four-value reduction exists nonuniformly for each generic pair; only finitely many integers and
  a rational step are hard-coded, with no additional real oracle.
dependencies: Baire-property continuity on a comeager restriction, countable affine shifts, finite oracle-program
  composition, bounded discrepancy and rational-cut transcripts.
antecedents: Sacks category cone avoidance, as stated by Kumar-Shelah in Large Turing independent sets,
  Lemma 4.1; Groszek-Slaman and Lutz-Siskind perfect-set recovery; the source separately invokes Slaman-Woodin
  representation.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Bounded feedback recovery and removal of generic oracle parameters

## Source manuscript and claim

[Rigidity of the Turing degrees](../papers/P-000155.md), by OpenAI, September 24, 2026.

The source claims that every order automorphism of the full Turing degrees is the identity, with no definability assumption on the automorphism.

## Extracted instruments

- [MI-000271: Four-value oracle recovery through a bounded binary feedback recurrence](../instruments/MI-000271.md)
- [MI-000272: Dense finite oracle transcripts remove auxiliary real parameters](../instruments/MI-000272.md)

## Dependencies and antecedents

Baire-property continuity on a comeager restriction, countable affine shifts, finite oracle-program composition, bounded discrepancy and rational-cut transcripts.

Sacks category cone avoidance, as stated by Kumar-Shelah in Large Turing independent sets, Lemma 4.1; Groszek-Slaman and Lutz-Siskind perfect-set recovery; the source separately invokes Slaman-Woodin representation. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the complete recovery and category-avoidance proofs, the continuity lemma and representation passage. The external Slaman-Woodin all-input representation theorem and the full rigidity/biinterpretability deductions were not independently certified.

Read DegreeRigidity.lean, including its oracle reducibility, antisymmetrized degree order and unrestricted rigidity target. Representation and biinterpretability corollaries are outside the selected target. These are target statements with sorry placeholders; no Lean solution was built or kernel-checked.

F is Borel with countable fibers and satisfies a pointwise addition reduction. The four-value reduction exists nonuniformly for each generic pair; only finitely many integers and a rational step are hard-coded, with no additional real oracle.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/241.md) · [Batch record](../../batches/B021/README.md)

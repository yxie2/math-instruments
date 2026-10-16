---
id: openai-math-277
record_type: family
title: Conditioning budgets and threshold repetition for entangled games
source_family: '277'
source_collection: openai/math
batch_id: B002
subject: Mathematical physics
source_paper_ids:
- P-000085
instrument_ids:
- MI-000123
- MI-000124
headline: The source derives a universal fifth-power threshold exponent for finite entangled games from
  an external conditioning estimate, and a cubic exponent depending on the question distribution.
central_instrument: A quantitative conditioning-to-tail transfer and reference-state rounding on connected
  components of the question support.
novelty_assessment: quantitative transfer and support-rounding combinations; established sampling and
  purification components are retained with attribution
formalization_summary: 'EntangledGames Comparator inspected: universal delta^13 rate only. The paper states
  delta^5 and a distribution-dependent cubic rate. No Lean build performed.'
statement_faithfulness: The selected formal statement is weaker than the paper main theorem and excludes
  its distribution-dependent cubic estimate.
dependencies: Song conditioning estimate for the universal application; operator-entropy exposure estimates
  for support rounding; classical sampling, tensor-copy amplification and Pinsker inequality.
antecedents: Rao concentration; Yuen tested-coordinate sampling; anchored entangled repetition; connection-graph
  methods; earlier OpenAI resolvent purification.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Conditioning budgets and threshold repetition for entangled games

## Source manuscript and claim

[Threshold parallel repetition for finite-dimensional entangled games](../papers/P-000085.md), by OpenAI, September 25, 2026.

The source derives a universal fifth-power threshold exponent for finite entangled games from an external conditioning estimate, and a cubic exponent depending on the question distribution.

## Extracted instruments

- [MI-000123: A tested-set conditioning budget gives an explicit threshold exponent](../instruments/MI-000123.md)
- [MI-000124: Reference-state rounding on question-support components](../instruments/MI-000124.md)

## Dependencies and antecedents

Song conditioning estimate for the universal application; operator-entropy exposure estimates for support rounding; classical sampling, tensor-copy amplification and Pinsker inequality.

Rao concentration; Yuen tested-coordinate sampling; anchored entangled repetition; connection-graph methods; earlier OpenAI resolvent purification. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Checked the transfer proof, the all-length tensor-copy step, the root-path estimate and the displayed exponent arithmetic. The exposure lemma and the external Song estimate were not fully re-proved. Fresh comparisons distinguish threshold events from all-wins repetition.

EntangledGames Comparator inspected: universal delta^13 rate only. The paper states delta^5 and a distribution-dependent cubic rate. No Lean build performed.

The selected formal statement is weaker than the paper main theorem and excludes its distribution-dependent cubic estimate.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/277.md) · [Batch record](../../batches/B002/README.md)

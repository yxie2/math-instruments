---
id: openai-math-276
record_type: family
title: Thermal block entropy and generalized amplitude-damping capacity
source_family: '276'
source_collection: openai/math
batch_id: B002
subject: Mathematical physics
source_paper_ids:
- P-000084
instrument_ids:
- MI-000121
- MI-000122
headline: The source claims a scalar capacity formula and tensor-power additivity for every qubit generalized
  amplitude-damping channel, plus additivity with every finite-dimensional partner channel.
central_instrument: A convex decomposition into two zero-block Gram matrices with the same scalar entropy
  contribution, followed by a common-Kraus branch bound.
novelty_assessment: thermal extension is a candidate new combination; zero-block inequality and one-use
  optimizer have prior sources
formalization_summary: AmplitudeDamping Comparator inspected for tensor powers, the scalar optimum and
  operational capacity; arbitrary-partner additivity is outside that selected statement. No Lean build
  performed.
statement_faithfulness: The selected Comparator covers repeated uses of one channel, not the stronger
  arbitrary-partner assertion in the manuscript.
dependencies: Triangular block entropy inequality of Tang--Zhu--Bai--Wang; entropy concavity; rectangular
  Kraus representations; convexity of the population-dependent output entropy.
antecedents: Earlier one-use amplitude-damping optimizers, ordinary-damping additivity, and unital/entanglement-breaking
  special cases.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Thermal block entropy and generalized amplitude-damping capacity

## Source manuscript and claim

[Classical capacity and entropy inequalities for generalized amplitude damping](../papers/P-000084.md), by OpenAI, September 24, 2026.

The source claims a scalar capacity formula and tensor-power additivity for every qubit generalized amplitude-damping channel, plus additivity with every finite-dimensional partner channel.

## Extracted instruments

- [MI-000121: A thermal block decomposition preserves the scalar entropy term](../instruments/MI-000121.md)
- [MI-000122: Common Kraus columns retain conditional partner entropy](../instruments/MI-000122.md)

## Dependencies and antecedents

Triangular block entropy inequality of Tang--Zhu--Bai--Wang; entropy concavity; rectangular Kraus representations; convexity of the population-dependent output entropy.

Earlier one-use amplitude-damping optimizers, ordinary-damping additivity, and unital/entanglement-breaking special cases. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Checked the endpoint mixture algebra, coefficient conditions, rectangular Kraus substitution and the scope of the supplied Comparator. The underlying triangular block theorem was traced to its cited antecedent, not independently proved in this batch.

AmplitudeDamping Comparator inspected for tensor powers, the scalar optimum and operational capacity; arbitrary-partner additivity is outside that selected statement. No Lean build performed.

The selected Comparator covers repeated uses of one channel, not the stronger arbitrary-partner assertion in the manuscript.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/276.md) · [Batch record](../../batches/B002/README.md)

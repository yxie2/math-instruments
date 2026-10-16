---
id: PAT-013
record_type: pattern
title: Control what an adaptive choice can observe
batch_id: B045
instrument_ids: [MI-000424, MI-000427, MI-000456]
updated: '2026-10-16'
---

# Control what an adaptive choice can observe

[Pattern index](README.md) · [Research guide](../../methodology/research-guide.md)

Several source arguments permit choices that depend on data, but only after specifying precisely which data is available. A useful bound can fail if one silently adds information or conditions on a successful outcome.

- [MI-000424](../instruments/MI-000424.md) bounds the probability that an adaptively selected child is marked. The selection sees raw observations with bounded likelihood ratio, but not the hidden mark or metadata revealing it. The proof conditions on those permitted observations and then averages. It does not condition on success.
- [MI-000427](../instruments/MI-000427.md) chooses bounded coordinate lists by a fixed deterministic rule. Each list must depend only on its own question and fixed background. This makes each pair of list positions a legal strategy and permits the collision bound. Dependence on the opposite question invalidates that step.
- [MI-000456](../instruments/MI-000456.md) concentrates all reserved candidate roles before a later selection. Stationarity comes from averaging over the starting coordinate. The resulting statement is neither a guarantee for each individual start nor a conditional guarantee along the selected answer path.

The shared method is to write the information available at each decision, prove the estimate with respect to that information, and only then make the decision. The probability inequalities themselves are classical; the useful extracted content is the exact information contract.

A proposed application is to audit a new adaptive sampling or decoding proof. First list every random variable revealed to the selector. Then test whether the posterior bound, local strategy or stationary average survives those revelations. The linked finite checks include controls illustrating failures when the contract is weakened. No new decoding theorem is claimed here.

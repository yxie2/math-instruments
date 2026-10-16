---
id: openai-math-105
record_type: family
title: Adaptive posterior bounds and dimension-free bilinear bias
source_family: '105'
source_collection: openai/math
batch_id: B040
subject: Theoretical computer science
source_paper_ids:
- P-000231
instrument_ids:
- MI-000424
- MI-000425
headline: The source claims perfect-completeness hardness for 2-to-1 games.
central_instrument: A likelihood-ratio bound controls a small adaptively chosen witness set. Quarter balance
  of independent factors produces a dimension-free bilinear bias estimate.
novelty_assessment: Bayes, conditional union bounds and character-wise bias amplification are standard.
  Their precise exposure interface is the useful extraction; no independent priority claim.
formalization_summary: Read PerfectCompleteness.lean and its binary reduction definitions. The target
  exists_reduction contains sorry. No Lean build or reduction implementation audit.
statement_faithfulness: Posterior control excludes marks and success-conditioning information. Bias amplification
  requires independent factor draws and fresh hidden buckets; it is not asserted after arbitrary slice
  conditioning.
dependencies: Product likelihood ratios, conditional expectation, bilinearity and independent character
  multiplication.
antecedents: Classical Bayes and union bounds; Naor-Naor small-bias framework.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Adaptive posterior bounds and dimension-free bilinear bias

## Source manuscript and claim

[Perfect completeness for 2-to-1 games](../papers/P-000231.md), by OpenAI, September 23, 2026.

The source claims perfect-completeness hardness for 2-to-1 games.

## Extracted instruments

- [MI-000424: Bound an adaptively selected witness set by posterior likelihood ratios](../instruments/MI-000424.md)
- [MI-000425: Amplify bilinear anti-concentration without a dimension loss](../instruments/MI-000425.md)

## Dependencies and antecedents

Product likelihood ratios, conditional expectation, bilinearity and independent character multiplication.

Classical Bayes and union bounds; Naor-Naor small-bias framework. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read both selected proofs completely. The sampler construction ensuring their conditional product laws and the complete hardness reduction were not audited.

Read PerfectCompleteness.lean and its binary reduction definitions. The target exists_reduction contains sorry. No Lean build or reduction implementation audit.

Posterior control excludes marks and success-conditioning information. Bias amplification requires independent factor draws and fresh hidden buckets; it is not asserted after arbitrary slice conditioning.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/105.md) · [Batch record](../../batches/B040/README.md)

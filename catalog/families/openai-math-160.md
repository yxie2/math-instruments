---
id: openai-math-160
record_type: family
title: Counting affine boundary patterns and lifting cyclic colorings
source_family: '160'
source_collection: openai/math
batch_id: B020
subject: Combinatorics
source_paper_ids:
- P-000151
instrument_ids:
- MI-000263
- MI-000264
headline: The source claims an absolute threshold K such that W_r(k)>k^(k floor(log_2 r)/100000) for all
  k>=K and all r>=2.
central_instrument: An arrangement count retains equality signs at mesh boundaries, and the first nonzero
  base-N digit of a progression step transfers cyclic avoidance to an interval product coloring.
novelty_assessment: Both extracted mechanisms are established arrangement and digit-product ideas. The
  source gives explicit boundary and composite-base bookkeeping. The central coloring construction behind
  its claimed superexponential two-color bound was not audited.
formalization_summary: Read the scope document and QuantitativeVanDerWaerden.lean definitions and uniform_lower_bound
  target. The target keeps one threshold uniform in the color count. These files specify targets with
  sorry placeholders; no Lean solution was built or kernel-checked.
statement_faithfulness: Zero signs are counted, including dependent or repeated hyperplanes. Cyclic progressions
  have nonzero common difference but may repeat residues; the transfer does not require N prime.
dependencies: Affine rank, the hyperplane-region recurrence, base-N digits and monotonicity in the number
  of colors.
antecedents: Stanley, An Introduction to Hyperplane Arrangements, Lemma 2.1 and Proposition 2.4; classical
  Erdos-Turan digit constructions; Fox-Hunter product-coloring arguments.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Counting affine boundary patterns and lifting cyclic colorings

## Source manuscript and claim

[Quantitative Superexponential Bounds for van der Waerden Numbers](../papers/P-000151.md), by OpenAI, September 23, 2026.

The source claims an absolute threshold K such that W_r(k)>k^(k floor(log_2 r)/100000) for all k>=K and all r>=2.

## Extracted instruments

- [MI-000263: Affine sign-pattern counting that retains boundary equalities](../instruments/MI-000263.md)
- [MI-000264: The first nonzero digit of a step transfers cyclic avoidance to product colorings](../instruments/MI-000264.md)

## Dependencies and antecedents

Affine rank, the hyperplane-region recurrence, base-N digits and monotonicity in the number of colors.

Stanley, An Introduction to Hyperplane Arrangements, Lemma 2.1 and Proposition 2.4; classical Erdos-Turan digit constructions; Fox-Hunter product-coloring arguments. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the complete affine-comparison count and cyclic-to-interval product proof. The outer coloring, local dichotomy and random perturbation estimates were not audited.

Read the scope document and QuantitativeVanDerWaerden.lean definitions and uniform_lower_bound target. The target keeps one threshold uniform in the color count. These files specify targets with sorry placeholders; no Lean solution was built or kernel-checked.

Zero signs are counted, including dependent or repeated hyperplanes. Cyclic progressions have nonzero common difference but may repeat residues; the transfer does not require N prime.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/160.md) · [Batch record](../../batches/B020/README.md)

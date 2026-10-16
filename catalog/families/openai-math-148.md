---
id: openai-math-148
record_type: family
title: Pair capacity and entropy gains before averaging the future
source_family: '148'
source_collection: openai/math
batch_id: B014
subject: Dynamical systems and ergodic theory
source_paper_ids:
- P-000129
instrument_ids:
- MI-000217
- MI-000218
headline: The source claims the entropy-rate dimension formula for every finite self-similar law on the
  line with nonzero strictly contracting ratios, including signed and unequal ratios.
central_instrument: Fair-pair capacity measures hidden entropy below a grid scale. A two-point entropy
  increment can then be averaged over future environments while keeping the selected pair and contraction
  fixed by the past.
novelty_assessment: Fair-pair decomposition and entropy gain under convolution have explicit antecedents
  in Varju. The sumset-controlled capacity bound and conditioning interface are the selected candidate
  refinements; the global dimension formula is not certified here.
formalization_summary: SelfSimilar and SelfSimilarCorollaries state the lower Hausdorff dimension formula
  and the no-exact-overlap homogeneous measure and attractor consequences. The rate uses entropy of complete
  composed affine maps. Scope text and Comparator statements were read. No Lean solution was built or
  kernel-checked; the extracted auxiliary lemmas are not separately certified targets.
statement_faithfulness: Entropy is in bits. Scale-interval entropy is concave and convolution-monotone
  in the form used here when the coarse/fine ratio is an integer. Nonsaturation is required for the averaged
  tail, not for every realized future.
dependencies: Finite entropy, fractional pair packing, independent samples, randomized nested cuts, observed-sum
  conditioning, shifted-grid entropy and Jensen averaging.
antecedents: Varju, Absolute continuity of Bernoulli convolutions for algebraic parameters, Propositions
  20 and 21 and Lemma 22, provide fair-pair decomposition and convolution entropy gain.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Pair capacity and entropy gains before averaging the future

## Source manuscript and claim

[The entropy-rate dimension formula for self-similar measures on the line](../papers/P-000129.md), by OpenAI, September 24, 2026.

The source claims the entropy-rate dimension formula for every finite self-similar law on the line with nonzero strictly contracting ratios, including signed and unequal ratios.

## Extracted instruments

- [MI-000217: A sumset bound converts hidden grid entropy into fair-pair capacity at finer scales](../instruments/MI-000217.md)
- [MI-000218: Two-point entropy gains survive future averaging when the pair is fixed by the past](../instruments/MI-000218.md)

## Dependencies and antecedents

Finite entropy, fractional pair packing, independent samples, randomized nested cuts, observed-sum conditioning, shifted-grid entropy and Jensen averaging.

Varju, Absolute continuity of Bernoulli convolutions for algebraic parameters, Propositions 20 and 21 and Lemma 22, provide fair-pair decomposition and convolution entropy gain. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the complete finite pair-bound proof, shifted-entropy definitions, two-point gain and conditional-gain lemma. Uniform nonsaturation and the global dimension argument were not audited.

SelfSimilar and SelfSimilarCorollaries state the lower Hausdorff dimension formula and the no-exact-overlap homogeneous measure and attractor consequences. The rate uses entropy of complete composed affine maps. Scope text and Comparator statements were read. No Lean solution was built or kernel-checked; the extracted auxiliary lemmas are not separately certified targets.

Entropy is in bits. Scale-interval entropy is concave and convolution-monotone in the form used here when the coarse/fine ratio is an integer. Nonsaturation is required for the averaged tail, not for every realized future.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/148.md) · [Batch record](../../batches/B014/README.md)

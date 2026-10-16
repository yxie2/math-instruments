---
id: openai-math-021
record_type: family
title: Probability weights and stable second moments for sieve paths
source_family: '021'
source_collection: openai/math
batch_id: B007
subject: Number theory
source_paper_ids:
- P-000102
instrument_ids:
- MI-000160
- MI-000161
headline: The source claims h(k)<=C k^2/(log log(3k))^2 for Jacobsthal intervals and every k>=1, uniformly
  over positive moduli with at most k distinct prime factors and signed interval starts. This extraction
  selects two probabilistic auxiliary tools.
central_instrument: Derivatives of the linear-sieve functions normalize harmonic path weights into a probability
  kernel with an exact endpoint factor; a two-point singular-series average remains valid under a controlled
  change of measure.
novelty_assessment: Linear-sieve delay functions, positive-function changes of measure and Gallagher singular-series
  averages are established. The source combines derivative weights and a stable finite-measure variance
  estimate in a stopped sieve tree. Neither the global bound nor priority is certified.
formalization_summary: JacobsthalImproved.lean states the iterated-logarithm saving with an absolute positive
  constant, all k>=1, arbitrary signed starts and moduli with at most k prime factors. Jacobsthal.lean
  retains the weaker quadratic statement. The scope document and Comparator declarations were compared,
  but no Lean solution was built or kernel-checked. The extracted auxiliary mechanisms are not separate
  Comparator statements.
statement_faithfulness: The claim is uniform over moduli, not only primorials, and does not determine
  the optimal growth of h(k). The source does not provide an explicit usable constant. Auxiliary bin widths
  and tree parameters are fixed before the main scale tends to infinity.
dependencies: Positive derivative weights solving coupled future-integral equations; a telescoping change
  of path measure; independent random forbidden residue classes; a summable divisor expansion and first/second-moment
  comparisons under finite positive measures.
antecedents: Iwaniec supplies the linear-sieve background. Gallagher supplies mean-one singular-series
  averaging, and Banks-Ford-Tao provide related random-sieve context. Regeneration and renewal theory
  used later in the source are established probabilistic tools.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Probability weights and stable second moments for sieve paths

## Source manuscript and claim

[A quadratic bound for Jacobsthal's function](../papers/P-000102.md), by OpenAI, None.

The source claims h(k)<=C k^2/(log log(3k))^2 for Jacobsthal intervals and every k>=1, uniformly over positive moduli with at most k distinct prime factors and signed interval starts. This extraction selects two probabilistic auxiliary tools.

## Extracted instruments

- [MI-000160: Derivative weights turn harmonic sieve paths into a probability process](../instruments/MI-000160.md)
- [MI-000161: Random forbidden classes have a second moment stable under measure changes](../instruments/MI-000161.md)

## Dependencies and antecedents

Positive derivative weights solving coupled future-integral equations; a telescoping change of path measure; independent random forbidden residue classes; a summable divisor expansion and first/second-moment comparisons under finite positive measures.

Iwaniec supplies the linear-sieve background. Gallagher supplies mean-one singular-series averaging, and Banks-Ford-Tao provide related random-sieve context. Regeneration and renewal theory used later in the source are established probabilistic tools. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the derivative-weight proof and exact path-density conversion, and the complete independent-class variance argument with its stable version. The regeneration estimates, inverse incidence theorem and stopped-tree comparison needed for the final Jacobsthal bound were not fully audited.

JacobsthalImproved.lean states the iterated-logarithm saving with an absolute positive constant, all k>=1, arbitrary signed starts and moduli with at most k prime factors. Jacobsthal.lean retains the weaker quadratic statement. The scope document and Comparator declarations were compared, but no Lean solution was built or kernel-checked. The extracted auxiliary mechanisms are not separate Comparator statements.

The claim is uniform over moduli, not only primorials, and does not determine the optimal growth of h(k). The source does not provide an explicit usable constant. Auxiliary bin widths and tree parameters are fixed before the main scale tends to infinity.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/021.md) · [Batch record](../../batches/B007/README.md)

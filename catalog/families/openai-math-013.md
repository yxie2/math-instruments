---
id: openai-math-013
record_type: family
title: Affine mixing and overlap counting in a prime-sumset argument
source_family: '013'
source_collection: openai/math
batch_id: B007
subject: Number theory
source_paper_ids:
- P-000100
instrument_ids:
- MI-000156
- MI-000157
headline: The source claims that no sum of two subsets of the nonnegative integers, each with at least
  two elements, differs from the primes in only finitely many places. This extraction selects two finite
  auxiliary estimates.
central_instrument: A weighted affine-action calculation controls mixed additive and multiplicative correlations;
  factorial counting makes arrangements with many overlap components scarce.
novelty_assessment: Affine mixing, Parseval and factorial entropy estimates are established. The explicit
  weighted operator and its combination with fixed-depth prime trees are candidate source-specific refinements;
  the full inverse Goldbach theorem and priority are not certified.
formalization_summary: OstmannPrimes.lean and OstmannComplete.lean state the infinite symmetric-difference
  assertion for nontrivial subsets of the natural numbers; the latter also states the two-infinite-summands
  case. The scope document and Comparator declarations were compared, but no Lean solution was built or
  kernel-checked. The extracted auxiliary mechanisms are not separate Comparator statements.
statement_faithfulness: Eventual equality with the primes requires both coverage of every sufficiently
  large prime and exclusion of every sufficiently large composite. It is stronger than density or thin
  prime-sumset statements. Tree depth is fixed before the arithmetic scale tends to infinity.
dependencies: Probability-normalized finite-field Fourier analysis; characters extended by zero at zero;
  bounded representation multiplicity in the affine group; equal-sized blocks and overlap multigraphs.
  The full source additionally uses inverse-sieve, prime-coverage and arithmetic transfer arguments.
antecedents: Gowers, Babai-Nikolov-Pyber and Gill provide quasirandom convolution and group-action context.
  Elsholtz-Harper and Green-Harper provide earlier inverse Goldbach and inverse-sieve restrictions. The
  source discusses a newer quadratic inverse theorem but does not equate a large intersection with near
  containment.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Affine mixing and overlap counting in a prime-sumset argument

## Source manuscript and claim

[The additive indecomposability of the primes](../papers/P-000100.md), by OpenAI, September 24, 2026.

The source claims that no sum of two subsets of the nonnegative integers, each with at least two elements, differs from the primes in only finitely many places. This extraction selects two finite auxiliary estimates.

## Extracted instruments

- [MI-000156: A weighted affine family has small norm on mean-zero functions](../instruments/MI-000156.md)
- [MI-000157: Overlap components give an entropy bound for bad block arrangements](../instruments/MI-000157.md)

## Dependencies and antecedents

Probability-normalized finite-field Fourier analysis; characters extended by zero at zero; bounded representation multiplicity in the affine group; equal-sized blocks and overlap multigraphs. The full source additionally uses inverse-sieve, prime-coverage and arithmetic transfer arguments.

Gowers, Babai-Nikolov-Pyber and Gill provide quasirandom convolution and group-action context. Elsholtz-Harper and Green-Harper provide earlier inverse Goldbach and inverse-sieve restrictions. The source discusses a newer quadratic inverse theorem but does not equate a large intersection with near containment. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the finite affine-action calculation, bottom-pair autocorrelation identities and complete bad-arrangement count. The full finite-field tree comparison, the prime-supply estimate and the arithmetic transfer were not independently certified. The source labels its cross-release quasi-Riemann observation optional; these extracted estimates do not use it.

OstmannPrimes.lean and OstmannComplete.lean state the infinite symmetric-difference assertion for nontrivial subsets of the natural numbers; the latter also states the two-infinite-summands case. The scope document and Comparator declarations were compared, but no Lean solution was built or kernel-checked. The extracted auxiliary mechanisms are not separate Comparator statements.

Eventual equality with the primes requires both coverage of every sufficiently large prime and exclusion of every sufficiently large composite. It is stronger than density or thin prime-sumset statements. Tree depth is fixed before the arithmetic scale tends to infinity.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/013.md) · [Batch record](../../batches/B007/README.md)

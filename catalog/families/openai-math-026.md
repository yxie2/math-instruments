---
id: openai-math-026
record_type: family
title: From weighted adjacent blocks to ordinary prime-gap density
source_family: '026'
source_collection: openai/math
batch_id: B022
subject: Number theory
source_paper_ids:
- P-000159
instrument_ids:
- MI-000280
- MI-000281
headline: The source claims that for each C>0 a positive lower proportion of consecutive prime gaps exceed
  C log p_n, with a bound holding for every sufficiently large N. It also deduces a positive lower density
  of increases of p_n/n.
central_instrument: Two weighted Cauchy-Schwarz inequalities transfer positive weighted mass to ordinary
  density, after adjacent-block charging controls multiplicity. A smooth profile keeps its L1 and L2 norms
  fixed while making its first squared moment arbitrarily small.
novelty_assessment: Moment inequalities and product-profile constructions have classical antecedents,
  including Maynard sieve weights. The selected cards isolate source-specific parameter bookkeeping; they
  do not certify the weight construction or a new prime-gap theorem.
formalization_summary: Read PrimeGaps.lean. Its actual large_gaps_and_ratio_density target conjoins the
  full arbitrary-C large-gap assertion with ratio-increase density. The accompanying scope note describes
  only the ratio assertion, so it understates the target actually displayed. The inspected Comparator
  files contain target statements with sorry placeholders; no Lean solution was built or kernel-checked.
statement_faithfulness: The second weighted prime moment must be uniform in the small error parameter.
  The ordinary second moment of the weights may depend on that parameter, which is fixed before X tends
  to infinity. The conclusion is ordinary lower density, not only a weighted count or a subsequence.
dependencies: Nonnegative weights, two Cauchy-Schwarz inequalities, a bounded-multiplicity assignment
  to consecutive gaps, the prime number theorem, smooth truncation and dilation.
antecedents: Maynard, Small gaps between primes, Section 7; classical weighted second-moment and counting
  arguments.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# From weighted adjacent blocks to ordinary prime-gap density

## Source manuscript and claim

[Positive lower density of large prime gaps](../papers/P-000159.md), by OpenAI, September 25, 2026.

The source claims that for each C>0 a positive lower proportion of consecutive prime gaps exceed C log p_n, with a bound holding for every sufficiently large N. It also deduces a positive lower density of increases of p_n/n.

## Extracted instruments

- [MI-000280: Weighted adjacent-block success becomes ordinary gap density](../instruments/MI-000280.md)
- [MI-000281: A smooth profile with fixed L1 and L2 norms and arbitrarily small first moment](../instruments/MI-000281.md)

## Dependencies and antecedents

Nonnegative weights, two Cauchy-Schwarz inequalities, a bounded-multiplicity assignment to consecutive gaps, the prime number theorem, smooth truncation and dilation.

Maynard, Small gaps between primes, Section 7; classical weighted second-moment and counting arguments. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the complete counting reduction and small-first-moment profile proof. The substantial sieve estimates establishing the required weight moments were not audited.

Read PrimeGaps.lean. Its actual large_gaps_and_ratio_density target conjoins the full arbitrary-C large-gap assertion with ratio-increase density. The accompanying scope note describes only the ratio assertion, so it understates the target actually displayed. The inspected Comparator files contain target statements with sorry placeholders; no Lean solution was built or kernel-checked.

The second weighted prime moment must be uniform in the small error parameter. The ordinary second moment of the weights may depend on that parameter, which is fixed before X tends to infinity. The conclusion is ordinary lower density, not only a weighted count or a subsequence.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/026.md) · [Batch record](../../batches/B022/README.md)

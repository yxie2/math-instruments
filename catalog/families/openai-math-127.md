---
id: openai-math-127
record_type: family
title: One-sided stationary coupling and weighted cube edge recovery
source_family: '127'
source_collection: openai/math
batch_id: B011
subject: Theoretical computer science
source_paper_ids:
- P-000116
instrument_ids:
- MI-000190
- MI-000191
headline: The source claims average sensitivity at most 8d sqrt(n) for every real degree-at-most-d polynomial
  threshold function on the uniform n-cube, assigning positive sign at zero.
central_instrument: An equal-marginal primitive identity converts a one-sided displacement bound into
  a quadratic estimate. Weighted orthogonal polynomial grades convert that estimate into sensitive-edge
  counts through an anticommutator and a binomial coupling.
novelty_assessment: Equal-law primitive cancellation and weighted polynomial three-term recurrences are
  established. The selected candidate packages are the quantitative one-sided estimate and edge recovery
  from the centered grading. The exact-extremizer conjecture is a different statement.
formalization_summary: GotsmanLinial.lean states the 8d sqrt(n) uniform-cube bound for multilinear real
  polynomials, 1<=d<=n, with sign zero equal to one. It does not identify exact extremizers. Scope documents
  and Comparator statements were compared. No Lean solution was built or kernel-checked, and the extracted
  auxiliary results are not separately certified Comparator targets.
statement_faithfulness: The coupling needs equal distributions, not independence or exchangeability. The
  grading weight must be strictly positive. A small positive shift preserves threshold signs and removes
  zeros before setting w=|p|.
dependencies: An increasing quadratic primitive; equal-marginal cancellation; weighted polynomial filtration;
  coordinate tridiagonality; parity conjugation; Hilbert-Schmidt block norms; reflected binomial marginals.
antecedents: Rollin replaces exchangeability by equality of distributions through primitive differences
  in Stein methods. Xu develops discrete multivariate orthogonal polynomial grading. The source distinguishes
  asymptotic Gotsman-Linial bounds from the refuted exact extremizer proposal.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# One-sided stationary coupling and weighted cube edge recovery

## Source manuscript and claim

[Average sensitivity of polynomial threshold functions](../papers/P-000116.md), by OpenAI, September 25, 2026.

The source claims average sensitivity at most 8d sqrt(n) for every real degree-at-most-d polynomial threshold function on the uniform n-cube, assigning positive sign at zero.

## Extracted instruments

- [MI-000190: An equal-marginal one-sided displacement bound controls mean squared motion](../instruments/MI-000190.md)
- [MI-000191: Weighted polynomial grades recover cube edges through an anticommutator](../instruments/MI-000191.md)

## Dependencies and antecedents

An increasing quadratic primitive; equal-marginal cancellation; weighted polynomial filtration; coordinate tridiagonality; parity conjugation; Hilbert-Schmidt block norms; reflected binomial marginals.

Rollin replaces exchangeability by equality of distributions through primitive differences in Stein methods. Xu develops discrete multivariate orthogonal polynomial grading. The source distinguishes asymptotic Gotsman-Linial bounds from the refuted exact extremizer proposal. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the coupling, weighted grading, edge-recovery and parity-coupling proofs. The finite matrix checks exercise their identities and are not an independent all-dimensional certification of the headline result.

GotsmanLinial.lean states the 8d sqrt(n) uniform-cube bound for multilinear real polynomials, 1<=d<=n, with sign zero equal to one. It does not identify exact extremizers. Scope documents and Comparator statements were compared. No Lean solution was built or kernel-checked, and the extracted auxiliary results are not separately certified Comparator targets.

The coupling needs equal distributions, not independence or exchangeability. The grading weight must be strictly positive. A small positive shift preserves threshold signs and removes zeros before setting w=|p|.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/127.md) · [Batch record](../../batches/B011/README.md)

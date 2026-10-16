---
id: openai-math-126
record_type: family
title: Orthogonal PSD splitting and symmetry-amplified local averaging
source_family: '126'
source_collection: openai/math
batch_id: B011
subject: Theoretical computer science
source_paper_ids:
- P-000115
instrument_ids:
- MI-000188
- MI-000189
headline: The source claims exponential real PSD rank for exactly positively shifted odd-cut matching
  matrices, for every fixed shift strictly between zero and one, and exponential size for exact affine
  semidefinite lifts of the perfect-matching polytope.
central_instrument: Recursive spectral cuts turn small PSD overlaps into nearly separated orthogonal blocks.
  A symmetric two-sample kernel turns an explicit trace estimate into dimension-independent matrix averaging.
novelty_assessment: The binary spectral discriminator, representation-multiplicity principle and scalar-to-Hilbert-space
  extension are established. The selected candidate combinations are the finite-family splitting bound
  and the matching-cell restriction channel. The full PSD-rank theorem is not certified.
formalization_summary: MatchingPSD.lean states eventual growth beyond each fixed positive real power of
  n for the unshifted slack matrix with edge and odd-cut rows. MatchingAffineLift.lean states the corresponding
  superpolynomial affine-lift bound. Neither selected declaration states the manuscript exponential bound
  for every fixed positive shift. Scope documents and Comparator statements were compared. No Lean solution
  was built or kernel-checked, and the extracted auxiliary results are not separately certified Comparator
  targets.
statement_faithfulness: Exact factorization is essential; entrywise approximation is a different problem.
  The endpoint shift one has a polynomial-size diagonal factorization and is excluded. Local cell size
  grows with fixed terminal count, before the global instance size.
dependencies: PSD trace positivity; spectral projections of matrix differences; recursive compression;
  uniform subset slices; matching-pair restrictions; exact two-sample density; binomial estimates and
  invariant eigenspace multiplicity.
antecedents: Helstrom supplies the binary spectral projection; Gowers uses a related spectral multiplicity
  principle. Cone factorization and the sums-of-squares approach to SDP lower bounds are established background,
  distinct from the selected auxiliary estimates.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Orthogonal PSD splitting and symmetry-amplified local averaging

## Source manuscript and claim

[Exponential PSD rank of positively shifted matching matrices](../papers/P-000115.md), by OpenAI, October 5, 2026.

The source claims exponential real PSD rank for exactly positively shifted odd-cut matching matrices, for every fixed shift strictly between zero and one, and exponential size for exact affine semidefinite lifts of the perfect-matching polytope.

## Extracted instruments

- [MI-000188: Recursive spectral cuts separate PSD matrices with a dimension-free overlap charge](../instruments/MI-000188.md)
- [MI-000189: A two-sample density and spectral multiplicity control a matching-cell averaging channel](../instruments/MI-000189.md)

## Dependencies and antecedents

PSD trace positivity; spectral projections of matrix differences; recursive compression; uniform subset slices; matching-pair restrictions; exact two-sample density; binomial estimates and invariant eigenspace multiplicity.

Helstrom supplies the binary spectral projection; Gowers uses a related spectral multiplicity principle. Cone factorization and the sums-of-squares approach to SDP lower bounds are established background, distinct from the selected auxiliary estimates. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the complete orthogonal-splitting and local-averaging proofs and the shift endpoint discussion. The product Fourier-smoothing induction, parity separating functional and global matching transfer were not audited.

MatchingPSD.lean states eventual growth beyond each fixed positive real power of n for the unshifted slack matrix with edge and odd-cut rows. MatchingAffineLift.lean states the corresponding superpolynomial affine-lift bound. Neither selected declaration states the manuscript exponential bound for every fixed positive shift. Scope documents and Comparator statements were compared. No Lean solution was built or kernel-checked, and the extracted auxiliary results are not separately certified Comparator targets.

Exact factorization is essential; entrywise approximation is a different problem. The endpoint shift one has a polynomial-size diagonal factorization and is excluded. Local cell size grows with fixed terminal count, before the global instance size.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/126.md) · [Batch record](../../batches/B011/README.md)

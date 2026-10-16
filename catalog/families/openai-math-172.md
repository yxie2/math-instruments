---
id: openai-math-172
record_type: family
title: Indefinite Gaussian smoothing with exact rational constraints
source_family: '172'
source_collection: openai/math
batch_id: B044
subject: Combinatorics
source_paper_ids:
- P-000249
instrument_ids:
- MI-000460
- MI-000461
headline: The source claims a classification of finite Euclidean Ramsey configurations.
central_instrument: A positive covariance path integrates an indefinite heat operator into a difference
  of Gaussian densities. Convolution keeps quotient cancellations and moments exact through discretization
  and rational approximation.
novelty_assessment: Gaussian differentiation, Schur complements, convolution moments and rational density
  are classical. Their constraint-preserving combination is the extracted interface; no priority claim.
formalization_summary: Read the scope document and EuclideanRamsey.lean in full. The classification target
  contains sorry. Six companion Comparators were acquired but not inspected; their stated scope is not
  proof verification. No Lean build.
statement_faithfulness: C may be indefinite, but U C U transpose must equal I. Rationalize the convolution
  input, not the constrained output, and preserve a strict inequality margin.
dependencies: Schur complements, Gaussian covariance differentiation, weighted cutoff estimates, signed
  convolution moments and rational approximation in finite support.
antecedents: Classical Gaussian heat identities and exact moment-preserving convolution.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Indefinite Gaussian smoothing with exact rational constraints

## Source manuscript and claim

[A classification of finite Euclidean Ramsey configurations](../papers/P-000249.md), by OpenAI, September 23, 2026.

The source claims a classification of finite Euclidean Ramsey configurations.

## Extracted instruments

- [MI-000460: Smooth an indefinite second-order operator with small projected negative mass](../instruments/MI-000460.md)
- [MI-000461: Rationalize a convolution input while retaining exact cancellations and moments](../instruments/MI-000461.md)

## Dependencies and antecedents

Schur complements, Gaussian covariance differentiation, weighted cutoff estimates, signed convolution moments and rational approximation in finite support.

Classical Gaussian heat identities and exact moment-preserving convolution. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the complete two-scale, smoothing and rational-weights proofs. The tensor stencil and Ramsey classification arguments were not audited.

Read the scope document and EuclideanRamsey.lean in full. The classification target contains sorry. Six companion Comparators were acquired but not inspected; their stated scope is not proof verification. No Lean build.

C may be indefinite, but U C U transpose must equal I. Rationalize the convolution input, not the constrained output, and preserve a strict inequality margin.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/172.md) · [Batch record](../../batches/B044/README.md)

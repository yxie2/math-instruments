---
id: openai-math-280
record_type: family
title: Dense preimages and positivity from polynomial moments
source_family: '280'
source_collection: openai/math
batch_id: B043
subject: Mathematical physics
source_paper_ids:
- P-000243
instrument_ids:
- MI-000448
- MI-000449
headline: The source claims strong locality, unitary modules and complete rationality for strongly rational
  unitary VOAs.
central_instrument: An annulus factorization identifies a dense preimage domain. Positivity against all
  polynomial squares recovers individual complex atomic masses under an exponential moment.
novelty_assessment: The first lemma is explicitly Henriques-Tener Lemma 7.9. The second is a classical
  moment-determinacy mechanism. No independent priority claim.
formalization_summary: Read the scope document and selected VertexAlgebraNet definitions and main target.
  The target has sorry and concerns only the first construction step; modules and complete rationality
  are outside its stated scope. No Lean build.
statement_faithfulness: A preimage domain need not be the domain of a globally bounded inverse. Moment
  positivity requires all polynomials and the exponential-moment hypothesis.
dependencies: Injective bounded annulus operators, dense finite-energy subspaces, Laplace analyticity
  and uniqueness of Fourier transforms.
antecedents: Henriques-Tener, Every conformal net has an associated unitary VOA, Lemma 7.9; classical
  polynomial-density arguments for moment measures.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Dense preimages and positivity from polynomial moments

## Source manuscript and claim

[Strongly rational unitary vertex operator algebras and conformal nets](../papers/P-000243.md), by OpenAI, September 25, 2026.

The source claims strong locality, unitary modules and complete rationality for strongly rational unitary VOAs.

## Extracted instruments

- [MI-000448: Use a heat factorization to identify a dense preimage domain](../instruments/MI-000448.md)
- [MI-000449: Recover atomic positivity from every polynomial-square moment](../instruments/MI-000449.md)

## Dependencies and antecedents

Injective bounded annulus operators, dense finite-energy subspaces, Laplace analyticity and uniqueness of Fourier transforms.

Henriques-Tener, Every conformal net has an associated unitary VOA, Lemma 7.9; classical polynomial-density arguments for moment measures. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the complete annulus range and positive-moments lemmas. The fusion construction, positivity identity and sector-exhaustion arguments were not audited.

Read the scope document and selected VertexAlgebraNet definitions and main target. The target has sorry and concerns only the first construction step; modules and complete rationality are outside its stated scope. No Lean build.

A preimage domain need not be the domain of a globally bounded inverse. Moment positivity requires all polynomials and the exponential-moment hypothesis.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/280.md) · [Batch record](../../batches/B043/README.md)

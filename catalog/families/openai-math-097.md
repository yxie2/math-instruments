---
id: openai-math-097
record_type: family
title: Adaptive spectral signing and contraction-canceling predictors
source_family: 097
source_collection: openai/math
batch_id: B004
subject: Convex and metric geometry
source_paper_ids:
- P-000092
instrument_ids:
- MI-000140
- MI-000141
headline: The source claims one signing controlling all prescribed-order Euclidean prefixes by C sqrt(d),
  independent of sequence length, and derives the same-order zero-sum rearrangement bound by established
  transference.
central_instrument: Diagonal Dirichlet-energy bounds support bounded adaptive shifts; a causal predictor
  then exactly cancels each contraction while paying a telescoping column-energy cost.
novelty_assessment: The density and symmetrization approach has explicit September 2026 antecedents. Bounded
  adaptive shifts and their filtered-path assembly are candidate extensions. No full proof or priority
  certification is claimed.
formalization_summary: SteinitzBergstrom quantifies over finite indexed vector sequences, including repeated
  and zero vectors, with one absolute constant for signed prescribed prefixes and unsigned zero-sum rearrangements.
  It is existential and does not assert an online algorithm. No Lean solution was built.
statement_faithfulness: A single signing controls every prefix. The construction can use the whole input.
  The predictor argument depends on the separately proved length-independent Dirichlet-energy estimate
  for filtered path bodies.
dependencies: Convex separation of coordinate energies, Sobolev compactness, lifted Steiner symmetrization,
  Dirichlet-energy convexity under Minkowski averaging, filtered-path energy estimates and rank-one contraction
  identities.
antecedents: Guo–Fang–Lu introduce the directional-density geometric transform; Bandeira and Akbas–Sra
  develop related Dirichlet-energy formulations. Chobanyan transference supplies the signs-to-ordering
  implication.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Adaptive spectral signing and contraction-canceling predictors

## Source manuscript and claim

[The Euclidean Steinitz–Bergström theorem](../papers/P-000092.md), by OpenAI, September 24, 2026.

The source claims one signing controlling all prescribed-order Euclidean prefixes by C sqrt(d), independent of sequence length, and derives the same-order zero-sum rearrangement bound by established transference.

## Extracted instruments

- [MI-000140: Diagonal spectral energy supports signs with bounded adaptive shifts](../instruments/MI-000140.md)
- [MI-000141: Causal predictor columns cancel rank-one contractions at a telescoping energy cost](../instruments/MI-000141.md)

## Dependencies and antecedents

Convex separation of coordinate energies, Sobolev compactness, lifted Steiner symmetrization, Dirichlet-energy convexity under Minkowski averaging, filtered-path energy estimates and rank-one contraction identities.

Guo–Fang–Lu introduce the directional-density geometric transform; Bandeira and Akbas–Sra develop related Dirichlet-energy formulations. Chobanyan transference supplies the signs-to-ordering implication. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the simultaneous-density and shifted-section proofs and the complete predictor assembly. Checked constants, adaptive quantifiers, telescoping columns and feedback cancellation. The long matrix variation and Brownian survival arguments proving the filtered-body energy estimate were not fully audited.

SteinitzBergstrom quantifies over finite indexed vector sequences, including repeated and zero vectors, with one absolute constant for signed prescribed prefixes and unsigned zero-sum rearrangements. It is existential and does not assert an online algorithm. No Lean solution was built.

A single signing controls every prefix. The construction can use the whole input. The predictor argument depends on the separately proved length-independent Dirichlet-energy estimate for filtered path bodies.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/097.md) · [Batch record](../../batches/B004/README.md)

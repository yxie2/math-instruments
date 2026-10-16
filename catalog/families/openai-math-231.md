---
id: openai-math-231
record_type: family
title: Uniform posterior response and equivariant sampling of forests
source_family: '231'
source_collection: openai/math
batch_id: B005
subject: Probability and statistical mechanics
source_paper_ids:
- P-000093
instrument_ids:
- MI-000142
- MI-000143
headline: The source constructs one Borel, root-free rule sampling the free uniform spanning forest from
  vertex IID labels on every infinite connected locally finite simple unweighted graph, and extends the
  method to invariant strongly Rayleigh laws on countable groups.
central_instrument: A finite covariance-row bound supplies an everywhere-defined infinite-volume drift;
  deterministic Picard inversion of Brownian innovations recovers the target law.
novelty_assessment: The strongly Rayleigh covariance bound and innovation identity are established inputs.
  The source-specific combination is the canonical drift and sampling construction on an unrestricted
  countable product path space. Priority of these formulations is not certified.
formalization_summary: The FreeUniformSpanningForest Comparator specifies one Borel rule equivariant for
  every relabeling and every label input, with the forest law on all infinite connected locally finite
  coded graphs. StronglyRayleighDPP also targets countable-group IID factors and determinantal positive-contraction
  kernels without a trace-class or amenability hypothesis. Statements were inspected; no Lean build was
  run.
statement_faithfulness: The construction is a measurable factor, with no finite coding radius or runtime
  bound. The drift estimate controls bounded differences between fields; the fields themselves need not
  be bounded.
dependencies: Weighted matrix-tree differentiation and negative dependence; finite-field weak limits;
  martingale convergence and Brownian innovations; deterministic Picard iteration on a countable product;
  integer-time slope recovery.
antecedents: The covariance estimate is explicitly present in Alishahi, Barzegar and Zamani, with earlier
  input from Ghosh, Liggett and Pemantle. Brownian posterior sampling and infinite-dimensional Ising factors
  have precedents in stochastic localization and Nam, Sly and Zhang.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Uniform posterior response and equivariant sampling of forests

## Source manuscript and claim

[The free uniform spanning forest is a factor of IID](../papers/P-000093.md), by OpenAI, September 25, 2026.

The source constructs one Borel, root-free rule sampling the free uniform spanning forest from vertex IID labels on every infinite connected locally finite simple unweighted graph, and extends the method to invariant strongly Rayleigh laws on countable groups.

## Extracted instruments

- [MI-000142: Finite response bounds extend by limsup to a canonical infinite-volume drift](../instruments/MI-000142.md)
- [MI-000143: Picard inversion on the full product path space gives a Brownian sampler](../instruments/MI-000143.md)

## Dependencies and antecedents

Weighted matrix-tree differentiation and negative dependence; finite-field weak limits; martingale convergence and Brownian innovations; deterministic Picard iteration on a countable product; integer-time slope recovery.

The covariance estimate is explicitly present in Alishahi, Barzegar and Zamani, with earlier input from Ghosh, Liggett and Pemantle. Brownian posterior sampling and infinite-dimensional Ising factors have precedents in stochastic localization and Nam, Sly and Zhang. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the finite response, canonical drift, posterior, innovations and deterministic decoder arguments, and the strongly Rayleigh response proof. Selected finite checks cover covariance algebra and Picard majorants. The full graph coding and all determinantal supplements were not separately audited.

The FreeUniformSpanningForest Comparator specifies one Borel rule equivariant for every relabeling and every label input, with the forest law on all infinite connected locally finite coded graphs. StronglyRayleighDPP also targets countable-group IID factors and determinantal positive-contraction kernels without a trace-class or amenability hypothesis. Statements were inspected; no Lean build was run.

The construction is a measurable factor, with no finite coding radius or runtime bound. The drift estimate controls bounded differences between fields; the fields themselves need not be bounded.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/231.md) · [Batch record](../../batches/B005/README.md)

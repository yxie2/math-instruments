---
id: openai-math-139
record_type: family
title: Query-preserving Gaussian absorption and stationary mean flows
source_family: '139'
source_collection: openai/math
batch_id: B024
subject: Theoretical computer science
source_paper_ids:
- P-000169
instrument_ids:
- MI-000300
- MI-000301
headline: For normalized C2 potentials with Hessian between I and 2I, the source claims exact value-and-gradient
  oracle query complexity at most C_epsilon d^epsilon for every epsilon>0, and at least c log d, for total-variation
  error 0.1.
central_instrument: Compensate Gaussian noise added to a query center by reducing seed covariance along
  a translation direction. A weighted-divergence identity turns a generalized Stein kernel into an invariant
  flow and an exact mean-shift law.
novelty_assessment: Gaussian covariance compensation and skew-flow invariance have established antecedents.
  The cards isolate the source query identity and conditional mean-flow construction without certifying
  its compiler or global complexity bound.
formalization_summary: Read the scope and full LogConcaveQuery.lean Comparator. The oracle is exact and
  adaptive; its complexity cap holds on every execution. Arithmetic and bit costs are not charged. The
  subpolynomial upper bound is not a polylogarithmic upper bound. These are inspected target statements
  with sorry placeholders; no Lean solution was built or kernel-checked.
statement_faithfulness: The center-shift identity must preserve physical oracle queries for every fixed
  seed. The stationary flow assumes a kernel and an exact initial law and contains the unknown mean, so
  it is an ideal comparison object rather than an implementable sampler by itself.
dependencies: Gaussian linear algebra, deterministic query translation, weighted divergence, complete
  ODE flows and change of variables. Quantitative kernel construction uses additional transport and jet
  bounds.
antecedents: Classical Gaussian covariance compensation; generalized Stein identities; Ma-Chen-Fox skew-symmetric
  stationary-flow construction.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Query-preserving Gaussian absorption and stationary mean flows

## Source manuscript and claim

[Subpolynomial query complexity for well-conditioned log-concave sampling](../papers/P-000169.md), by OpenAI, September 26, 2026.

For normalized C2 potentials with Hessian between I and 2I, the source claims exact value-and-gradient oracle query complexity at most C_epsilon d^epsilon for every epsilon>0, and at least c log d, for total-variation error 0.1.

## Extracted instruments

- [MI-000300: Absorb Gaussian center noise while preserving physical oracle queries](../instruments/MI-000300.md)
- [MI-000301: A weighted-divergence kernel gives a stationary flow with an exact mean shift](../instruments/MI-000301.md)

## Dependencies and antecedents

Gaussian linear algebra, deterministic query translation, weighted divergence, complete ODE flows and change of variables. Quantitative kernel construction uses additional transport and jet bounds.

Classical Gaussian covariance compensation; generalized Stein identities; Ma-Chen-Fox skew-symmetric stationary-flow construction. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the complete compiler-absorption and stationary-flow proofs and the displayed kernel construction. The transport/jet estimates supplying the kernel, adaptive compiler accuracy theorem and oracle lower bound were not audited.

Read the scope and full LogConcaveQuery.lean Comparator. The oracle is exact and adaptive; its complexity cap holds on every execution. Arithmetic and bit costs are not charged. The subpolynomial upper bound is not a polylogarithmic upper bound. These are inspected target statements with sorry placeholders; no Lean solution was built or kernel-checked.

The center-shift identity must preserve physical oracle queries for every fixed seed. The stationary flow assumes a kernel and an exact initial law and contains the unknown mean, so it is an ideal comparison object rather than an implementable sampler by itself.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/139.md) · [Batch record](../../batches/B024/README.md)

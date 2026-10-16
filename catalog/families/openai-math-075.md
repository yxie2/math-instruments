---
id: openai-math-075
record_type: family
title: Positive thermal Fourier coefficients and marginal-constrained entropy minimization
source_family: '075'
source_collection: openai/math
batch_id: B032
subject: Real and complex analysis
source_paper_ids:
- P-000200
instrument_ids:
- MI-000362
- MI-000363
headline: The source claims almost-everywhere convergence of all symmetric Fourier partial sums for every
  complex-valued L log L function on the circle.
central_instrument: Positive Fourier expansions and a squared two-copy covariance identity give thermal
  monotonicity. A finite Gibbs dual constructs correlated letters with prescribed marginals while retaining
  both correlation cost and noisy-sum information.
novelty_assessment: Thermal monotonicity belongs to the classical Griffiths-Ginibre method. Gibbs variational
  duality and marginal multipliers are established tools. The selected combined cost is useful, but no
  first-priority claim or full Fourier-convergence certification is made.
formalization_summary: 'Read FourierLLogL.lean: full symmetric partial sums converge to f outside one
  measurable null set under integrability of |f|log(2+|f|). Its target contains sorry; no Lean build was
  performed.'
statement_faithfulness: Thermal coefficients are nonnegative and only nonnegative form increments are
  ordered. The variational hypothesis holds for every single-letter probability law on S; the constructed
  letters may be correlated and are not claimed independent.
dependencies: Absolutely convergent Fourier series, torus Haar invariance, positive covariance, finite
  convex duality, conditional entropy and permutation symmetrization.
antecedents: Griffiths-Ginibre correlation method, discussed in Benassi-Lees-Ueltschi 2016; classical
  Gibbs variational principle and entropy minimization.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Positive thermal Fourier coefficients and marginal-constrained entropy minimization

## Source manuscript and claim

[Almost-everywhere Fourier convergence in L log L](../papers/P-000200.md), by OpenAI, September 23, 2026.

The source claims almost-everywhere convergence of all symmetric Fourier partial sums for every complex-valued L log L function on the circle.

## Extracted instruments

- [MI-000362: Order thermal forms using positive Fourier coefficients and a covariance square](../instruments/MI-000362.md)
- [MI-000363: Construct correlated letters with fixed marginals and a controlled noisy-sum cost](../instruments/MI-000363.md)

## Dependencies and antecedents

Absolutely convergent Fourier series, torus Haar invariance, positive covariance, finite convex duality, conditional entropy and permutation symmetrization.

Griffiths-Ginibre correlation method, discussed in Benassi-Lees-Ueltschi 2016; classical Gibbs variational principle and entropy minimization. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the complete thermal positivity proof, prescribed-marginal variational proof and block-gluing proof. The global entropy-compression search, spectral update, live budgets and delayed-transform convergence argument were not audited.

Read FourierLLogL.lean: full symmetric partial sums converge to f outside one measurable null set under integrability of |f|log(2+|f|). Its target contains sorry; no Lean build was performed.

Thermal coefficients are nonnegative and only nonnegative form increments are ordered. The variational hypothesis holds for every single-letter probability law on S; the constructed letters may be correlated and are not claimed independent.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/075.md) · [Batch record](../../batches/B032/README.md)

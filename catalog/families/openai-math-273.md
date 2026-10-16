---
id: openai-math-273
record_type: family
title: Entropy photon-number comparison through diagonal-form interpolation
source_family: '273'
source_collection: openai/math
batch_id: B002
subject: Mathematical physics
source_paper_ids:
- P-000083
instrument_ids:
- MI-000119
- MI-000120
headline: The source claims the entropy photon-number inequality for arbitrary independent finite-energy
  bosonic inputs with any finite number of modes, allowing entanglement within each input.
central_instrument: Four-weight interpolation via a Stieltjes representation, together with moment-controlled
  Gibbs regularization.
novelty_assessment: candidate interpolation combination; Gibbs regularity is a specialized auxiliary lemma,
  with historical novelty unresolved
formalization_summary: EntropyPhotonNumber Comparator statement and scope document inspected; no Lean
  build performed.
statement_faithfulness: Selected Comparator includes independent inputs, finite mean energy and a finite
  positive number of modes; channel-capacity consequences are outside that statement.
dependencies: Parallel sums and operator means; Herglotz/Stieltjes representation; Gibbs variational principle;
  energy-constrained entropy continuity; the full EPnI argument additionally uses minimum-specific Hessian
  and stationarity identities.
antecedents: Guha--Erkmen--Shapiro EPnI formulation; Kubo--Ando operator means; one-mode variational Gaussian
  optimizer results.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Entropy photon-number comparison through diagonal-form interpolation

## Source manuscript and claim

[The entropy photon-number inequality](../papers/P-000083.md), by OpenAI, September 24, 2026.

The source claims the entropy photon-number inequality for arbitrary independent finite-energy bosonic inputs with any finite number of modes, allowing entanglement within each input.

## Extracted instruments

- [MI-000119: Four diagonal-form comparisons interpolate to a thermal hyperbolic weight](../instruments/MI-000119.md)
- [MI-000120: Fourth-moment Gibbs regularization supplies seventh-moment control](../instruments/MI-000120.md)

## Dependencies and antecedents

Parallel sums and operator means; Herglotz/Stieltjes representation; Gibbs variational principle; energy-constrained entropy continuity; the full EPnI argument additionally uses minimum-specific Hessian and stationarity identities.

Guha--Erkmen--Shapiro EPnI formulation; Kubo--Ando operator means; one-mode variational Gaussian optimizer results. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Inspected the interpolation construction and Gibbs regularity proof, including singular parameter limits and moment exponents. The full infinite-dimensional minimization and limiting EPnI proof were not independently verified.

EntropyPhotonNumber Comparator statement and scope document inspected; no Lean build performed.

Selected Comparator includes independent inputs, finite mean energy and a finite positive number of modes; channel-capacity consequences are outside that statement.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/273.md) · [Batch record](../../batches/B002/README.md)

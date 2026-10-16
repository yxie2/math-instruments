---
id: openai-math-083
record_type: family
title: Compensated random thinning and probability changes that retain a small error
source_family: 083
source_collection: openai/math
batch_id: B023
subject: Real and complex analysis
source_paper_ids:
- P-000164
instrument_ids:
- MI-000290
- MI-000291
headline: The source claims a universal L2 bound for each short hard-truncated Hilbert transform along
  a Lipschitz unit vector field in the plane, with both-coordinate dependence allowed, and a bounded principal-value
  extension.
central_instrument: Exponential-clock thinning selects separated indices and matches its inverse-probability
  cost to coefficient powers. A lower-deviation bound allows a change from a Fourier-supported probability
  to uniform measure with error proportional to the relative mass drop.
novelty_assessment: Random local-minimum independent sets and inverse-probability reconstruction are established
  methods. The mixture estimate is elementary. The source-specific matching of these ingredients to an
  analytic hierarchy is isolated without certifying the full Hilbert-transform theorem.
formalization_summary: Read LipschitzHilbert.lean, including the fixed short-scale hard-truncation, Schwartz
  principal-value, weak-(2,2), bounded-extension and reciprocal-Lipschitz-scale targets. The latter permits
  R<=1/(1000000 K). These are inspected target statements with sorry placeholders; no Lean solution was
  built or kernel-checked.
statement_faithfulness: The truncation supremum is outside the L2 norm, not a maximal-truncation estimate.
  A field direction is frozen at the output point. Retention indicators are dependent, and the finite
  Fourier estimate for each retained set is a separate input.
dependencies: Independent exponential clocks, weighted local-minimum selection, inverse inclusion probabilities,
  Minkowski and concave Jensen, probability mixtures and logarithmic blending.
antecedents: Caro-Wei/Boppana local-minimum selection; classical inverse-probability weighting; elementary
  probability domination and concavity of log.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Compensated random thinning and probability changes that retain a small error

## Source manuscript and claim

[A uniform Hilbert transform estimate for Lipschitz directions](../papers/P-000164.md), by OpenAI, September 25, 2026.

The source claims a universal L2 bound for each short hard-truncated Hilbert transform along a Lipschitz unit vector field in the plane, with both-coordinate dependence allowed, and a bounded principal-value extension.

## Extracted instruments

- [MI-000290: Exponential-clock thinning cancels its own inverse-probability cost](../instruments/MI-000290.md)
- [MI-000291: A small lower deficit prevents a fixed loss when changing probabilities](../instruments/MI-000291.md)

## Dependencies and antecedents

Independent exponential clocks, weighted local-minimum selection, inverse inclusion probabilities, Minkowski and concave Jensen, probability mixtures and logarithmic blending.

Caro-Wei/Boppana local-minimum selection; classical inverse-probability weighting; elementary probability domination and concavity of log. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the clock-selection calculation, complete Fourier-supported averaging proof, logarithmic blending and change-of-probability argument. The finite Fourier estimate, snapshot-motion bounds and integrated path theorem were not audited.

Read LipschitzHilbert.lean, including the fixed short-scale hard-truncation, Schwartz principal-value, weak-(2,2), bounded-extension and reciprocal-Lipschitz-scale targets. The latter permits R<=1/(1000000 K). These are inspected target statements with sorry placeholders; no Lean solution was built or kernel-checked.

The truncation supremum is outside the L2 norm, not a maximal-truncation estimate. A field direction is frozen at the output point. Retention indicators are dependent, and the finite Fourier estimate for each retained set is a separate input.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/083.md) · [Batch record](../../batches/B023/README.md)

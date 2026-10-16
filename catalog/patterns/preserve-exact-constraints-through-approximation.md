---
id: PAT-012
record_type: pattern
title: Preserve exact constraints through approximation
batch_id: B045
instrument_ids: [MI-000419, MI-000432, MI-000438, MI-000445, MI-000447, MI-000461]
updated: '2026-10-16'
---

# Preserve exact constraints through approximation

[Pattern index](README.md) · [Research guide](../../methodology/research-guide.md)

Approximation becomes useful only if the final object still satisfies the equations needed later. These instruments arrange that preservation before taking a limit, choosing representatives or reducing coefficients.

| Mechanism | What remains exact | Hypothesis that enables it |
| --- | --- | --- |
| [Convolution before rational approximation](../instruments/MI-000461.md) | Quotient cancellations and second moments | Rational finite stencil with zero mass and first moment; a strict inequality margin |
| [Homology projection adapted to one subspace](../instruments/MI-000438.md) | Chain homotopy and preservation of the chosen subspace | A finite graded complex over a field; compatible choices of complements |
| [Cutoff implementation in a hereditary corner](../instruments/MI-000432.md) | The prescribed square and simultaneous algebra transport | Positive cutoff and the stated Cuntz comparison |
| [Graded lifting from a special fiber](../instruments/MI-000419.md) | The whole algebra identification | Surjectivity, flat target and a kernel bounded below in degree |
| [Localized lattice saturation](../instruments/MI-000445.md) | Integral intersection with a rational span | Independent reductions modulo the residual prime |
| [Integral character evaluation](../instruments/MI-000447.md) | Stable lattices and common residual modules | Freeness over the integral group ring before specialization |

These are different theorems, not instances of one proved general result. Their common research prompt is concrete: identify the exact equations, then parameterize the construction so those equations hold throughout. Approximate the remaining free parameters. In the convolution example, rounding the output weights can destroy cancellation; rounding the convolution input preserves it automatically.

A proposed next use is a rational certificate for a new constrained moment problem. One would need to construct the appropriate annihilating stencil, obtain a strict analytic margin and check that the desired constraints are among the preserved pushforwards. This catalogue does not record that application as completed.

The linked cards give source labels, antecedents and verification limits. This pattern is a synthesis of their interfaces, not a novelty claim or a verification of the source headline theorems.

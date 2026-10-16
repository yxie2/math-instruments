---
id: openai-math-354
record_type: family
title: Turn slice averages and finite parameter tables into uniform bounds
source_family: '354'
source_collection: openai/math
batch_id: B029
subject: Differential geometry
source_paper_ids:
- P-000190
instrument_ids:
- MI-000342
- MI-000343
headline: The source claims the full isoperimetric profile and all minimizers of the unit cubic flat three-torus,
  including both equality classes at the ball-tube and tube-slab transitions.
central_instrument: A convex scalar function turns an arclength-mean flux identity into a slice inequality.
  An upper second-derivative bound turns certified knot values into uniform positivity between knots.
novelty_assessment: Jensen, monotone minorants, outward interval arithmetic and chord-error bounds are
  established tools. The source chooses concrete functions and a rational certificate; the selected arithmetic
  is checked conditionally on its endpoint and analytic derivative bounds.
formalization_summary: Read CubicTorus.lean and its scope. It uses the unit flat quotient torus, De Giorgi
  perimeter for arbitrary finite-perimeter regions, null-set equivalence, attainment, and all equality
  cases at 4pi/81 and 1/pi, including complements. The inspected Comparator contains a sorry target, not
  a proof built or kernel-checked here.
statement_faithfulness: Flux fixes an arclength average, not pointwise inclination. The interpolation
  certificate uses an upper bound on the second derivative to prove a lower bound between endpoints. The
  endpoint table and analytic curvature bounds remain separate inputs.
dependencies: Jensen convexity, a nonincreasing minorant, coarea, scalar concavity after subtracting a
  quadratic and rational outward arithmetic.
antecedents: Classical Jensen and coarea methods; elementary rigorous interpolation and interval arithmetic.
  No first-priority claim established for the source scalar choices.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Turn slice averages and finite parameter tables into uniform bounds

## Source manuscript and claim

[The Isoperimetric Conjecture for the Cubic Flat Three-Torus](../papers/P-000190.md), by OpenAI, September 24, 2026.

The source claims the full isoperimetric profile and all minimizers of the unit cubic flat three-torus, including both equality classes at the ball-tube and tube-slab transitions.

## Extracted instruments

- [MI-000342: Use a convex flux defect instead of substituting a mean pointwise](../instruments/MI-000342.md)
- [MI-000343: Certify positivity between rational knots using an upper curvature bound](../instruments/MI-000343.md)

## Dependencies and antecedents

Jensen convexity, a nonincreasing minorant, coarea, scalar concavity after subtracting a quadratic and rational outward arithmetic.

Classical Jensen and coarea methods; elementary rigorous interpolation and interval arithmetic. No first-priority claim established for the source scalar choices. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the complete integrated-flux proof and the outward-arithmetic/interpolation section. The geometric reduction, endpoint transcendental evaluations, analytic second-derivative bounds and final equality classification were not audited.

Read CubicTorus.lean and its scope. It uses the unit flat quotient torus, De Giorgi perimeter for arbitrary finite-perimeter regions, null-set equivalence, attainment, and all equality cases at 4pi/81 and 1/pi, including complements. The inspected Comparator contains a sorry target, not a proof built or kernel-checked here.

Flux fixes an arclength average, not pointwise inclination. The interpolation certificate uses an upper bound on the second derivative to prove a lower bound between endpoints. The endpoint table and analytic curvature bounds remain separate inputs.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/354.md) · [Batch record](../../batches/B029/README.md)

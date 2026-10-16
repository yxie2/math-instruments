---
id: openai-math-069
record_type: family
title: Kummer inertia vanishing and bounded-weight tail detection
source_family: 069
source_collection: openai/math
batch_id: B046
subject: Algebraic and complex geometry
source_paper_ids:
- P-000254
instrument_ids:
- MI-000470
- MI-000471
headline: The source claims global quantum geometric Langlands at irrational level.
central_instrument: Nonintegral Kummer monodromy forces a central-inertia category to vanish. A uniform
  upper weight bound promotes vanishing modulo a finite logarithm length to vanishing of completed generators.
novelty_assessment: Euler-operator acyclicity and strict weight arguments are classical. The source geometric
  and categorical inputs remain separate; no equivalence or priority certification.
formalization_summary: No formalization scope document is listed for this family in the pinned inventory.
  No Lean build.
statement_faithfulness: Vanishing of a filtered colimit at one parameter does not imply finite-stage vanishing.
  Completed finite generation, compatible homogeneous lifts and a uniform target weight bound are required
  for the extracted tail argument.
dependencies: Strong Kummer equivariance, Laurent de Rham complexes, conservative pullback, completed
  finite modules, strict weight maps and finite generation.
antecedents: Classical Kummer acyclicity, Nakayama and strictness of mixed Hodge structures.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Kummer inertia vanishing and bounded-weight tail detection

## Source manuscript and claim

[Global quantum geometric Langlands at irrational level](../papers/P-000254.md), by OpenAI, October 4, 2026.

The source claims global quantum geometric Langlands at irrational level.

## Extracted instruments

- [MI-000470: Use nonintegral inertia to force a twisted category to vanish](../instruments/MI-000470.md)
- [MI-000471: Kill completed generators using a uniform weight gap](../instruments/MI-000471.md)

## Dependencies and antecedents

Strong Kummer equivariance, Laurent de Rham complexes, conservative pullback, completed finite modules, strict weight maps and finite generation.

Classical Kummer acyclicity, Nakayama and strictness of mixed Hodge structures. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the complete inertia, non-torsion rank and logarithm-colimit proofs. Extracted only the elementary inertia calculation and the conditional bounded-weight killing step; geometric perfectness, rank constancy and the global equivalence were not independently verified.

No formalization scope document is listed for this family in the pinned inventory. No Lean build.

Vanishing of a filtered colimit at one parameter does not imply finite-stage vanishing. Completed finite generation, compatible homogeneous lifts and a uniform target weight bound are required for the extracted tail argument.

[Batch record](../../batches/B046/README.md)

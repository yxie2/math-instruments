---
id: openai-math-166
record_type: family
title: Distance separators and interpolation through nonreduced points
source_family: '166'
source_collection: openai/math
batch_id: B036
subject: Combinatorics
source_paper_ids:
- P-000217
instrument_ids:
- MI-000396
- MI-000397
headline: The source claims the higher-dimensional Erdos distinct-distances lower bound.
central_instrument: Distance polynomials give explicit point separators and exact defining equations.
  A local Artin-algebra determinant replaces the Jacobian when isolating singular points.
novelty_assessment: Polynomial separation, Bezout, complete-intersection socles and Hermite interpolation
  are established tools. The selected source assembles useful degree-controlled interfaces; the global
  distance theorem is not audited.
formalization_summary: No formalization scope document is listed for this family in the pinned inventory.
  No Lean build was performed.
statement_faithfulness: Real point sets provide nonzero squared-distance factors, but the defining-equation
  conclusion concerns complex zeros too. General isolation allows nonreduced isolated points and other
  positive-dimensional zero components.
dependencies: Products of squared-distance factors, Bezout, regular sequences, Koszul complexes, local
  Artin quotients and coefficient functionals.
antecedents: Classical polynomial method and complete-intersection algebra; the source cites Chardin interpolation
  and standard Stacks Project regular-sequence facts.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Distance separators and interpolation through nonreduced points

## Source manuscript and claim

[The higher-dimensional Erdős distinct-distances conjecture](../papers/P-000217.md), by OpenAI, September 23, 2026.

The source claims the higher-dimensional Erdos distinct-distances lower bound.

## Extracted instruments

- [MI-000396: Build exact defining equations from squared-distance separators](../instruments/MI-000396.md)
- [MI-000397: Separate isolated singular points using a local Artin determinant](../instruments/MI-000397.md)

## Dependencies and antecedents

Products of squared-distance factors, Bezout, regular sequences, Koszul complexes, local Artin quotients and coefficient functionals.

Classical polynomial method and complete-intersection algebra; the source cites Chardin interpolation and standard Stacks Project regular-sequence facts. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the complete polynomial toolkit section, including separator, socle and isolated-point interpolation proofs. The later global incidence decomposition and distinct-distance theorem were not audited.

No formalization scope document is listed for this family in the pinned inventory. No Lean build was performed.

Real point sets provide nonzero squared-distance factors, but the defining-equation conclusion concerns complex zeros too. General isolation allows nonreduced isolated points and other positive-dimensional zero components.

[Batch record](../../batches/B036/README.md)

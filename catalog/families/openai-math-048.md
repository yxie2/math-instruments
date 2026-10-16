---
id: openai-math-048
record_type: family
title: Normalized trace pairings and volume-preserving jet corrections
source_family: 048
source_collection: openai/math
batch_id: B026
subject: Algebraic and complex geometry
source_paper_ids:
- P-000177
instrument_ids:
- MI-000316
- MI-000317
headline: The source claims a singular normal affine complex surface whose algebraic tangent module is
  free of rank two, with a single marked singular point.
central_instrument: Normalize a ramified trace pairing by the relative differential, then pass to an orthogonal
  quotient. Compute homogeneous jet corrections relative to a meromorphic volume form and isolate the
  resonant order.
novelty_assessment: Finite-morphism duality, orthogonal reduction and Lie derivative calculations are
  established. The source-specific normalizations and resonant coefficient are extracted; the claimed
  Lipman-Zariski counterexample is not certified.
formalization_summary: No family-specific scope document or Comparator target is listed for this family.
  No Lean artifact was built or kernel-checked.
statement_faithfulness: The trace is not divided by the covering degree. Evaluation norms belong to the
  dual quadratic form. Volume-preserving correction by b=hprime/(4-k) excludes k=4 and does not itself
  solve a global gluing problem.
dependencies: Relative dualizing trace, splitting of bundles on P1, isotropic orthogonal quotients, coordinate
  transformation and Lie bracket/divergence formulas.
antecedents: Grothendieck finite-morphism duality and P1 bundle splitting; classical local vector-field
  calculus.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Normalized trace pairings and volume-preserving jet corrections

## Source manuscript and claim

[A singular normal affine surface with free tangent sheaf](../papers/P-000177.md), by OpenAI, September 23, 2026.

The source claims a singular normal affine complex surface whose algebraic tangent module is free of rank two, with a single marked singular point.

## Extracted instruments

- [MI-000316: Normalize the ramified trace before taking an orthogonal quotient](../instruments/MI-000316.md)
- [MI-000317: A weighted divergence formula separates correctable jet orders from resonance](../instruments/MI-000317.md)

## Dependencies and antecedents

Relative dualizing trace, splitting of bundles on P1, isotropic orthogonal quotients, coordinate transformation and Lie bracket/divergence formulas.

Grothendieck finite-morphism duality and P1 bundle splitting; classical local vector-field calculus. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the complete trace-pairing proof, its quotient and evaluation normalization, and the complete jet bracket proof with coordinate and volume conventions. The prescribed curve, full principal parts, obstruction vanishing, analytic realization and algebraization were not audited.

No family-specific scope document or Comparator target is listed for this family. No Lean artifact was built or kernel-checked.

The trace is not divided by the covering degree. Evaluation norms belong to the dual quadratic form. Volume-preserving correction by b=hprime/(4-k) excludes k=4 and does not itself solve a global gluing problem.

[Batch record](../../batches/B026/README.md)

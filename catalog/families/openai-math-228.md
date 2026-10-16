---
id: openai-math-228
record_type: family
title: Convex limits and full support transfer under density transforms
source_family: '228'
source_collection: openai/math
batch_id: B079
subject: Probability and statistical mechanics
source_paper_ids:
- P-000496
instrument_ids:
- MI-000738
- MI-000739
headline: The family claims continuum temperature singularities for stable radial pair potentials.
central_instrument: Retain complete supporting vectors through pressure limits and a quadratic density
  transform.
novelty_assessment: Known finite mechanisms are credited separately from source headline claims. Exhaustive
  novelty is not established.
formalization_summary: ContinuumTransition targets one stable radial potential with a divergent core,
  an integrable o(r^-3) tail, and a temperature derivative jump over a density interval. It is distinct
  from the bounded-potential targets linked in the scope. Full scope and named Comparator read; other
  linked Comparators were not inspected. The target contains sorry; no separate solution or Lean build
  was checked.
statement_faithfulness: Local convex convergence is on an open convex domain with a finite limit. Joint
  support transfer assumes the density conjugate is finite and concave in inverse temperature.
dependencies: Finite-dimensional separation, local Lipschitz bounds, Fenchel equality and attainment of
  the transformed density supremum.
antecedents: Classical convex convergence, conjugacy and reachable-gradient theory.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Convex limits and full support transfer under density transforms

## Source manuscripts and claim

- [A continuum temperature singularity for a radial pair potential](../papers/P-000496.md): selected passages extracted.

The following companions are inventoried but have no extraction in this batch:

- [A radial continuum phase transition with algebraic decay](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/A-radial-continuum-phase-transition-with-algebraic-decay-September-24-2026)

The family claims continuum temperature singularities for stable radial pair potentials.

## Extracted instruments

- [MI-000738: Pass finite convex limits together with their supporting vectors](../instruments/MI-000738.md)
- [MI-000739: Transfer both coordinates of a support through a quadratic density transform](../instruments/MI-000739.md)

## Dependencies and antecedents

Finite-dimensional separation, local Lipschitz bounds, Fenchel equality and attainment of the transformed density supremum.

Classical convex convergence, conjugacy and reachable-gradient theory.

## Review and formalization scope

Read the complete convex-facts appendix and joint/quadratic support proofs. The companion is inventory-only. Potential construction and thermodynamic limits are not certified.

ContinuumTransition targets one stable radial potential with a divergent core, an integrable o(r^-3) tail, and a temperature derivative jump over a density interval. It is distinct from the bounded-potential targets linked in the scope. Full scope and named Comparator read; other linked Comparators were not inspected. The target contains sorry; no separate solution or Lean build was checked.

Local convex convergence is on an open convex domain with a finite limit. Joint support transfer assumes the density conjugate is finite and concave in inverse temperature.

[Batch record](../../batches/B079/README.md)

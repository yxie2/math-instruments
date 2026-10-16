---
id: openai-math-363
record_type: family
title: Collision geometry and stable pullback of vanishing functions
source_family: '363'
source_collection: openai/math
batch_id: B086
subject: Partial differential equations
source_paper_ids:
- P-000523
instrument_ids:
- MI-000792
- MI-000793
headline: The family claims nonuniqueness of hard-sphere Boltzmann solutions with specified conservation
  properties.
central_instrument: Track the exact collision normalization and use full-rank limiting maps to pull back
  bounded functions converging in measure.
novelty_assessment: Classical ingredients are distinguished from source-specific uses. Exact priority
  of the extracted formulations is not established.
formalization_summary: Read the full scope and BoltzmannNonuniqueness Comparator. Its target is the earlier
  periodic admissibility statement; the selected later local-conservation refinements are outside that
  scope. The target has sorry; no separate solution or Lean build was checked.
statement_faithfulness: The collision kernel uses ordinary sphere area and absolute normal relative velocity.
  Pullback densities are uniformly bounded on a common compact set; the limiting map has full rank almost
  everywhere.
dependencies: Reflection geometry, coarea, Tonelli, inverse-function charts and convergence in measure.
antecedents: Classical Carleman representations and local changes of variables near regular points.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Collision geometry and stable pullback of vanishing functions

## Source manuscripts and claim

- [Nonuniqueness with local conservation for the hard-sphere Boltzmann equation](../papers/P-000523.md): selected passages extracted.

The following companions are inventoried but have no extraction in this batch:

- [Nonuniqueness for the periodic hard-sphere Boltzmann equation](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Nonuniqueness-for-the-periodic-hard-sphere-Boltzmann-equation-September-23-2026)

The family claims nonuniqueness of hard-sphere Boltzmann solutions with specified conservation properties.

## Extracted instruments

- [MI-000792: Convert hard-sphere gain to planes with the exact normalization](../instruments/MI-000792.md)
- [MI-000793: Pull back convergence in measure through a stable almost-everywhere submersion](../instruments/MI-000793.md)

## Dependencies and antecedents

Reflection geometry, coarea, Tonelli, inverse-function charts and convergence in measure.

Classical Carleman representations and local changes of variables near regular points.

## Review and formalization scope

Read complete collision-geometry, redundant-plane-parameter and uniform-pullback proofs. One companion is inventory-only. The nonlinear construction, nonconcentration and nonuniqueness theorem are not certified.

Read the full scope and BoltzmannNonuniqueness Comparator. Its target is the earlier periodic admissibility statement; the selected later local-conservation refinements are outside that scope. The target has sorry; no separate solution or Lean build was checked.

The collision kernel uses ordinary sphere area and absolute normal relative velocity. Pullback densities are uniformly bounded on a common compact set; the limiting map has full rank almost everywhere.

[Batch record](../../batches/B086/README.md)

---
id: openai-math-150
record_type: family
title: Reflection constraints and compact spectral obstructions
source_family: '150'
source_collection: openai/math
batch_id: B076
subject: Dynamical systems and ergodic theory
source_paper_ids:
- P-000479
instrument_ids:
- MI-000710
- MI-000711
headline: The family claims ergodicity and weak mixing for every triangular billiard with an irrational
  angle.
central_instrument: After transverse rigidity, reflection identities eliminate plane-wave eigenfunctions;
  a compact integral operator converts product invariance into a forbidden eigenfunction.
novelty_assessment: Established mechanisms are credited explicitly. Selected source-specific formulations
  are extracted without an exhaustive priority claim.
formalization_summary: The linked scope and IrrationalTriangleBilliard Comparator target ergodicity, including
  actual regular flight chains, measure preservation and the flow law; they do not state weak mixing.
  The complete scope and Comparator were read. The inspected target contains sorry; no separate solution
  or Lean build was checked.
statement_faithfulness: The geometric conclusion is conditional on the local plane-wave form and crossing-chart
  compatibility. These prerequisites are not proved by the reflection argument.
dependencies: Circle Fourier series, affine reflections, strongly continuous unitary groups and compact-operator
  spectral theory.
antecedents: Classical irrational-rotation ergodicity and the spectral characterization of weak mixing.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Reflection constraints and compact spectral obstructions

## Source manuscripts and claim

- [Weak mixing of triangular billiards with an irrational angle](../papers/P-000479.md): selected passages extracted.

The following companions are inventoried but have no extraction in this batch:

- [Ergodicity of triangular billiards with an irrational angle](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Ergodicity-of-triangular-billiards-with-an-irrational-angle-September-25-2026)

The family claims ergodicity and weak mixing for every triangular billiard with an irrational angle.

## Extracted instruments

- [MI-000710: Use affine side relations to remove a plane-wave eigenfunction](../instruments/MI-000710.md)
- [MI-000711: Turn an invariant product kernel into a finite-dimensional spectral obstruction](../instruments/MI-000711.md)

## Dependencies and antecedents

Circle Fourier series, affine reflections, strongly continuous unitary groups and compact-operator spectral theory.

Classical irrational-rotation ergodicity and the spectral characterization of weak mixing.

## Review and formalization scope

Read the complete side-reflection and spectral proofs in the weak-mixing manuscript, and the spatial regularization and individual-mode arguments as context. One companion is inventory-only. The transverse rigidity argument and the headline billiard results are not certified.

The linked scope and IrrationalTriangleBilliard Comparator target ergodicity, including actual regular flight chains, measure preservation and the flow law; they do not state weak mixing. The complete scope and Comparator were read. The inspected target contains sorry; no separate solution or Lean build was checked.

The geometric conclusion is conditional on the local plane-wave form and crossing-chart compatibility. These prerequisites are not proved by the reflection argument.

[Batch record](../../batches/B076/README.md)

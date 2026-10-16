---
id: openai-math-372
record_type: family
title: Null-conic polarization bundles and finite-type uniqueness
source_family: '372'
source_collection: openai/math
batch_id: B028
subject: Partial differential equations
source_paper_ids:
- P-000184
instrument_ids:
- MI-000330
- MI-000331
headline: The source claims global uniqueness of both smooth isotropic Lame moduli in a three-dimensional
  bounded smooth connected domain from the full displacement-to-traction map.
central_instrument: An explicit null-conic frame identifies a nonsplit quotient bundle. An overdetermined
  Hessian relation closes on the gradient and one scalar, so zero data propagate along paths by ODE uniqueness.
novelty_assessment: The conic bundle calculation is an explicit form of classical projective geometry,
  and prolongation to a finite first-order system is classical. Their role in coefficient recovery is
  extracted conditionally on the source unaudited analytic transport construction.
formalization_summary: Read ElasticityUniqueness.lean and its scope. It requires smooth real moduli with
  mu>0 and 3lambda+2mu>0, and equality of the full physical DN pairing on the variational trace quotient.
  It asserts uniqueness, not reconstruction. The inspected Comparator contains a sorry placeholder; no
  Lean proof was built or kernel-checked.
statement_faithfulness: Orthogonality on the complex null conic is bilinear, not Hermitian. A trivial
  quotient does not make its exact sequence split, and vanishing global sections does not force all bundle
  endomorphisms to be scalar. The finite-type lemma needs dimension at least two.
dependencies: Homogeneous conic parametrization, tautological line bundles, compactness of P1, commutation
  of third derivatives and linear ODE uniqueness.
antecedents: Classical conic and Euler-sequence geometry; elementary finite-type prolongation of overdetermined
  differential systems.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Null-conic polarization bundles and finite-type uniqueness

## Source manuscript and claim

[Global Uniqueness for the Smooth Isotropic Elasticity Inverse Problem](../papers/P-000184.md), by OpenAI, September 24, 2026.

The source claims global uniqueness of both smooth isotropic Lame moduli in a three-dimensional bounded smooth connected domain from the full displacement-to-traction map.

## Extracted instruments

- [MI-000330: Resolve null-conic polarizations with an explicit nonsplit quotient sequence](../instruments/MI-000330.md)
- [MI-000331: Close a Hessian equation on the gradient and scalar trace ambiguity](../instruments/MI-000331.md)

## Dependencies and antecedents

Homogeneous conic parametrization, tautological line bundles, compactness of P1, commutation of third derivatives and linear ODE uniqueness.

Classical conic and Euler-sequence geometry; elementary finite-type prolongation of overdetermined differential systems. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the complete conic-bundle and finite-type uniqueness proofs. Carleman estimates, physical amplitudes, transport matching and comparison rigidity were not audited.

Read ElasticityUniqueness.lean and its scope. It requires smooth real moduli with mu>0 and 3lambda+2mu>0, and equality of the full physical DN pairing on the variational trace quotient. It asserts uniqueness, not reconstruction. The inspected Comparator contains a sorry placeholder; no Lean proof was built or kernel-checked.

Orthogonality on the complex null conic is bilinear, not Hermitian. A trivial quotient does not make its exact sequence split, and vanishing global sections does not force all bundle endomorphisms to be scalar. The finite-type lemma needs dimension at least two.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/372.md) · [Batch record](../../batches/B028/README.md)

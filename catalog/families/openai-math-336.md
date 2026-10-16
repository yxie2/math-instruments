---
id: openai-math-336
record_type: family
title: Spectral preprocessing and graph-angle linearization
source_family: '336'
source_collection: openai/math
batch_id: B084
subject: Differential geometry
source_paper_ids:
- P-000517
instrument_ids:
- MI-000780
- MI-000781
headline: The family claims codimension-two Urysohn-width estimates from scalar or spectral scalar curvature.
central_instrument: Convert a positive spectral lower bound into a logarithmic drift weight, and retain
  angle dependence when linearizing graph pressure.
novelty_assessment: Classical ingredients are identified; exact priority of the source-specific formulations
  is not established.
formalization_summary: No family scope is supplied; no Lean verification is claimed.
statement_faithfulness: The manifold is complete, connected and boundaryless; the graph-angle identity
  assumes a smooth solution of the prescribed equation.
dependencies: Positive Dirichlet ground states, Harnack compactness, elliptic regularity and normal variation.
antecedents: Classical positive-solution principles and Jacobi equations for graphs.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Spectral preprocessing and graph-angle linearization

## Source manuscripts and claim

- [Spectral scalar curvature and uniform Urysohn width](../papers/P-000517.md): selected passages extracted.

The following companions are inventoried but have no extraction in this batch:

- [Spectral scalar curvature and Urysohn width in dimension three](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Spectral-scalar-curvature-and-Urysohn-width-in-dimension-three-October-5-2026)
- [Positive scalar curvature and uniform codimension-two width](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Positive-scalar-curvature-and-uniform-codimension-two-width-September-23-2026)

The family claims codimension-two Urysohn-width estimates from scalar or spectral scalar curvature.

## Extracted instruments

- [MI-000780: Convert a spectral lower bound to a logarithmic drift weight](../instruments/MI-000780.md)
- [MI-000781: Retain angle-dependent pressure in a graph Jacobi equation](../instruments/MI-000781.md)

## Dependencies and antecedents

Positive Dirichlet ground states, Harnack compactness, elliptic regularity and normal variation.

Classical positive-solution principles and Jacobi equations for graphs.

## Review and formalization scope

Read the complete supersolution lemma and graph-angle proof. Two companions are inventory-only. The global graph construction, reserve estimates and width theorem are not certified.

No family scope is supplied; no Lean verification is claimed.

The manifold is complete, connected and boundaryless; the graph-angle identity assumes a smooth solution of the prescribed equation.

[Batch record](../../batches/B084/README.md)

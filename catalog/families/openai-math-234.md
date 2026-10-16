---
id: openai-math-234
record_type: family
title: Spectral approximation tools for invariant Ising pressure
source_family: '234'
source_collection: openai/math
batch_id: B005
subject: Probability and statistical mechanics
source_paper_ids:
- P-000094
instrument_ids:
- MI-000144
- MI-000145
headline: The source claims an all-temperature variational pressure formula for orthogonally invariant
  Ising interactions, including compact spectral laws without outliers. This extraction selects two standalone
  approximation arguments.
central_instrument: Continuity of an edge-capped inverse Stieltjes transform and a multiplicity comparison
  based on eigenspace symmetry remove regularity and arithmetic restrictions.
novelty_assessment: The R-transform and Haar interpolation framework are established. The two displayed
  approximation lemmas are candidate useful formulations; their historical priority and the global all-temperature
  formula have not been certified.
formalization_summary: InvariantIsing targets expected and almost-sure limits for deterministic spectra,
  positive temperatures and ground states, plus conditional-Haar random spectra, Gaussian patterns and
  Wasserstein-one field extensions. The target statements were inspected; no Lean solution was built.
statement_faithfulness: 'Weak convergence alone is insufficient for the selected transform-continuity
  statement: upper support edges must converge. The multiplicity estimate concerns Haar expectations and
  positive multiplicities, not arbitrary deterministic rotations or negligible-rank perturbations.'
dependencies: Inverse Stieltjes transforms with an edge cap; uniform expansion at the origin; convexity
  of log partition functions; Haar symmetry inside endpoint eigenspaces.
antecedents: Guionnet and Maida develop the R-transform and spherical-integral framework. Bhattacharya
  and Sen and Fan and Wu treat high-temperature or replica-symmetric invariant Ising pressure. The present
  extraction does not reclassify those inputs as new.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Spectral approximation tools for invariant Ising pressure

## Source manuscript and claim

[All-temperature pressure for orthogonally invariant Ising spin glasses](../papers/P-000094.md), by OpenAI, September 25, 2026.

The source claims an all-temperature variational pressure formula for orthogonally invariant Ising interactions, including compact spectral laws without outliers. This extraction selects two standalone approximation arguments.

## Extracted instruments

- [MI-000144: Weak convergence plus support-edge convergence controls the capped R-transform uniformly](../instruments/MI-000144.md)
- [MI-000145: Eigenspace symmetry bounds pressure changes caused by spectral multiplicity errors](../instruments/MI-000145.md)

## Dependencies and antecedents

Inverse Stieltjes transforms with an edge cap; uniform expansion at the origin; convexity of log partition functions; Haar symmetry inside endpoint eigenspaces.

Guionnet and Maida develop the R-transform and spherical-integral framework. Bhattacharya and Sen and Fan and Wu treat high-temperature or replica-symmetric invariant Ising pressure. The present extraction does not reclassify those inputs as new. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read both approximation lemmas in section 60-general and their full proofs. Checked the edge branch, origin expansion, and endpoint derivative symmetry. The overlap arrays, cavity limit and global variational identification were not fully audited.

InvariantIsing targets expected and almost-sure limits for deterministic spectra, positive temperatures and ground states, plus conditional-Haar random spectra, Gaussian patterns and Wasserstein-one field extensions. The target statements were inspected; no Lean solution was built.

Weak convergence alone is insufficient for the selected transform-continuity statement: upper support edges must converge. The multiplicity estimate concerns Haar expectations and positive multiplicities, not arbitrary deterministic rotations or negligible-rank perturbations.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/234.md) · [Batch record](../../batches/B005/README.md)

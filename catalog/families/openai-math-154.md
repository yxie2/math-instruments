---
id: openai-math-154
record_type: family
title: Oscillation and correlation as separate convergence tests
source_family: '154'
source_collection: openai/math
batch_id: B076
subject: Dynamical systems and ergodic theory
source_paper_ids:
- P-000480
instrument_ids:
- MI-000712
- MI-000713
headline: The family claims pointwise convergence of multiple ergodic averages for mixing transformations.
central_instrument: A deterministic-block oscillation bound proves almost-everywhere convergence; a Hilbert-space
  correlation estimate can identify the limit in norm.
novelty_assessment: Established mechanisms are credited explicitly. Selected source-specific formulations
  are extracted without an exhaustive priority claim.
formalization_summary: The pinned inventory supplies no scope document or linked Comparator for this family.
  No Lean verification is claimed.
statement_faithfulness: The oscillation bound must hold for every deterministic increasing list of block
  endpoints with one uniform constant. Correlation limits are taken with each lag fixed before the lag
  cutoff grows.
dependencies: Monotone convergence, Cauchy-Schwarz, completeness and Hilbert-space correlations.
antecedents: Classical oscillation methods and the Hilbert-space van der Corput criterion.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Oscillation and correlation as separate convergence tests

## Source manuscripts and claim

- [Triple ergodic averages with distinct integer slopes](../papers/P-000480.md): selected passages extracted.

The following companions are inventoried but have no extraction in this batch:

- [Pointwise Multiple Ergodic Averages for Mixing Transformations](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Pointwise-Multiple-Ergodic-Averages-for-Mixing-Transformations-October-4-2026)
- [Pointwise convergence of fourfold ergodic averages for mixing transformations](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Pointwise-convergence-of-fourfold-ergodic-averages-for-mixing-transformations-October-4-2026)
- [Pointwise convergence of triple ergodic averages for mixing transformations](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Pointwise-convergence-of-triple-ergodic-averages-for-mixing-transformations-October-4-2026)

The family claims pointwise convergence of multiple ergodic averages for mixing transformations.

## Extracted instruments

- [MI-000712: Extract convergence from sublinear deterministic-block oscillation](../instruments/MI-000712.md)
- [MI-000713: Keep boundary terms in the finite van der Corput estimate](../instruments/MI-000713.md)

## Dependencies and antecedents

Monotone convergence, Cauchy-Schwarz, completeness and Hilbert-space correlations.

Classical oscillation methods and the Hilbert-space van der Corput criterion.

## Review and formalization scope

Read the complete oscillation-implies-convergence and van der Corput proofs in the distinct-slope manuscript. The other three manuscripts are inventory-only. Analytic oscillation estimates and multiple-average convergence are not certified.

The pinned inventory supplies no scope document or linked Comparator for this family. No Lean verification is claimed.

The oscillation bound must hold for every deterministic increasing list of block endpoints with one uniform constant. Correlation limits are taken with each lag fixed before the lag cutoff grows.

[Batch record](../../batches/B076/README.md)

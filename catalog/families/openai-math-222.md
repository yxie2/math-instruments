---
id: openai-math-222
record_type: family
title: Finite-replica continuity and Gaussian Gibbs calculus
source_family: '222'
source_collection: openai/math
batch_id: B078
subject: Probability and statistical mechanics
source_paper_ids:
- P-000492
instrument_ids:
- MI-000730
- MI-000731
headline: The family claims free-energy formulas and microscopic jamming for several perceptron models.
central_instrument: Express normalizing denominators by additional replicas and derive Gaussian perturbation
  identities with all diagonal corrections retained.
novelty_assessment: Classical finite mechanisms are separated from the source headline claims. Exhaustive
  priority is not established.
formalization_summary: IsingFiniteness concerns finiteness of a variational value for bounded continuous
  inputs and nonnegative alpha. It is not a formal statement of convergence of the Ising perceptron free
  energy. The full scope document and named Comparator were read. Other linked Comparators were not inspected.
  Target declarations contain sorry; no separate solution or Lean build was checked.
statement_faithfulness: The base random probability measure is independent of the fresh Gaussian fields.
  Reweighting is uniformly bounded above and away from zero for the continuity statement; unbounded weights
  need additional integrability.
dependencies: Finite-dimensional Gaussian continuity including singular covariance, polynomial approximation
  on compact intervals, Gaussian integration by parts and Jensen bounds.
antecedents: Classical replica representations and Gaussian interpolation, including Guerra and Toninelli.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Finite-replica continuity and Gaussian Gibbs calculus

## Source manuscripts and claim

- [The free energy of the Ising random perceptron](../papers/P-000492.md): selected passages extracted.

The following companions are inventoried but have no extraction in this batch:

- [Microscopic jamming in the negative spherical perceptron](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Microscopic-jamming-in-the-negative-spherical-perceptron-September-24-2026)
- [The spherical perceptron with bi-orthogonally invariant disorder](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-spherical-perceptron-with-bi-orthogonally-invariant-disorder-September-24-2026)
- [The free energy of the spherical random perceptron](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-free-energy-of-the-spherical-random-perceptron-September-24-2026)

The family claims free-energy formulas and microscopic jamming for several perceptron models.

## Extracted instruments

- [MI-000730: Replace Gibbs denominators by additional replicas to pass array limits](../instruments/MI-000730.md)
- [MI-000731: Differentiate Gaussian Gibbs observables with the correct replica diagonals](../instruments/MI-000731.md)

## Dependencies and antecedents

Finite-dimensional Gaussian continuity including singular covariance, polynomial approximation on compact intervals, Gaussian integration by parts and Jensen bounds.

Classical replica representations and Gaussian interpolation, including Guerra and Toninelli.

## Review and formalization scope

Read the full bounded-array continuity and Gaussian-calculus proofs. Three companions are inventory-only. No perceptron variational formula or jamming assertion is certified.

IsingFiniteness concerns finiteness of a variational value for bounded continuous inputs and nonnegative alpha. It is not a formal statement of convergence of the Ising perceptron free energy. The full scope document and named Comparator were read. Other linked Comparators were not inspected. Target declarations contain sorry; no separate solution or Lean build was checked.

The base random probability measure is independent of the fresh Gaussian fields. Reweighting is uniformly bounded above and away from zero for the continuity statement; unbounded weights need additional integrability.

[Batch record](../../batches/B078/README.md)

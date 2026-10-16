---
id: openai-math-364
record_type: family
title: Pattern-preserving centering and retained-slot entropy
source_family: '364'
source_collection: openai/math
batch_id: B086
subject: Partial differential equations
source_paper_ids:
- P-000524
instrument_ids:
- MI-000794
- MI-000795
headline: The family claims a Boltzmann-Grad limit for stable radial potentials on regular kinetic intervals,
  with a hard-sphere fluctuation companion.
central_instrument: Center only isolated labels while retaining full geometric indicators; count retained
  slots globally rather than assigning independent layer choices.
novelty_assessment: Classical ingredients are distinguished from source-specific uses. Exact priority
  of the extracted formulations is not established.
formalization_summary: No family scope is supplied; no Lean verification is claimed.
statement_faithfulness: Nonsingleton components stay intact. The L1 transform bound assumes normalized
  nonnegative one-body factors. Entropy conclusions depend on the stated slot-budget bounds.
dependencies: Boolean-lattice inversion, disjoint pattern supports and binomial coefficient estimates.
antecedents: Classical correlation-error transforms and combinatorial entropy bounds.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Pattern-preserving centering and retained-slot entropy

## Source manuscripts and claim

- [The Boltzmann–Grad limit for stable radial potentials on regular kinetic intervals](../papers/P-000524.md): selected passages extracted.

The following companions are inventoried but have no extraction in this batch:

- [Hard-sphere fluctuations on the regular Boltzmann lifespan](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Hard-sphere-fluctuations-on-the-regular-Boltzmann-lifespan-September-23-2026)

The family claims a Boltzmann-Grad limit for stable radial potentials on regular kinetic intervals, with a hard-sphere fluctuation companion.

## Extracted instruments

- [MI-000794: Center isolated labels without deleting full-array geometry](../instruments/MI-000794.md)
- [MI-000795: Count retained slots through one global binomial coefficient](../instruments/MI-000795.md)

## Dependencies and antecedents

Boolean-lattice inversion, disjoint pattern supports and binomial coefficient estimates.

Classical correlation-error transforms and combinatorial entropy bounds.

## Review and formalization scope

Read complete centering/inversion, collapsed-transform and retained-slot entropy proofs. One companion is inventory-only. A fixed-pivot forest proof was also read but is not extracted as a certified dynamical estimate. The kinetic limit is not certified.

No family scope is supplied; no Lean verification is claimed.

Nonsingleton components stay intact. The L1 transform bound assumes normalized nonnegative one-body factors. Entropy conclusions depend on the stated slot-budget bounds.

[Batch record](../../batches/B086/README.md)

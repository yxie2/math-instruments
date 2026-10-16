---
id: openai-math-235
record_type: family
title: Omission delays and random-clause replacement
source_family: '235'
source_collection: openai/math
batch_id: B080
subject: Probability and statistical mechanics
source_paper_ids:
- P-000499
instrument_ids:
- MI-000744
- MI-000745
headline: The family claims limiting random SAT thresholds, hitting-time variance bounds and computability.
central_instrument: Turn a squared omission delay into a sum of truncated killing probabilities; replace
  a shorter clause uniformly in its background and telescope in time.
novelty_assessment: Classical ingredients are credited; exact novelty of the source-specific assembly
  is not established.
formalization_summary: FixedClauseThreshold targets a positive finite limiting density for each fixed
  k>=3, with no assertion at equality and no numerical value. The scope describes other variance and computability
  targets, not inspected here. Full scope and named Comparator read. Other linked targets were not inspected.
  The inspected target includes sorry; no separate solution or Lean build was checked.
statement_faithfulness: Omitted positions keep their original indices and the capped endpoint is included.
  Clauses use distinct variables with independent signs; successive replacements condition on all other
  clauses.
dependencies: Martingale variance decomposition, frozen solution-set hazards, exact forced-variable counts
  and monotone survival telescoping.
antecedents: Efron-Stein-type omission bounds and Carenini pointwise cubical replacement.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Omission delays and random-clause replacement

## Source manuscripts and claim

- [A Limiting Satisfiability Threshold for Every Fixed Clause Size](../papers/P-000499.md): selected passages extracted.

The following companions are inventoried but have no extraction in this batch:

- [Linear Variance of the Random 3-SAT Hitting Time](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Linear-Variance-of-the-Random-3-SAT-Hitting-Time-October-5-2026)
- [Variance of the Random k-SAT Hitting Time](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Variance-of-the-Random-k-SAT-Hitting-Time-September-27-2026)
- [Computing the Random 3-SAT Threshold](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Computing-the-Random-3-SAT-Threshold-September-27-2026)

The family claims limiting random SAT thresholds, hitting-time variance bounds and computability.

## Extracted instruments

- [MI-000744: Bound a squared omission delay by frozen killing hazards](../instruments/MI-000744.md)
- [MI-000745: Replace a shorter clause uniformly and telescope the forcing mass](../instruments/MI-000745.md)

## Dependencies and antecedents

Martingale variance decomposition, frozen solution-set hazards, exact forced-variable counts and monotone survival telescoping.

Efron-Stein-type omission bounds and Carenini pointwise cubical replacement.

## Review and formalization scope

Read complete concentration deletion and pivotal-pair proofs, and the full replacement/integrated-forcing section. Three companions are inventory-only. No threshold convergence or sharp variance headline is certified.

FixedClauseThreshold targets a positive finite limiting density for each fixed k>=3, with no assertion at equality and no numerical value. The scope describes other variance and computability targets, not inspected here. Full scope and named Comparator read. Other linked targets were not inspected. The inspected target includes sorry; no separate solution or Lean build was checked.

Omitted positions keep their original indices and the capped endpoint is included. Clauses use distinct variables with independent signs; successive replacements condition on all other clauses.

[Batch record](../../batches/B080/README.md)

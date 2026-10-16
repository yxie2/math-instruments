---
id: openai-math-104
record_type: family
title: Pathwise gain-bias arguments and uniform strategy restarts
source_family: '104'
source_collection: openai/math
batch_id: B073
subject: Theoretical computer science
source_paper_ids:
- P-000459
- P-000460
instrument_ids:
- MI-000690
- MI-000691
headline: The family claims quasipolynomial algorithms for several mean-payoff game models.
central_instrument: Finite-valued gain stabilization converts one-step data to pathwise payoffs; increasing
  rounds preserve uniform prefix bounds under repeated restarts.
novelty_assessment: Directly checked antecedents are identified below. No exhaustive novelty determination
  or certification of a source headline is claimed.
formalization_summary: Read the scope and complete RandomizedMeanPayoff Comparator. Its earlier target
  is a randomized quasipolynomial machine with success probability at least 7/8. It does not state the
  newer stochastic or parity targets. The other listed Comparator was not inspected. Inspected Comparator
  target bodies contain sorry; no separate solution or Lean build was checked.
statement_faithfulness: Gain and bias data are assumed supplied. The parity strategy is fixed before an
  accuracy parameter is chosen, and controls every prefix against history-dependent play.
dependencies: Finite-valued submartingales, bounded martingale differences, telescoping potentials, attractors
  and cycle deletion.
antecedents: Classical martingale arguments and Bouyer-Markey-Olschewski-Ummels increasing-round strategy
  combinations.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Pathwise gain-bias arguments and uniform strategy restarts

## Source manuscripts and claim

- [Turn-Based Stochastic Mean-Payoff Games in Deterministic Quasipolynomial Time](../papers/P-000459.md): selected passages extracted.
- [Mean-payoff parity games in quasipolynomial time](../papers/P-000460.md): selected passages extracted.

The following companions are inventoried but have no extraction in this batch:

- [Deterministic quasipolynomial-time mean-payoff games](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Deterministic-quasipolynomial-time-mean-payoff-games-September-25-2026)
- [Randomized quasipolynomial-time mean-payoff games](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Randomized-quasipolynomial-time-mean-payoff-games-September-25-2026)

The family claims quasipolynomial algorithms for several mean-payoff game models.

## Extracted instruments

- [MI-000690: Turn finite-valued gain and bounded bias into pathwise average bounds](../instruments/MI-000690.md)
- [MI-000691: Preserve all-prefix guarantees when restarting parity sub-strategies](../instruments/MI-000691.md)

## Dependencies and antecedents

Finite-valued submartingales, bounded martingale differences, telescoping potentials, attractors and cycle deletion.

Classical martingale arguments and Bouyer-Markey-Olschewski-Ummels increasing-round strategy combinations.

## Review and formalization scope

Read all selected pathwise lemmas and their payoff application, the one-step gain-bias conditions, the full parity combination proof and its mean-payoff prefix input. Two of four manuscripts receive extractions; earlier deterministic and randomized manuscripts remain inventory-only. Quasipolynomial bounds and construction of the gain-bias data are not certified.

Read the scope and complete RandomizedMeanPayoff Comparator. Its earlier target is a randomized quasipolynomial machine with success probability at least 7/8. It does not state the newer stochastic or parity targets. The other listed Comparator was not inspected. Inspected Comparator target bodies contain sorry; no separate solution or Lean build was checked.

Gain and bias data are assumed supplied. The parity strategy is fixed before an accuracy parameter is chosen, and controls every prefix against history-dependent play.

[Batch record](../../batches/B073/README.md)

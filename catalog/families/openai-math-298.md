---
id: openai-math-298
record_type: family
title: Retained matrix ensembles and rare structural events in entropy comparisons
source_family: '298'
source_collection: openai/math
batch_id: B018
subject: Operator algebras
source_paper_ids:
- P-000146
instrument_ids:
- MI-000253
- MI-000254
headline: The source claims a bounded self-adjoint finite tuple in a faithful normal tracial von Neumann
  algebra with both free entropies finite and microstates entropy at least one-half below nonmicrostates
  entropy.
central_instrument: Select one near-optimal matrix ensemble before adding noise, transfer its entropy
  production by polynomial tests, and apply a structural rare-event deficit to that same terminal law.
novelty_assessment: The Fisher-information comparison follows established work of Jekel-Pi and earlier
  entropy comparisons. Binary data processing and Gaussian net estimates are classical. The candidate
  reusable combination preserves the same ensemble so a structural entropy deficit survives the comparison.
formalization_summary: 'The scope document and FiniteEntropySeparation.lean target were inspected, including
  cutoff/limsup microstates entropy and semicircular-noise nonmicrostates entropy. Comparator statements
  were inspected, not proof builds: no Lean solution was built or kernel-checked. The auxiliary cards
  are not all separate formalization targets.'
statement_faithfulness: The dimension subsequence and initial laws are fixed independently of time and
  polynomial tests. The block event is a deterministic event on terminal tuples; the initial spectral
  partition is only a probability witness. Moment convergence, conjugate variables and block structure
  are explicit inputs.
dependencies: Gaussian smoothing, normalized de Bruijn identity, noncommutative polynomial derivatives,
  Fatou, unitary nets, chi-square tails and binary relative entropy.
antecedents: Jekel-Pi, An elementary proof of the inequality chi<=chi* for conditional free entropy, Proposition
  6.1 and Theorem 6.4; Biane-Capitaine-Guionnet entropy comparison; classical binary data processing and
  Gaussian concentration.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Retained matrix ensembles and rare structural events in entropy comparisons

## Source manuscript and claim

[A finite-entropy separation of microstates and nonmicrostates free entropy](../papers/P-000146.md), by OpenAI, September 25, 2026.

The source claims a bounded self-adjoint finite tuple in a faithful normal tracial von Neumann algebra with both free entropies finite and microstates entropy at least one-half below nonmicrostates entropy.

## Extracted instruments

- [MI-000253: Retaining one ensemble transfers matrix entropy production to free Fisher information](../instruments/MI-000253.md)
- [MI-000254: A persistent block event yields a Gaussian-relative entropy deficit](../instruments/MI-000254.md)

## Dependencies and antecedents

Gaussian smoothing, normalized de Bruijn identity, noncommutative polynomial derivatives, Fatou, unitary nets, chi-square tails and binary relative entropy.

Jekel-Pi, An elementary proof of the inequality chi<=chi* for conditional free entropy, Proposition 6.1 and Theorem 6.4; Biane-Capitaine-Guionnet entropy comparison; classical binary data processing and Gaussian concentration. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the variational Fisher formula, retained-ensemble flow proof, matrix block transfer and complete rare-event entropy argument. The free cumulant estimates, construction of the limiting tuple and full finite-entropy separation were not audited.

The scope document and FiniteEntropySeparation.lean target were inspected, including cutoff/limsup microstates entropy and semicircular-noise nonmicrostates entropy. Comparator statements were inspected, not proof builds: no Lean solution was built or kernel-checked. The auxiliary cards are not all separate formalization targets.

The dimension subsequence and initial laws are fixed independently of time and polynomial tests. The block event is a deterministic event on terminal tuples; the initial spectral partition is only a probability witness. Moment convergence, conjugate variables and block structure are explicit inputs.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/298.md) · [Batch record](../../batches/B018/README.md)

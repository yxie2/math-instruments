---
id: openai-math-214
record_type: family
title: Unimodular traces and sprinkling resolvents
source_family: '214'
source_collection: openai/math
batch_id: B051
subject: Probability and statistical mechanics
source_paper_ids:
- P-000286
instrument_ids:
- MI-000510
- MI-000511
headline: The source claims a nonuniqueness phase and critical mean-field laws on every nonamenable quasi-transitive
  graph.
central_instrument: Inverse stabilizer weights make invariant diagonal averages into a finite trace. Independent
  sprinkling compares connection kernels through a positive Neumann series.
novelty_assessment: 'Both selected mechanisms have explicit classical antecedents: Aldous-Lyons for invariant
  traces and Hutchcroft Lemma 2.4 for the same sprinkling inequality.'
formalization_summary: The targets include critical operator boundedness, pc<p_(2-to-2)<=pu, a single
  coupled interval with infinitely many infinite clusters, critical tail and susceptibility laws, exponential
  decay, and every finite symmetric Cayley generating set. The scope document and all linked Comparator
  definitions and targets were read. Their target proofs contain sorry; no solution or Lean project was
  built.
statement_faithfulness: Root-type weights do not change the counting-measure Hilbert space. Sprinkling
  is an entrywise kernel comparison, not a positive-semidefinite order assertion, and its useful norm
  conclusion requires a convergent series.
dependencies: Unimodular Haar stabilizer volumes, mass transport, absolute summability and positive square
  roots; product percolation, disjoint-witness inequality and Neumann-series convergence.
antecedents: Benjamini-Lyons-Peres-Schramm mass transport; Aldous-Lyons invariant trace; Hutchcroft connection-operator
  sprinkling.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Unimodular traces and sprinkling resolvents

## Source manuscripts and claim

- [Nonuniqueness of percolation on nonamenable quasi-transitive graphs](../papers/P-000286.md): selected passages extracted.

The source claims a nonuniqueness phase and critical mean-field laws on every nonamenable quasi-transitive graph.

## Extracted instruments

- [MI-000510: Use stabilizer weights to obtain a finite invariant trace](../instruments/MI-000510.md)
- [MI-000511: Control percolation sprinkling by a positive connection-kernel series](../instruments/MI-000511.md)

## Dependencies and antecedents

Unimodular Haar stabilizer volumes, mass transport, absolute summability and positive square roots; product percolation, disjoint-witness inequality and Neumann-series convergence.

Benjamini-Lyons-Peres-Schramm mass transport; Aldous-Lyons invariant trace; Hutchcroft connection-operator sprinkling.

## Review and formalization scope

Read the full weighted mass-transport, invariant-trace and sprinkling proofs. Also read the monotone endpoint-passage proof for context. The critical boundedness argument and nonuniqueness theorem remain unverified here.

The targets include critical operator boundedness, pc<p_(2-to-2)<=pu, a single coupled interval with infinitely many infinite clusters, critical tail and susceptibility laws, exponential decay, and every finite symmetric Cayley generating set. The scope document and all linked Comparator definitions and targets were read. Their target proofs contain sorry; no solution or Lean project was built.

Root-type weights do not change the counting-measure Hilbert space. Sprinkling is an entrywise kernel comparison, not a positive-semidefinite order assertion, and its useful norm conclusion requires a convergent series.

[Batch record](../../batches/B051/README.md)

---
id: openai-math-186
record_type: family
title: Capture supports and average restricted Fourier mass exactly
source_family: '186'
source_collection: openai/math
batch_id: B060
subject: Combinatorics
source_paper_ids:
- P-000354
- P-000355
instrument_ids:
- MI-000585
- MI-000586
headline: The sources claim a uniform influence bound for hypergraph properties and a sharp threshold-width
  bound for monotone graph properties.
central_instrument: A block meeting one low-degree support vertex captures a nonempty low Fourier level.
  Orthogonality expresses averaged restricted coefficients exactly in terms of the original coefficients.
novelty_assessment: Fourier restriction averaging is standard, with a directly inspected earlier lemma.
  The hypergraph capture argument is an elementary extension of the graph companion, with explicit degree
  conversion; independent priority of that particular extension is unresolved.
formalization_summary: SharpThreshold defines Bernoulli graph means and quantiles and asserts width at
  most 2^19 log(1/(2 epsilon))/(log n)^2 for invariant increasing nontrivial graph properties. It does
  not state the hypergraph companion influence theorem. All four scope documents and all six linked Comparators
  in this batch were read in full. Their headline targets have sorry proof bodies. No separate solution
  or Lean project was built.
statement_faithfulness: A support is a set of distinct r-edges. Capturing one vertex retains all its incident
  support edges, not necessarily one edge. Fourier mass conditions only the free-coordinate degree; outside
  degree is unrestricted.
dependencies: Hypergraph average degree, uniform fixed-size sampling, a union bound, product Fourier orthogonality
  and pivotal-event conditioning.
antecedents: Standard random-restriction Fourier identity; Kelman-Kindler-Lifshitz-Minzer-Safra Lemma
  2.7; the graph companion capture method.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Capture supports and average restricted Fourier mass exactly

## Source manuscripts and claim

- [A uniform influence bound for hypergraph properties](../papers/P-000354.md): selected passages extracted.
- [A Sharp Threshold Bound for Monotone Graph Properties](../papers/P-000355.md): selected passages extracted.

The sources claim a uniform influence bound for hypergraph properties and a sharp threshold-width bound for monotone graph properties.

## Extracted instruments

- [MI-000585: Capture a hypergraph support by hitting one low-degree vertex](../instruments/MI-000585.md)
- [MI-000586: Average a Fourier restriction without discarding exterior degree](../instruments/MI-000586.md)

## Dependencies and antecedents

Hypergraph average degree, uniform fixed-size sampling, a union bound, product Fourier orthogonality and pivotal-event conditioning.

Standard random-restriction Fourier identity; Kelman-Kindler-Lifshitz-Minzer-Safra Lemma 2.7; the graph companion capture method.

## Review and formalization scope

Read the full hypergraph restriction and capture section and the full exact restriction lemma in the graph paper. The low-degree analytic estimate and global influence and threshold arguments were not audited.

SharpThreshold defines Bernoulli graph means and quantiles and asserts width at most 2^19 log(1/(2 epsilon))/(log n)^2 for invariant increasing nontrivial graph properties. It does not state the hypergraph companion influence theorem. All four scope documents and all six linked Comparators in this batch were read in full. Their headline targets have sorry proof bodies. No separate solution or Lean project was built.

A support is a set of distinct r-edges. Capturing one vertex retains all its incident support edges, not necessarily one edge. Fourier mass conditions only the free-coordinate degree; outside degree is unrestricted.

[Batch record](../../batches/B060/README.md)

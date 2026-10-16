---
id: openai-math-175
record_type: family
title: Smoothed covers, maximal cutoffs and pair-sampled repair
source_family: '175'
source_collection: openai/math
batch_id: B060
subject: Combinatorics
source_paper_ids:
- P-000349
- P-000350
- P-000351
instrument_ids:
- MI-000580
- MI-000581
- MI-000582
headline: The three sources concern graph decomposition at the integral expectation threshold, integral-fractional
  threshold equivalence and Talagrand discrete convexity.
central_instrument: A greedy probability increment compresses a smoothed cover; a maximal truncation controls
  heavy coordinates; pair sampling makes an uncovered m-tuple pay m squared independent failures.
novelty_assessment: The maximal-cutoff mechanism has an explicit earlier analogue in Bednorz-Martynek-Meller.
  Sampled unions appear in Fischer-Person. The source arrangements and parameters are recorded without
  claiming these general ideas are new.
formalization_summary: The scope and linked targets cover integral-fractional comparison with constant
  25 times 512^4, and discrete convexity with k=2^75 and budget 1/2. Fractional covers include the empty
  set. The convexity target permits repeated union members and arbitrary input families. No graph-decomposition
  target is linked. All four scope documents and all six linked Comparators in this batch were read in
  full. Their headline targets have sorry proof bodies. No separate solution or Lean project was built.
statement_faithfulness: Compression gives a probabilistic smoothed cover, not a deterministic containment
  cover. Strictly heavy coordinates are used at a possibly tied cutoff. Ordered sampled pairs, including
  diagonals, remain independent even when unions coincide.
dependencies: Finite Bernoulli product measures, greedy probability increments, piecewise-linear truncation,
  weighted-degree counting and first moments.
antecedents: Maximal truncation in selector processes; sampled unions in Fischer-Person; elementary greedy
  measure increments.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Smoothed covers, maximal cutoffs and pair-sampled repair

## Source manuscripts and claim

- [Graph Decompositions at the Integral Expectation Threshold](../papers/P-000349.md): selected passages extracted.
- [Integral and fractional expectation thresholds are equivalent](../papers/P-000350.md): selected passages extracted.
- [Talagrand’s discrete-convexity conjecture](../papers/P-000351.md): selected passages extracted.

The three sources concern graph decomposition at the integral expectation threshold, integral-fractional threshold equivalence and Talagrand discrete convexity.

## Extracted instruments

- [MI-000580: Compress a cover after independent Bernoulli smoothing](../instruments/MI-000580.md)
- [MI-000581: Use a maximal truncation to bound the strictly heavy set](../instruments/MI-000581.md)
- [MI-000582: Repair a sampled cover using the quadratic number of pair failures](../instruments/MI-000582.md)

## Dependencies and antecedents

Finite Bernoulli product measures, greedy probability increments, piecewise-linear truncation, weighted-degree counting and first moments.

Maximal truncation in selector processes; sampled unions in Fischer-Person; elementary greedy measure increments.

## Review and formalization scope

Read the full compression proof, maximal-truncation proof and 185-line elementary covering argument. Global threshold comparison, discrete-convexity transfer and graph-decomposition theorem are not certified.

The scope and linked targets cover integral-fractional comparison with constant 25 times 512^4, and discrete convexity with k=2^75 and budget 1/2. Fractional covers include the empty set. The convexity target permits repeated union members and arbitrary input families. No graph-decomposition target is linked. All four scope documents and all six linked Comparators in this batch were read in full. Their headline targets have sorry proof bodies. No separate solution or Lean project was built.

Compression gives a probabilistic smoothed cover, not a deterministic containment cover. Strictly heavy coordinates are used at a possibly tied cutoff. Ordered sampled pairs, including diagonals, remain independent even when unions coincide.

[Batch record](../../batches/B060/README.md)

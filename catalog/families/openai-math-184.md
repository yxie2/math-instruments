---
id: openai-math-184
record_type: family
title: Bounded input participation and simultaneous coupling
source_family: '184'
source_collection: openai/math
batch_id: B060
subject: Combinatorics
source_paper_ids:
- P-000352
- P-000353
instrument_ids:
- MI-000583
- MI-000584
headline: The sources claim correspondence-coloring bounds for forbidden cliques and logarithmic independence
  bounds for clique-free graphs.
central_instrument: Generalized Holder reduces dependence to input participation. Shared rejection sampling
  couples every probability row at once with a pairwise total-variation bound.
novelty_assessment: Both selected tools are classical and explicitly attributed in the sources. Their
  application interfaces are useful, but no novelty is claimed for the concentration or coupling theorem.
formalization_summary: 'Despite the family title, the only linked target is CliqueFreeLog: for each fixed
  r>=4 a positive c_r gives independent-set size at least c_r n log(d)/d in K_r-free graphs with average
  degree d>=2. It does not state the correspondence-coloring companion theorem. All four scope documents
  and all six linked Comparators in this batch were read in full. Their headline targets have sorry proof
  bodies. No separate solution or Lean project was built.'
statement_faithfulness: Inputs are independent, output functions need not be. Range lengths may differ
  and the participation parameter may be real. Coupling is simultaneous; pairwise maximality is not asserted.
dependencies: Generalized Holder, Hoeffding exponential moments, Markov inequality and elementary rejection
  sampling.
antecedents: Finner; Gavinsky-Lovett-Saks-Srinivasan; Kleinberg-Tardos; Angel-Spinka.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Bounded input participation and simultaneous coupling

## Source manuscripts and claim

- [Correspondence coloring graphs with a forbidden clique](../papers/P-000352.md): selected passages extracted.
- [A logarithmic independence bound for clique-free graphs](../papers/P-000353.md): selected passages extracted.

The sources claim correspondence-coloring bounds for forbidden cliques and logarithmic independence bounds for clique-free graphs.

## Extracted instruments

- [MI-000583: Concentrate a sum by counting how often each independent input is read](../instruments/MI-000583.md)
- [MI-000584: Couple all probability rows through one rejection stream](../instruments/MI-000584.md)

## Dependencies and antecedents

Generalized Holder, Hoeffding exponential moments, Markov inequality and elementary rejection sampling.

Finner; Gavinsky-Lovett-Saks-Srinivasan; Kleinberg-Tardos; Angel-Spinka.

## Review and formalization scope

Read the complete bounded-participation proof and its local use, and the complete shared-rejection proof. Full coloring rounds, entropy smoothing and the global clique-free bounds remain unaudited.

Despite the family title, the only linked target is CliqueFreeLog: for each fixed r>=4 a positive c_r gives independent-set size at least c_r n log(d)/d in K_r-free graphs with average degree d>=2. It does not state the correspondence-coloring companion theorem. All four scope documents and all six linked Comparators in this batch were read in full. Their headline targets have sorry proof bodies. No separate solution or Lean project was built.

Inputs are independent, output functions need not be. Range lengths may differ and the participation parameter may be real. Coupling is simultaneous; pairwise maximality is not asserted.

[Batch record](../../batches/B060/README.md)

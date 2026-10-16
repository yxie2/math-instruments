---
id: openai-math-307
record_type: family
title: Propagation-controlled maximal norms and multipliers
source_family: '307'
source_collection: openai/math
batch_id: B083
subject: Topology
source_paper_ids:
- P-000512
instrument_ids:
- MI-000770
- MI-000771
headline: The family claims failure of rational injectivity for coarse assembly, with maximal and reduced
  variants in separate manuscripts.
central_instrument: Decompose a bounded-propagation operator into matchings to control every representation;
  construct multipliers using a positive square identity.
novelty_assessment: The finite mechanisms are separated from the headline claims. Exact priority of source-specific
  formulations is not established.
formalization_summary: The scope and selected CoarseAssembly definitions and main target were inspected.
  The 6648-line prerequisite development was not read in full. The target uses the concrete reduced locally
  compact Roe algebra, whereas the selected manuscript concerns the maximal completion. Its target contains
  sorry; no separate solution or Lean build was checked.
statement_faithfulness: The discrete space has bounded geometry. Compact entries define local compactness
  without a uniform rank bound. Uniform propagation is retained when taking norm limits.
dependencies: Bipartite edge coloring, contractivity on diagonal C*-algebras and double-centralizer extension.
antecedents: Classical maximal Roe norm control and finite-propagation multiplier theory.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Propagation-controlled maximal norms and multipliers

## Source manuscripts and claim

- [Failure of rational injectivity for maximal coarse assembly](../papers/P-000512.md): selected passages extracted.

The following companions are inventoried but have no extraction in this batch:

- [A counterexample to the coarse Novikov conjecture](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/A-counterexample-to-the-coarse-Novikov-conjecture-September-23-2026)

The family claims failure of rational injectivity for coarse assembly, with maximal and reduced variants in separate manuscripts.

## Extracted instruments

- [MI-000770: Use matching decompositions to control every fixed-propagation representation](../instruments/MI-000770.md)
- [MI-000771: Extend bounded finite-propagation operators as multipliers by a positive square](../instruments/MI-000771.md)

## Dependencies and antecedents

Bipartite edge coloring, contractivity on diagonal C*-algebras and double-centralizer extension.

Classical maximal Roe norm control and finite-propagation multiplier theory.

## Review and formalization scope

Read complete fixed-propagation, compact-ideal and multiplier proofs. One companion is inventory-only. The persistent class, transfer and sliding arguments are not certified.

The scope and selected CoarseAssembly definitions and main target were inspected. The 6648-line prerequisite development was not read in full. The target uses the concrete reduced locally compact Roe algebra, whereas the selected manuscript concerns the maximal completion. Its target contains sorry; no separate solution or Lean build was checked.

The discrete space has bounded geometry. Compact entries define local compactness without a uniform rank bound. Uniform propagation is retained when taking norm limits.

[Batch record](../../batches/B083/README.md)

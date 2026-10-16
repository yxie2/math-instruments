---
id: openai-math-118
record_type: family
title: Competing tree quotas and conservative scalar packing encodings
source_family: '118'
source_collection: openai/math
batch_id: B010
subject: Theoretical computer science
source_paper_ids:
- P-000112
instrument_ids:
- MI-000182
- MI-000183
headline: The source claims unbounded additive gaps for both individual-copy and numerical-type configuration
  LPs, and NP-hardness of every fixed additive approximation gap in one-dimensional bin packing.
central_instrument: Two trees are easy to mark separately but impossible to hit together under shared
  depth quotas. Hierarchical scalar scores encode bin patterns while global conservation bounds the exceptions
  caused by extra bins.
novelty_assessment: Disjoint-branch quota obstructions and large-base constraint encodings have antecedents.
  The two-color pruning and the explicit defect accounting are selected candidate combinations; the full
  reduction and priority are not certified.
formalization_summary: BinPackingGap.lean states the equal-LP unbounded gap, NP-hard gap reductions for
  every fixed nonnegative integer c, and existence of a fixed-additive polynomial algorithm iff P=NP,
  using explicit binary encodings and finite-alphabet machines. The scope documents and Comparator statements
  were compared; no Lean solution was built or kernel-checked. The auxiliary instruments are not separate
  certified Comparator results.
statement_faithfulness: The LP statements distinguish physical copies from unrestricted numerical-type
  configurations. A feasible bin need not have an intended pattern; nonpositive primary scores and inventory
  conservation control the exceptions.
dependencies: Finite rooted trees with uncontracted depth levels; exponentially growing within-phase quotas;
  two-color pruning; ten bounded integer count equations; separated rational scales; equal label inventories
  and prefix conservation.
antecedents: Chalermsook-Chuzhoy use disjoint-branch constructions for fire containment. Large-base aggregation
  is classical, with a recent bin-packing use by Jansen-Pirotton-Tutas. The selected cards retain these
  attributions.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Competing tree quotas and conservative scalar packing encodings

## Source manuscript and claim

[Additive hardness and unbounded configuration gaps in bin packing](../papers/P-000112.md), by OpenAI, September 24, 2026.

The source claims unbounded additive gaps for both individual-copy and numerical-type configuration LPs, and NP-hardness of every fixed additive approximation gap in one-dimensional bin packing.

## Extracted instruments

- [MI-000182: Two trees separate individual multiple hits from shared one-hit quotas](../instruments/MI-000182.md)
- [MI-000183: Scalar packing encodings retain a bounded defect budget through conservation](../instruments/MI-000183.md)

## Dependencies and antecedents

Finite rooted trees with uncontracted depth levels; exponentially growing within-phase quotas; two-color pruning; ten bounded integer count equations; separated rational scales; equal label inventories and prefix conservation.

Chalermsook-Chuzhoy use disjoint-branch constructions for fire containment. Large-base aggregation is classical, with a recent bin-packing use by Jansen-Pirotton-Tutas. The selected cards retain these attributions. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the competing-tree construction, scalar encoding proof, primary-defect count and label-prefix argument. The geometric coordinate construction, full soundness reduction, LP witness and complexity reductions were not audited.

BinPackingGap.lean states the equal-LP unbounded gap, NP-hard gap reductions for every fixed nonnegative integer c, and existence of a fixed-additive polynomial algorithm iff P=NP, using explicit binary encodings and finite-alphabet machines. The scope documents and Comparator statements were compared; no Lean solution was built or kernel-checked. The auxiliary instruments are not separate certified Comparator results.

The LP statements distinguish physical copies from unrestricted numerical-type configurations. A feasible bin need not have an intended pattern; nonpositive primary scores and inventory conservation control the exceptions.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/118.md) · [Batch record](../../batches/B010/README.md)

---
id: openai-math-133
record_type: family
title: Parity-lift duality and cycle potentials
source_family: '133'
source_collection: openai/math
batch_id: B074
subject: Theoretical computer science
source_paper_ids:
- P-000467
- P-000468
instrument_ids:
- MI-000698
- MI-000699
headline: The family claims construction and complexity results for Weisfeiler-Leman equivalence and identification.
central_instrument: Binary affine systems compare lift counts without cancellation; rectangular differences
  turn globally vanishing edge sums into vertex potentials.
novelty_assessment: Established mechanisms and directly checked antecedents are identified below. No exhaustive
  novelty determination or source headline certification is claimed.
formalization_summary: Read the scope and both complete named Comparators. ParityLifts targets a choice-system
  equivalence under joint, separate and pure WL conventions with specified early-round detection. WLIdentification
  targets EXPTIME-completeness for identifying a graph against every comparison graph. The other two listed
  Comparators were not inspected. The inspected theorem targets contain sorry; no separate solution or
  Lean build was checked.
statement_faithfulness: Tag variables are indexed by source vertices, even when their projected images
  agree. Cycle lifting is over F2, with at least three coordinate factors and a full product domain.
dependencies: Graph homomorphisms, binary linear algebra, connected type graphs and mixed differences.
antecedents: Roberson parity graphs and the finite-field alternative for linear systems; elementary potential
  decomposition.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Parity-lift duality and cycle potentials

## Source manuscripts and claim

- [Parity lifts and bounded-treewidth witnesses for Weisfeiler–Leman equivalence](../papers/P-000467.md): selected passages extracted.
- [The complexity of identifying a graph by Weisfeiler–Leman refinement](../papers/P-000468.md): selected passages extracted.

The following companions are inventoried but have no extraction in this batch:

- [Unconditional time lower bounds for Weisfeiler–Leman equivalence](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Unconditional-time-lower-bounds-for-Weisfeiler-Leman-equivalence-September-25-2026)
- [Variable-dimension Weisfeiler–Leman equivalence on general and subcubic graphs](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Variable-dimension-Weisfeiler-Leman-equivalence-on-general-and-subcubic-graphs-September-25-2026)

The family claims construction and complexity results for Weisfeiler-Leman equivalence and identification.

## Extracted instruments

- [MI-000698: Compare parity lifts by binary solvability and expose a dual witness](../instruments/MI-000698.md)
- [MI-000699: Recover vertex potentials from a vanishing cyclic sum](../instruments/MI-000699.md)

## Dependencies and antecedents

Graph homomorphisms, binary linear algebra, connected type graphs and mixed differences.

Roberson parity graphs and the finite-field alternative for linear systems; elementary potential decomposition.

## Review and formalization scope

Read the complete parity-lift definition, lift-count duality proof and connected type-mass argument, and the complete cycle-lifting proof with its row-sum definition. Two of four manuscripts receive extractions; unconditional-time and variable-dimension manuscripts remain inventory-only. Separator extraction, graph encodings and complexity reductions are not certified.

Read the scope and both complete named Comparators. ParityLifts targets a choice-system equivalence under joint, separate and pure WL conventions with specified early-round detection. WLIdentification targets EXPTIME-completeness for identifying a graph against every comparison graph. The other two listed Comparators were not inspected. The inspected theorem targets contain sorry; no separate solution or Lean build was checked.

Tag variables are indexed by source vertices, even when their projected images agree. Cycle lifting is over F2, with at least three coordinate factors and a full product domain.

[Batch record](../../batches/B074/README.md)

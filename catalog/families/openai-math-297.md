---
id: openai-math-297
record_type: family
title: Naimark’s problem in ZFC
source_family: '297'
source_collection: openai/math
batch_id: B001
original_group: 2
subject: Operator algebras, topology and symplectic geometry
source_paper_ids:
- P-000013
instrument_ids:
- MI-000101
- MI-000102
- MI-000103
headline: Naimark’s problem in ZFC
central_instrument: '“Selective bridge”: a reduced HNN adjunction along peaking projection sequences merges exactly two pure-state classes while every other pure state extends uniquely, so each step depends on countably many earlier ones and diamond is replaced by cardinal bookkeeping at length $`\mathfrak{c}^{+}`$.'
novelty_assessment: combination
formalization_summary: modules, not in catalogue
statement_faithfulness: yes, no hypotheses
dependencies: 'no'
antecedents: Tanaka, arXiv 2609.26930
review_status: imported-from-direction-paper
updated: '2026-10-12'
source_status_line: 'Lean, 16 modules, not in catalogue combination earlier related result: Tanaka'
map_formalization_summary: yes (not in catalogue)
---

# Naimark’s problem in ZFC

[Family index](../../tables/families.md) · [Batch B001](../../batches/B001/README.md)

The statements and assessments below report the direction paper’s extraction. They do not certify the source proofs.

## Source manuscripts

- [P-000013](../papers/P-000013.md)

## Family description

Source status as recorded in the direction paper: Lean, 16 modules, not in catalogue combination earlier related result: Tanaka

The source constructs a unital, infinite-dimensional, simple $`C^*`$-algebra with a faithful tracial state whose nonzero irreducible representations are all unitarily equivalent, in ZFC alone. Akemann–Weaver 2004 needed Jensen’s diamond. The construction has length $`\mathfrak{c}^{+}`$; density is left in $`[\mathfrak{c},\mathfrak{c}^+]`$. Tanaka’s preprint of 22 September 2026 [source](../../direction/references.md#src:tanaka) gives the same existence theorem plus density exactly $`\mathfrak{c}`$; the paper acknowledges this earlier result.

## Extracted instruments.

- [MI-000101: Selective bridge via reduced HNN adjunction along peaking sequences](../instruments/MI-000101.md)

- [MI-000102: Dependency-closed subiterations with reduced-HNN reordering](../instruments/MI-000102.md)

- [MI-000103: Diamond replacement](../instruments/MI-000103.md)

## Reused.

Ueda’s HNN extensions and Blanchard–Dykema expectations; Akemann–Anderson–Pedersen excision; Akemann–Weaver cross-excision; Kadison transitivity; Kishimoto–Ozawa–Sakai homogeneity (only on separable subalgebras; reproved in Lean).

## Caveats.

The repository’s formalization records differ: the catalogue omits the result, while the documentation reports full coverage. No Lean build was run here.

## Recorded assessment

- Novelty: combination
- Formalization: modules, not in catalogue
- Statement coverage: yes, no hypotheses
- Dependencies: no
- Antecedents: Tanaka, arXiv 2609.26930

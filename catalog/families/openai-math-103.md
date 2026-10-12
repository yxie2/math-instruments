---
id: openai-math-103
record_type: family
title: L = RL = BPL
source_family: '103'
source_collection: openai/math
batch_id: B001
original_group: 2
subject: Combinatorics, geometry and complexity
source_paper_ids:
- P-000034
instrument_ids:
- MI-000080
- MI-000081
- MI-000082
headline: $`\mathrm{L}=\mathrm{RL}=\mathrm{BPL}`$
central_instrument: '“Exact correction and copy hierarchy”: no pseudorandom generator; refine the configuration graph algebraically so every transition weight is small, estimate the reward with a sampler driven by one O(log n)-bit environment, and control the evaluator’s recursive space use with a catalytic key-equality gadget.'
novelty_assessment: new
formalization_summary: files; identifiers obfuscated
statement_faithfulness: yes, multi-tape TM, L = RL ∧ RL = BPL
dependencies: 'no'
antecedents: —
review_status: imported-from-direction-paper
updated: '2026-10-12'
source_status_line: Lean, multi-tape Turing-machine statement new
map_formalization_summary: 'yes'
---

# L = RL = BPL

[Family index](../../tables/families.md) · [Batch B001](../../batches/B001/README.md)

The statements and assessments below report the direction paper’s extraction. They do not certify the source proofs.

## Source manuscripts

- [P-000034](../papers/P-000034.md)

## Family description

Source status as recorded in the direction paper: Lean, multi-tape Turing-machine statement new

Deterministic logspace equals randomized logspace, one- and two-sided error. The comparator states exactly $`\mathrm{L}=\mathrm{RL}\wedge\mathrm{RL}=\mathrm{BPL}`$ for a multi-tape model with fresh coins per step and polynomial halting on every coin tape. The record stood at Hoza’s $`\log^{3/2}n/\sqrt{\log\log n}`$. The formalization has a narrower scope than the full construction: the effective compiler and numerical bounds are not formalized, and Lean identifiers are obfuscated, which limits the textual inspection reported here to the statement.

## Extracted instruments.

- [MI-000080: Exact correction and copy hierarchy](../instruments/MI-000080.md)

- [MI-000081: Rank channels and conditional averaging in a shared environment](../instruments/MI-000081.md)

- [MI-000082: Allowance/clock controller with catalytic key equality](../instruments/MI-000082.md)

## Reused.

Nilpotent inverse of the configuration graph; k-wise independent hashing; relative property (T) expanders (Shalom, Kassabov); Riesz–Thorin; Carter–Wegman fingerprints; Cook–McKenzie traversal; Lange–McKenzie–Tapp reversibility; catalytic computation (BCKLS).

## Caveats.

The source contains about 400 KB of text and an eight-step chain of sufficiently large constants. It avoids storing a seed hierarchy, the source of the $`\log^{3/2}`$ space bound in the comparison made by the initial extraction.

## Recorded assessment

- Novelty: new
- Formalization: files; identifiers obfuscated
- Statement coverage: yes, multi-tape TM, L = RL ∧ RL = BPL
- Dependencies: no
- Antecedents: —

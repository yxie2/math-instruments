---
id: openai-math-003
record_type: family
title: Zero-free half-plane Re s > 7/8
source_family: '003'
source_collection: openai/math
batch_id: B001
original_group: 1
subject: Number theory and arithmetic geometry
source_paper_ids:
- P-000062
- P-000063
- P-000075
instrument_ids:
- MI-000001
- MI-000002
- MI-000003
headline: $`\zeta`$ and Dirichlet L zero-free for $`\operatorname{Re} s>7/8`$
central_instrument: Twist the Möbius sum by all sextic residue symbols; Poisson fuses $`\mu`$ with Gauss sums into cubic Gauss sums, whose Kubota–Patterson automorphy moves the thin sextic family to a quadratic one where square-root cancellation on average is known.
novelty_assessment: combination as architecture, leaning new
formalization_summary: zeta partly inspected; Dirichlet/Hecke declarations also located
statement_faithfulness: not inspected
dependencies: no (cubic first-moment paper cited, unused)
antecedents: —
review_status: imported-from-direction-paper
updated: '2026-10-12'
source_status_line: 'Lean, agent-generated, unreviewed architecture: combination, leaning new'
map_formalization_summary: partial inspection
---

# Zero-free half-plane Re s > 7/8

[Family index](../../tables/families.md) · [Batch B001](../../batches/B001/README.md)

The statements and assessments below report the direction paper’s extraction. They do not certify the source proofs.

## Source manuscripts

- [P-000062](../papers/P-000062.md)
- [P-000063](../papers/P-000063.md)
- [P-000075](../papers/P-000075.md)

## Family description

Source status as recorded in the direction paper: Lean, agent-generated, unreviewed architecture: combination, leaning new

Every Dirichlet L-function and every finite-order Hecke L-function over $`\mathbb{Q}(\sqrt{-3})`$ has no zeros in $`\operatorname{Re} s>7/8`$. The main paper has 199 pages; a human-edited companion reaches 11/12. Corollaries include Vinogradov’s least-nonresidue conjecture.

## Extracted instruments.

- [MI-000001: Embedding the Möbius sum in a sextic family](../instruments/MI-000001.md)

- [MI-000002: Cube completion and transfer](../instruments/MI-000002.md)

- [MI-000003: Continuation from a common signal, saturated-witness zero detector, compensated probe](../instruments/MI-000003.md)

## Reused.

Kubota–Patterson theta and Dunn–Radziwiłł cusp expansions; Goldmakher–Louvel and Baier–Bansal large sieves; Heath-Brown’s recursion; Thorner–Zaman prime counting; Hecke functional equation.

## Caveats.

The needed bound is comparable to GRH on average over a family for which the general cubic sieve is sharp. The twist bookkeeping in the theta reflection is therefore a central point to check, as is the dependence of constants on the character.

## Recorded assessment

- Novelty: combination as architecture, leaning new
- Formalization: zeta partly inspected; Dirichlet/Hecke declarations also located
- Statement coverage: not inspected
- Dependencies: no (cubic first-moment paper cited, unused)
- Antecedents: —

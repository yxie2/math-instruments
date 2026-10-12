---
id: openai-math-325
record_type: family
title: The complete Crouzeix conjecture
source_family: '325'
source_collection: openai/math
batch_id: B001
original_group: 2
subject: Operator algebras, topology and symplectic geometry
source_paper_ids:
- P-000016
- P-000066
instrument_ids:
- MI-000107
- MI-000108
- MI-000109
headline: Complete (matrix-valued) Crouzeix conjecture
central_instrument: '“Ordered density comparison”: compress the Crouzeix–Palencia positive kernel by the top singular pair into a $`2\times2`$ block of boundary matrix functions and measure in Hilbert–Schmidt norm, so Parseval over Faber coefficients replaces the triangle inequality that gave $`1+\sqrt{2}`$.'
novelty_assessment: combination leaning new
formalization_summary: files, five challenges
statement_faithfulness: yes, full cb statement
dependencies: 'no'
antecedents: Luo 2026 (novelty comparison incomplete)
review_status: imported-from-direction-paper
updated: '2026-10-12'
source_status_line: Lean, all sizes, matrix-valued, arbitrary Hilbert space combination leaning new
map_formalization_summary: 'yes'
---

# The complete Crouzeix conjecture

[Family index](../../tables/families.md) · [Batch B001](../../batches/B001/README.md)

The statements and assessments below report the direction paper’s extraction. They do not certify the source proofs.

## Source manuscripts

- [P-000016](../papers/P-000016.md)
- [P-000066](../papers/P-000066.md)

## Family description

Source status as recorded in the direction paper: Lean, all sizes, matrix-valued, arbitrary Hilbert space combination leaning new

For every bounded operator $`A`$ on a nonzero complex Hilbert space, including infinite-dimensional spaces, and every matrix polynomial $`P(z)=\sum_k B_kz^k`$, the stated complete inequality is
``` math
\left\|\sum_k A^k\otimes B_k\right\|
 \le2\sup_{z\in W(A)}\|P(z)\|
 =2\max_{z\in\overline{W(A)}}\|P(z)\|.
```
The constant 2 is sharp. The numerical range need not be closed in infinite dimension, which is why the supremum or its closure is used. The holomorphic extension concerns matrix-valued functions holomorphic on an open neighborhood of $`\overline{W(A)}`$; rational functions must have all their poles outside $`\overline{W(A)}`$. In this sense the closure is a complete 2-spectral set. Scalar proofs are presented in the 2026 preprints of Jin, Lorist–Schwenninger and Luo [source](../../direction/references.md#src:jin) [source](../../direction/references.md#src:lorist) [source](../../direction/references.md#src:luo). Lorist–Schwenninger explicitly explain why their proof and Jin’s do not directly give the completely bounded version.

## Extracted instruments.

- [MI-000107: Ordered density comparison](../instruments/MI-000107.md)

- [MI-000108: Exterior Faber coefficients and the positive kernel](../instruments/MI-000108.md)

- [MI-000109: Optimal metric and endpoint extremal](../instruments/MI-000109.md)

## Reused.

Delyon–Delyon and Crouzeix–Palencia double-layer positivity; exterior conformal maps and Faber polynomials; Paulsen’s similarity theorem; Stein 1952; Sz.-Nagy dilation; Katsnelson–Kheifets–Yuditskii colligations.

## Caveats.

The structural theorem applies separately to each enclosing domain strictly containing $`\overline{W(A)}`$; no limiting similarity on the closure is asserted. Luo’s scalar argument also uses a top singular pair [source](../../direction/references.md#src:luo), so that ingredient alone is not evidence of novelty. The relation between its boundary certificates and the matrix-valued argument here requires closer comparison.

## Recorded assessment

- Novelty: combination leaning new
- Formalization: files, five challenges
- Statement coverage: yes, full cb statement
- Dependencies: no
- Antecedents: Luo 2026 (novelty comparison incomplete)

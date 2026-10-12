---
id: openai-math-362
record_type: family
title: Relativistic Vlasov–Maxwell, 3D, large data
source_family: '362'
source_collection: openai/math
batch_id: B001
original_group: 1
subject: Analysis and geometry
source_paper_ids:
- P-000041
instrument_ids:
- MI-000019
- MI-000020
- MI-000021
headline: 3D relativistic Vlasov–Maxwell, large data, global smooth
central_instrument: '“Signed momentum increment” bootstrap: bound the net impulse on a particle over a short interval, not the force pointwise, via a signed Liénard–Wiechert identity along source worldlines; each momentum doubling costs time $`\ge c/\log P`$, and the harmonic sum diverges.'
novelty_assessment: combination; direction-change counting new
formalization_summary: files, continuation statement included
statement_faithfulness: yes; uniqueness among global classical solutions
dependencies: 'no'
antecedents: Cheverry–Ibrahim 2025
review_status: imported-from-direction-paper
updated: '2026-10-12'
source_status_line: Lean, 207 files, continuation step included combination
map_formalization_summary: 'yes'
---

# Relativistic Vlasov–Maxwell, 3D, large data

[Family index](../../tables/families.md) · [Batch B001](../../batches/B001/README.md)

The statements and assessments below report the direction paper’s extraction. They do not certify the source proofs.

## Source manuscripts

- [P-000041](../papers/P-000041.md)

## Family description

Source status as recorded in the direction paper: Lean, 207 files, continuation step included combination

For the one-species system with no background charge, the source assumes
``` math
\begin{gathered}
 f_0\in C_c^\infty(\mathbb R_x^3\times\mathbb R_v^3),\qquad f_0\ge0,\\
 E_0,B_0\in C_b^\infty(\mathbb R^3;\mathbb R^3)\cap L^2(\mathbb R^3;\mathbb R^3),\\
 \nabla\cdot E_0=\rho_{f_0},\qquad \nabla\cdot B_0=0,\qquad
 \rho_{f_0}(x)=\int_{\mathbb R^3}f_0(x,v)\,dv.
\end{gathered}
```
Here every spatial derivative of the fields is bounded, the fields have finite energy, and the nonnegative phase-space datum is smooth and compactly supported. Under these hypotheses the paper claims a unique global classical solution, smooth on each finite time interval and with compact phase-space support there, without a size restriction. The repository supplies a formalization covering a continuation statement; it was not compiled or kernel-checked for this survey.

## Extracted instruments.

- [MI-000019: Signed momentum increment bootstrap](../instruments/MI-000019.md)

- [MI-000020: Signed force identity along source labels](../instruments/MI-000020.md)

- [MI-000021: Occupation of retarded bins, direction-change counting, selection](../instruments/MI-000021.md)

## Reused.

Glassey–Strauss representation; Luk–Strain cone flux; Lazarovici label change; Pallard’s cone Jacobians; Pfaffelmoser; Kirchhoff; Gagliardo–Nirenberg; Picard.

## Caveats.

The reasoning summary states that the cited continuation theorem alone does not establish the required estimates, whereas the paper presents them as proved. Cheverry–Ibrahim is cited six times in the summary and omitted from the paper. The exponent comparison has a small margin. A repository formalization is supplied, but no machine check was run for this survey. Uniqueness is asserted only among global classical solutions.

## Recorded assessment

- Novelty: combination; direction-change counting new
- Formalization: files, continuation statement included
- Statement coverage: yes; uniqueness among global classical solutions
- Dependencies: no
- Antecedents: Cheverry–Ibrahim 2025

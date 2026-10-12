---
id: openai-math-143
record_type: family
title: Hilbert’s sixteenth problem, uniform bounds
source_family: '143'
source_collection: openai/math
batch_id: B001
original_group: 2
subject: Analysis, dynamics and mathematical physics
source_paper_ids:
- P-000080
- P-000081
instrument_ids:
- MI-000068
- MI-000069
- MI-000070
headline: 'Hilbert’s 16th: $`H(n)<\infty`$ for every degree'
central_instrument: Parametric Lion–Rolin preparation of the slope field, coefficients as parameters, in place of blow-ups, giving a finite alphabet of passages uniform over degeneracies; a Khovanskii-type projection principle turns non-uniform finiteness into a uniform bound; Ilyashenko’s cochains re-engineered into multi-scale “packets”.
novelty_assessment: combination
formalization_summary: companion (quintic Liénard) only
statement_faithfulness: —
dependencies: 'no'
antecedents: —
review_status: imported-from-direction-paper
updated: '2026-10-12'
source_status_line: not formalized (companion only) combination
map_formalization_summary: no (companion only)
---

# Hilbert’s sixteenth problem, uniform bounds

[Family index](../../tables/families.md) · [Batch B001](../../batches/B001/README.md)

The statements and assessments below report the direction paper’s extraction. They do not certify the source proofs.

## Source manuscripts

- [P-000080](../papers/P-000080.md)
- [P-000081](../papers/P-000081.md)

## Family description

Source status as recorded in the direction paper: not formalized (companion only) combination

For each degree d there is a finite B(d) bounding the number of limit cycles of every real planar polynomial vector field of degree $`\le d`$: the uniform-boundedness assertion in the second part of Hilbert’s sixteenth problem. The bound is ineffective; Écalle–Ilyashenko individual finiteness is not used as a premise. The manuscript has 160 pages. The companion concerns the classical Liénard system $`\dot x=y-F(x)`$, $`\dot y=-x`$, with $`\deg F\le5`$; it claims at most two isolated periodic orbits. The repository supplies a formalization of this self-contained companion.

## Extracted instruments.

- [MI-000068: Packets on saturated logarithmic flags and the separation theorem](../instruments/MI-000068.md)

- [MI-000069: Absolute isolated-zero finiteness and projection count](../instruments/MI-000069.md)

- [MI-000070: Finite passage templates and matching systems](../instruments/MI-000070.md)

## Reused.

Lion–Rolin and Opris preparation; Bierstone–Milman and Gabrielov uniform finiteness; Khovanskii’s Rolle; Gevrey truncation; Ilyashenko–Yakovenko cyclic systems; rotated vector fields to make cycles hyperbolic.

## Caveats.

The paper cites Yeung 2025 for a gap in Ilyashenko 1991 at a differential-closure step and claims to repair it through differentiated implicit calculus. That assertion and Sections 6–8, which devote 80 pages to checking packet hypotheses for four transfer models, merit detailed examination. Degenerate singularities and polycycles are not named outside the introduction. The literature comparison was limited.

## Recorded assessment

- Novelty: combination
- Formalization: companion (quintic Liénard) only
- Statement coverage: —
- Dependencies: no
- Antecedents: —

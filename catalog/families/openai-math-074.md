---
id: openai-math-074
record_type: family
title: Kakeya maximal conjecture in ℝ³; Kakeya sets in ℝ⁴
source_family: '074'
source_collection: openai/math
batch_id: B001
original_group: 1
subject: Analysis and geometry
source_paper_ids:
- P-000032
- P-000058
instrument_ids:
- MI-000013
- MI-000014
- MI-000015
headline: Kakeya maximal conjecture in $`\mathbb{R}^{3}`$; Kakeya sets in $`\mathbb{R}^{4}`$ have dimension 4
central_instrument: 'Differentiate the critical exponent: BV gives approximate differentiability of the exponent surface; a separate monotonicity argument yields an ordinary differentiability point whose partial derivatives prescribe extremal configurations ruled out by an entropy and mutual-information bound. In 4D, a variational “horizon” built from quadratic local fits replaces polynomial Wolff axioms.'
novelty_assessment: combination leaning new; 4D framework new
formalization_summary: 'no'
statement_faithfulness: —
dependencies: '3D: alternative route only. 4D: cites 3D for a lemma that is really GWZ 2026'
antecedents: Rios–Sawyer
review_status: imported-from-direction-paper
updated: '2026-10-12'
source_status_line: not formalized combination leaning new (3D) new framework (4D)
map_formalization_summary: 'no'
---

# Kakeya maximal conjecture in ℝ³; Kakeya sets in ℝ⁴

[Family index](../../tables/families.md) · [Batch B001](../../batches/B001/README.md)

The statements and assessments below report the direction paper’s extraction. They do not certify the source proofs.

## Source manuscripts

- [P-000032](../papers/P-000032.md)
- [P-000058](../papers/P-000058.md)

## Family description

Source status as recorded in the direction paper: not formalized combination leaning new (3D) new framework (4D)

The sources claim $`\|K_\delta f\|_{L^3(S^2)}\le C_\varepsilon\delta^{-\varepsilon}\|f\|_{L^3}`$ in $`\mathbb{R}^{3}`$ (the maximal conjecture, stronger than the Wang–Zahl set conjecture), and every set in $`\mathbb{R}^{4}`$ containing a unit segment in every direction has Hausdorff dimension 4, without measurability or compactness assumptions. The manuscripts have 97 and 175 pages. The earlier bound cited by the initial extraction in $`\mathbb{R}^{4}`$ is 3.059.

## Extracted instruments.

- [MI-000013: Deformed critical-exponent surface with BV selection](../instruments/MI-000013.md)

- [MI-000014: Two-frame entropy transfer of projection theorems](../instruments/MI-000014.md)

- [MI-000015: Chart/horizon framework with narrowness trichotomy](../instruments/MI-000015.md)

## Reused.

GWZ 2026 convex-clustering estimate (reformulated as a weighted plank lemma, the real dependence of 4D on 3D); Ren–Wang, Wang–Wu; multilinear Kakeya; Hochman–Shmerkin entropy across scales; Orponen–Shmerkin; Christ’s quasiextremals; Basu–Pollack–Roy.

## Caveats.

The two manuscripts total 272 pages and use nested limits, slow diagonal choices, triangular subsequences and almost-everywhere offsets. Their order of limits needs detailed checking beyond the selected comparisons made here. The three-dimensional argument cites another unformalized OpenAI restriction paper as an alternative route. The initial extraction identifies Rios–Sawyer as an uncited antecedent. Literature comparisons remain incomplete.

## Recorded assessment

- Novelty: combination leaning new; 4D framework new
- Formalization: no
- Statement coverage: —
- Dependencies: 3D: alternative route only. 4D: cites 3D for a lemma that is really GWZ 2026
- Antecedents: Rios–Sawyer

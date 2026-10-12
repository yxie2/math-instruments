---
id: openai-math-007
record_type: family
title: Ordinary two-point Chowla
source_family: '007'
source_collection: openai/math
batch_id: B001
original_group: 2
subject: Number theory and arithmetic geometry
source_paper_ids:
- P-000046
instrument_ids:
- MI-000056
- MI-000057
- MI-000058
headline: Ordinary two-point Chowla; corrected binary Elliott
central_instrument: '“Terminal-scale divisor bins”: dilations confined so narrowly that the scale is unchanged, removing Tao’s logarithmic averaging; integers certified to behave like independent residues by Braverman’s theorem that polylog independence fools $`\mathrm{AC}^{0}`$.'
novelty_assessment: combination bordering new
formalization_summary: 'original: statements; docs report coverage, unbuilt'
statement_faithfulness: —
dependencies: 'no'
antecedents: —
review_status: imported-from-direction-paper
updated: '2026-10-12'
source_status_line: repository reports Lean coverage; comparator and solution coverage not independently checked here combination bordering new
map_formalization_summary: 'original: statements only; see card'
---

# Ordinary two-point Chowla

[Family index](../../tables/families.md) · [Batch B001](../../batches/B001/README.md)

The statements and assessments below report the direction paper’s extraction. They do not certify the source proofs.

## Source manuscripts

- [P-000046](../papers/P-000046.md)

## Family description

Source status as recorded in the direction paper: repository reports Lean coverage; comparator and solution coverage not independently checked here combination bordering new

For fixed integers $`a_1,a_2\ge1`$ and $`b_1,b_2\ge0`$ satisfying $`a_1b_2-a_2b_1\ne0`$, the source claims
``` math
\left|\sum_{1\le n\le X}\lambda(a_1n+b_1)\lambda(a_2n+b_2)\right|
 \le C_{a_1,a_2,b_1,b_2}\frac{X}{(\log X)^c}\qquad(X\ge3).
```
The exponent $`c>0`$ is absolute; the implied constant can depend on the fixed forms, and no uniformity for coefficients growing with $`X`$ is asserted. The corrected binary Elliott conclusion is qualitative, under uniform non-pretentiousness of an original factor and the same conditions on the affine forms. The initial extraction describes ordinary two-point Chowla as open before this release. The exponent is not given numerically.

## Extracted instruments.

- [MI-000056: Terminal-scale divisor bins with padding anti-concentration](../instruments/MI-000056.md)

- [MI-000057: Finite residue comparison via Braverman’s theorem](../instruments/MI-000057.md)

- [MI-000058: Degree-normalized two-band divisor graph with matched centering](../instruments/MI-000058.md)

## Reused.

Helfgott–Radziwiłł divisibility graph and prohibited paths; Pilatte’s composite labels and non-backtracking operator; Matomäki–Radziwiłł–Tao short sums (corrected 2022 version); Granville–Soundararajan distance; Brun truncation.

## Caveats.

The reasoning summary makes the conclusion conditional on simultaneous-witness elimination, forest counting, finite-residue comparison and spectral-transfer bounds, while the paper states these steps as proved. They are the main points identified for further checking. Part II gives no rate.

## Recorded assessment

- Novelty: combination bordering new
- Formalization: original: statements; docs report coverage, unbuilt
- Statement coverage: —
- Dependencies: no
- Antecedents: —

---
id: openai-math-158
record_type: family
title: The plane is not 5-colorable
source_family: '158'
source_collection: openai/math
batch_id: B001
original_group: 1
subject: Combinatorics and theoretical computer science
source_paper_ids:
- P-000055
instrument_ids:
- MI-000034
- MI-000035
- MI-000036
headline: The plane is not 5-colorable
central_instrument: '“Transfer of colorability”: a proper k-coloring exists iff a weak measurable one does, via a rigidity theorem that every wild rotation-invariant law on the dual of the algebraic plane is Haar. The only finite graph used is a Moser spindle in the final step.'
novelty_assessment: new
formalization_summary: ≈ 24, 500 lines
statement_faithfulness: yes, unrestricted
dependencies: 'no'
antecedents: —
review_status: imported-from-direction-paper
updated: '2026-10-12'
source_status_line: Lean, unrestricted statement, $`\approx 24{,}500`$ lines new
map_formalization_summary: 'yes'
---

# The plane is not 5-colorable

[Family index](../../tables/families.md) · [Batch B001](../../batches/B001/README.md)

The statements and assessments below report the direction paper’s extraction. They do not certify the source proofs.

## Source manuscripts

- [P-000055](../papers/P-000055.md)

## Family description

Source status as recorded in the direction paper: Lean, unrestricted statement, $`\approx 24{,}500`$ lines new

Every 5-coloring of $`\mathbb{R}^{2}`$ with arbitrary color classes has a monochromatic unit pair, so the chromatic number of the plane is 6 or 7, in ZFC. The formal statement is literally $`\neg\exists\, c:\mathbb{C}\to\mathrm{Fin}\,5`$ proper. The proof uses neither a SAT solver nor a vertex list; its argument is structural and ergodic.

## Extracted instruments.

- [MI-000034: Transfer of colorability via Haar rigidity of wild character laws](../instruments/MI-000034.md)

- [MI-000035: Angular palettes, binary centers, transition graph](../instruments/MI-000035.md)

- [MI-000036: Common exclusion continua](../instruments/MI-000036.md)

## Reused.

de Bruijn–Erdős; Falconer, Payne; Furstenberg–Zimmer; Bochner/SNAG; Følner means; Fourier decay of the circle; Brouwer; Hatcher covering theory; Moser spindle with a rational placement certificate.

## Caveats.

The rigidity theorem is dense and relies on a transfinite induction; the initial extraction places it inside the Lean closure (Rigidity.lean). The inspected comparator configuration disables the optional nanoda independent kernel recheck; no build was run here. The paper never exhibits a finite 6-chromatic graph, consistent with the method. A footnote disputes a pseudonymous manuscript; that dispute is not assessed here.

## Recorded assessment

- Novelty: new
- Formalization: ≈ 24, 500 lines
- Statement coverage: yes, unrestricted
- Dependencies: no
- Antecedents: —

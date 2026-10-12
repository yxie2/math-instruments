---
id: openai-math-285
record_type: family
title: Baum–Connes and Kadison–Kaplansky counterexamples
source_family: '285'
source_collection: openai/math
batch_id: B001
original_group: 2
subject: Operator algebras, topology and symplectic geometry
source_paper_ids:
- P-000007
- P-000008
- P-000023
instrument_ids:
- MI-000095
- MI-000096
- MI-000097
headline: Reduced Baum–Connes injectivity fails (torsion-free)
central_instrument: '“Heisenberg voltage tower”: relators are nilpotent-group covers of an expander tower so each layer carries $`\ell^2(H)`$ and incidence operators realize Bott-class symbols; an Eilenberg swindle makes the embedded torus class vanish.'
novelty_assessment: combination
formalization_summary: 'no'
statement_faithfulness: —
dependencies: methodological on the Kadison–Kaplansky companion; none on 196/197
antecedents: —
review_status: imported-from-direction-paper
updated: '2026-10-12'
source_status_line: not formalized combination reduced assembly-map scope
map_formalization_summary: 'no'
---

# Baum–Connes and Kadison–Kaplansky counterexamples

[Family index](../../tables/families.md) · [Batch B001](../../batches/B001/README.md)

The statements and assessments below report the direction paper’s extraction. They do not certify the source proofs.

## Source manuscripts

- [P-000007](../papers/P-000007.md)
- [P-000008](../papers/P-000008.md)
- [P-000023](../papers/P-000023.md)

## Family description

Source status as recorded in the direction paper: not formalized combination reduced assembly-map scope

The source constructs a finitely generated torsion-free group $`G_{inj}`$, an injection $`\mathbb{Z}^2\to G`$ and a degree-2 class pairing to 1 with the torus, such that the Bott class dies in $`K_0(C^*_rG)`$: rational injectivity of the reduced, coefficient-free assembly map fails. The claim does not contradict classical Novikov or maximal injectivity (Hanke–Schick). The source asserts finite generation; it establishes neither finite presentation nor its failure. The corrected Antonini–Buss–Engel–Siebenand result concerns specified exotic group $`C^*`$-algebras for finitely presented groups; identifying its target with the reduced algebra needs an additional condition, such as exactness, which is also not supplied here. Companions: a torsion-free group with a projection of trace in $`(0,1/2)`$ (surjectivity failure, Kadison–Kaplansky fails) and a group with p-torsion and an irrational-trace projection.

## Extracted instruments.

- [MI-000095: Heisenberg voltage tower with simultaneously sampled Bott symbols](../instruments/MI-000095.md)

- [MI-000096: Parity-swindle Bott cancellation in a norm-sequence quotient](../instruments/MI-000096.md)

- [MI-000097: Sheet-cone complex, exact cone chains, prime-order obstruction, Shapiro extension](../instruments/MI-000097.md)

## Reused.

Baum–Connes–Higson; Lück’s trace theorem; an integrality attribution to Bartels–Greenlees–Wegner left unresolved by the initial extraction; Hanke–Schick; Emerson–Hudson; Kasparov descent; graphical small cancellation; Osajda labelling; LLL; Rieffel projections; Dykema–Rørdam.

## Caveats.

The construction uses large parameters (s a multiple of 20,000, scales $`2^{500H_i}`$). Their order of choice and the claimed absence of circular dependence require close checking. All three papers share the architecture, so a defect in it could affect the whole family. The main paper adapts and reproves methods from the Kadison–Kaplansky companion, which cites an unrefereed GitHub note as motivation. The comparison used directly retrieved primary sources without a fresh literature search.

## Recorded assessment

- Novelty: combination
- Formalization: no
- Statement coverage: —
- Dependencies: methodological on the Kadison–Kaplansky companion; none on 196/197
- Antecedents: —

---
id: openai-math-263
record_type: family
title: The ionization conjecture
source_family: '263'
source_collection: openai/math
batch_id: B001
original_group: 2
subject: Analysis, dynamics and mathematical physics
source_paper_ids:
- P-000038
- P-000039
- P-000074
instrument_ids:
- MI-000071
- MI-000072
- MI-000073
headline: Ionization conjecture, full Schrödinger theory
central_instrument: Condition a many-body ground state on noisy, unlabeled coarse-grained observations of electron positions; the energy cost is logarithmic in the event probability and free of particle number, so local failures of Thomas–Fermi yield low-energy states that contradict semiclassics.
novelty_assessment: new
formalization_summary: companions only (607 + 428 files); headline none
statement_faithfulness: companions faithful
dependencies: companions depend on main paper’s foundation estimates
antecedents: —
review_status: imported-from-direction-paper
updated: '2026-10-12'
source_status_line: headline not formalized; companions yes new
map_formalization_summary: companions only
---

# The ionization conjecture

[Family index](../../tables/families.md) · [Batch B001](../../batches/B001/README.md)

The statements and assessments below report the direction paper’s extraction. They do not certify the source proofs.

## Source manuscripts

- [P-000038](../papers/P-000038.md)
- [P-000039](../papers/P-000039.md)
- [P-000074](../papers/P-000074.md)

## Family description

Source status as recorded in the direction paper: headline not formalized; companions yes new

The source uses the nonrelativistic fermionic Coulomb Hamiltonian on $`\bigwedge^n L^2(\mathbb R^3;\mathbb C^2)`$, with two electron spin states and kinetic term $`-\Delta/2`$. The $`M\ge1`$ fixed nuclei have distinct positions $`R_j`$ and real charges $`z_j\ge1`$; $`Z=\sum_{j=1}^M z_j`$ is total nuclear charge. The system’s net charge in electron-charge units is $`Z-n`$, and excess electron number is $`n-Z`$. Nuclear repulsion is omitted as a constant independent of $`n`$. For the ground-energy infima $`E_n`$ (with $`E_0=0`$), strict binding $`E_n<E_{n-1}`$ is claimed to imply $`n\le Z+CM`$, with universal $`C`$; threshold bound states are not excluded. For a neutral atom with one nucleus at the origin and integer $`Z\ge1`$, let $`\rho_{\Psi_Z}`$ be the spin-summed density of any normalized ground state, of total mass $`Z`$. Its outer half-electron radius is
``` math
R(\Psi_Z)=\inf\left\{r\ge0:\int_{|x|>r}\rho_{\Psi_Z}(x)\,dx\le\frac12\right\}.
```
The stated bounds are $`0<c\le R(\Psi_Z)\le C`$ and $`0<c\le I_1(Z):=E_Z(Z-1)-E_Z(Z)\le C`$, uniformly in such $`Z`$. The radius retains a fixed exterior mass, not a fixed fraction of all electrons. The initial extraction lists repository formalizations for two Thomas–Fermi asymptotic companions (607 and 428 files), not an independently checked proof of the main strict-binding assertion.

## Extracted instruments.

- [MI-000071: Noisy-observation conditioning with a dimension-free tilt cost](../instruments/MI-000071.md)

- [MI-000072: Conditional density determines the field](../instruments/MI-000072.md)

- [MI-000073: Outward propagation by convexity-preserved subsolutions under observation forgetting](../instruments/MI-000073.md)

## Reused.

Lieb’s 1984 bound; Zhislin binding; IMS localization; Lewin’s sector localization; Lieb–Thirring; Lieb–Simon Neumann bracketing and Thomas–Fermi theory; Solovej’s coherent states and exterior screened-potential strategy; Bénilan–Brezis.

## Caveats.

The argument has many quantitative parameters ($`L=10^6`$, exponents 1.01, probabilities $`r^{25}`$, $`r^{40}`$); the full bookkeeping was not checked. The formalization catalogue marks “Partial progress”, review “unchecked”, and omits the radii development from its results list. The literature comparison was limited.

## Recorded assessment

- Novelty: new
- Formalization: companions only (607 + 428 files); headline none
- Statement coverage: companions faithful
- Dependencies: companions depend on main paper’s foundation estimates
- Antecedents: —

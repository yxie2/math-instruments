# B059: Torsor alignment, sparse supports and protected transfers

Extraction date: 2026-10-16. This batch adds 4 families, 8 source manuscripts and 8 instruments.

## Instruments

| Instrument | Family |
| --- | --- |
| [MI-000570: Absorb a countable bit matrix with finite row and column translations](../../catalog/instruments/MI-000570.md) | 240 |
| [MI-000571: Recover a class and its strong maps from small pairs before uniformizing](../../catalog/instruments/MI-000571.md) | 240 |
| [MI-000572: Concentrate an edge cochain by subtracting three prefix gradients](../../catalog/instruments/MI-000572.md) | 243 |
| [MI-000573: Control all small components by a projection boundary budget](../../catalog/instruments/MI-000573.md) | 243 |
| [MI-000574: Use faithful disjoint strips to justify stable group identities](../../catalog/instruments/MI-000574.md) | 247 |
| [MI-000575: Lift inverses and elementwise finite orders through a matrix-nil ideal](../../catalog/instruments/MI-000575.md) | 247 |
| [MI-000576: Factor a sparse masked operator through edges with their labels retained](../../catalog/instruments/MI-000576.md) | 251 |
| [MI-000577: Transfer nearby metrics while protecting a prescribed subspace](../../catalog/instruments/MI-000577.md) | 251 |

## Source and method

Pinned source revision: [`1581d4cbdd69a0faf34b2089614fe2a814316a6a`](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a). The [source manifest](../../sources/batches/B059.json) records hashes, exact labels and manuscript coverage.

Eight instruments from four families and all eight associated manuscripts. Complete selected arguments were read, with direct primary comparisons to Vasey, Weibel and Higham. All four scope documents and all six linked Comparators were read in full.

## Mathematical checks and scope

The [verification program](verification/check_instruments.py) and [results](verification/results.json) contain eight groups: countable-matrix windows, coherent finite diagrams, sparse grid cochains, component mass, faithful strips, matrix-nil periodicity, indexed masked operators and protected metric transfer.

The AEC uniformity step is an equivalence, not a proof of eventual categoricity. Matrix periodicity alone does not establish a 2-group or torsion in a Steinberg kernel. Finite diagram checks do not certify transfinite coding; matrix checks do not certify an abstract presented-group kernel. No Lean solution was built and no source headline theorem is certified. The fixed edition is unchanged.

Proposed applications are not subsequent results. No independent human review or exhaustive novelty certification is claimed.

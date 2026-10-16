# B029: Local geometry constructions and interval certificates

Extraction date: 2026-10-16. This batch adds 4 previously uncatalogued families, 4 source manuscripts and 8 instruments. The original groups of 17 and 21 families remain together in B001.

## Instruments

| Instrument | Family |
| --- | --- |
| [MI-000336: Prescribe the mean of a loop by a smoothly varying positive density](../../catalog/instruments/MI-000336.md) | 333 |
| [MI-000337: Prescribe a transverse derivative on curves while keeping the function uniformly small](../../catalog/instruments/MI-000337.md) | 333 |
| [MI-000338: Realize a small arbitrary curvature function through a scalar ODE](../../catalog/instruments/MI-000338.md) | 334 |
| [MI-000339: Pay coordinate-scaling costs before summing accumulating local perturbations](../../catalog/instruments/MI-000339.md) | 334 |
| [MI-000340: Rearrange convex functions increasingly without losing convexity on a downward polytope](../../catalog/instruments/MI-000340.md) | 343 |
| [MI-000341: Construct relative area primitives and preserve moment faces in a Moser deformation](../../catalog/instruments/MI-000341.md) | 343 |
| [MI-000342: Use a convex flux defect instead of substituting a mean pointwise](../../catalog/instruments/MI-000342.md) | 354 |
| [MI-000343: Certify positivity between rational knots using an upper curvature bound](../../catalog/instruments/MI-000343.md) | 354 |

## Source and method

The source revision is [`1581d4cbdd69a0faf34b2089614fe2a814316a6a`](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a). Its preprint tree is identical to the B001 snapshot; intervening upstream commits changed repository administration. Records give exact manuscript bindings, labelled source passages and SHA-256 hashes in the [source manifest](../../sources/batches/B029.json).

Eight selected mechanisms from four differential-geometry families. Complete selected proofs were read. Khuri 2009 directly supplies the prescribed-curvature antecedent, and Siegel-Yao supplies the packing conjecture context. Five Comparator files were inspected. Global immersion, nonimmersion, packing and isoperimetric claims are not certified.

## Mathematical checks and scope

The [verification program](verification/check_instruments.py) and [results](verification/results.json) contain eight groups.

- Family 333: 96 positive density/patching models, a symbolic transverse derivative and 96 support budgets; a vertical-arc control retains the finite-tangency hypothesis.
- Family 334: symbolic curvature and tensor transformations, nine formal flat-jet ODE models, 3,320 derivative budgets and 192 tails. The local nonimmersion obstruction remains an unaudited input.
- Family 343: 40 rearrangement integrals, 400 convexity/monotonicity models, a symbolic relative primitive and 75 horizontal Moser matrices. No Hamiltonian realization or ball packing is constructed.
- Family 354: 400 scalar flux models and exact checks of all 23 source rational interpolation intervals, with minimum conditional margin 9/100000. The endpoint table and analytic second-derivative bounds are inputs; they are not independently reproduced.

All five Comparator files contain sorry targets; no Lean build was performed. The immutable import edition is unchanged.

Potential applications are labelled as proposals. This extraction adds no claim of independent human review or exhaustive novelty certification.

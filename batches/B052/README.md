# B052: Divisor variances, modular norms and geometric obstructions

Extraction date: 2026-10-16. This batch adds 4 families, 4 source manuscripts and 8 instruments.

## Instruments

| Instrument | Family |
| --- | --- |
| [MI-000512: Balance restriction slopes with a bounded monotone average](../../catalog/instruments/MI-000512.md) | 195 |
| [MI-000513: Extract a nonnegative variance from a Cartier-divisor lattice filtration](../../catalog/instruments/MI-000513.md) | 195 |
| [MI-000514: Cancel p-orbits to compare coefficient restriction with Brauer projection](../../catalog/instruments/MI-000514.md) | 202 |
| [MI-000515: Use dual-basis averaging to construct a central radical annihilator](../../catalog/instruments/MI-000515.md) | 202 |
| [MI-000516: Transfer projectivity through internal norms without a monoidal evaluation](../../catalog/instruments/MI-000516.md) | 208 |
| [MI-000517: Choose an independent Frobenius-constrained nullvector](../../catalog/instruments/MI-000517.md) | 208 |
| [MI-000518: Obstruct nonpositive curvature by incompatible torus orthogonality](../../catalog/instruments/MI-000518.md) | 358 |
| [MI-000519: Optimize a boundary penalty in the dual energy norm](../../catalog/instruments/MI-000519.md) | 358 |

## Source and method

Pinned source revision: [`1581d4cbdd69a0faf34b2089614fe2a814316a6a`](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a). The [source manifest](../../sources/batches/B052.json) records hashes, exact labels and manuscript coverage.

Eight selected instruments from families 195, 202, 208 and 358. Full selected source arguments were read and compared with Chen-Sun, Webb, Lorenz-Tokoly, Chebolu-Christensen-Minac, Coulembier-Flake and Leeb. The two available family scope documents and Comparator targets were read; families 202 and 208 have none listed in the pinned inventory.

## Mathematical checks and scope

The [verification program](verification/check_instruments.py) and [results](verification/results.json) check slope and variance arithmetic, divisor-layer identities, modular orbit projections, Higman averaging, projectivity norms, Moore nullvectors, torus gluing and boundary-penalty optimization.

The small Cohen-Macaulay Comparator asserts only ring properties, not the headline module nonexistence. None of the source counterexample, Alperin, fiber-functor or no-conjugate-points headline results is certified by these finite checks. No Lean solution was built; the fixed edition is unchanged.

Proposed applications are not subsequent results. No independent human review or exhaustive novelty certification is claimed.

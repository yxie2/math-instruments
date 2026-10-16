# B026: Restriction growth, polynomial certificates and curvature obstructions

Extraction date: 2026-10-16. This batch adds 4 previously uncatalogued families, 4 source manuscripts and 8 instruments. The original groups of 17 and 21 families remain together in B001.

## Instruments

| Instrument | Family |
| --- | --- |
| [MI-000312: Bound restriction images uniformly using only a fixed part of the generic fiber](../../catalog/instruments/MI-000312.md) | 038 |
| [MI-000313: Rationalize a supporting profile without changing which polytopes contain it](../../catalog/instruments/MI-000313.md) | 038 |
| [MI-000314: A polynomial certificate removes the denominator from a cylinder coordinate](../../catalog/instruments/MI-000314.md) | 047 |
| [MI-000315: Use an adapted filtration to preserve locally nilpotent derivations and their invariants](../../catalog/instruments/MI-000315.md) | 047 |
| [MI-000316: Normalize the ramified trace before taking an orthogonal quotient](../../catalog/instruments/MI-000316.md) | 048 |
| [MI-000317: A weighted divergence formula separates correctable jet orders from resonance](../../catalog/instruments/MI-000317.md) | 048 |
| [MI-000318: Keep the zero-set atoms when turning a squared seminorm into curvature](../../catalog/instruments/MI-000318.md) | 050 |
| [MI-000319: Two odd-order projective maps with a loxodromic product admit no finite invariant measure](../../catalog/instruments/MI-000319.md) | 050 |

## Source and method

The source revision is [`1581d4cbdd69a0faf34b2089614fe2a814316a6a`](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a). Its preprint tree is identical to the B001 snapshot; intervening upstream commits changed repository administration. Records give exact manuscript bindings, labelled source passages and SHA-256 hashes in the [source manifest](../../sources/batches/B026.json).

Eight instruments are extracted from four complex-geometry families. Complete selected proofs were read, with primary comparisons to Dutta-Lahiri residual-coordinate stabilization and Raufi singular metric theory. Two Comparator target files were inspected. The global conjecture-resolution and counterexample claims are not certified.

## Mathematical checks and scope

The [verification program](verification/check_instruments.py) and [results](verification/results.json) give eight check groups. SymPy is added to the shared finite-verification requirements for exact polynomial and algebraic-number calculations.

- Family 038: 432 hypersurface Hilbert-function comparisons, 240 residue-class estimates and 100 rational shared-face approximants. No minimizer or center-elimination theorem is verified.
- Family 047: exact source cylinder identities, derivation nilpotence, ideal certificate and a 381-term polynomial inverse; 1,152 graded-iterate and 192 LND order-product checks. A nonadapted generator set fails the shift bound. The source rigidity and non-polynomiality argument remains unaudited.
- Family 048: 64 ramified trace Gram matrices, 50 quotient norms, the splitting-count constraint, 48 bracket identities and 40 nonresonant volume corrections. The order-four resonance is retained. No curve, global gluing, contraction or algebraization is verified.
- Family 050: 44 singular radial metrics retain diffuse and atomic curvature mass. Exact source matrix orders, traces and eigenline conditions support the written invariant-measure obstruction. The quadratic-limit construction and ampleness proof remain unaudited.

The two Comparator files contain inspected target statements, not Lean proofs built here. Families 038 and 048 have no listed family-specific scope document. The immutable import edition is unchanged.

Potential applications are labelled as proposals. This extraction adds no claim of independent human review or exhaustive novelty certification.

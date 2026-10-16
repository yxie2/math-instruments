# B025: Finite algebra and chain mechanisms in topology

Extraction date: 2026-10-16. This batch adds 4 previously uncatalogued families, 4 source manuscripts and 8 instruments. The original groups of 17 and 21 families remain together in B001.

## Instruments

| Instrument | Family |
| --- | --- |
| [MI-000304: Lift a quasi-isomorphism through nilpotent labels and recover a positive power](../../catalog/instruments/MI-000304.md) | 306 |
| [MI-000305: Preserve an integral pairing by repeating a mod-two unit](../../catalog/instruments/MI-000305.md) | 306 |
| [MI-000306: A saturated initial flag defines a signed chain residue](../../catalog/instruments/MI-000306.md) | 310 |
| [MI-000307: Shuffle augmented flags into a product without losing the join sign](../../catalog/instruments/MI-000307.md) | 310 |
| [MI-000308: Diagonal transfer forces inverse-automorphism integration weights](../../catalog/instruments/MI-000308.md) | 314 |
| [MI-000309: Subgroup counts of Z_p^d stabilize to a nonzero p-adic unit](../../catalog/instruments/MI-000309.md) | 314 |
| [MI-000310: Cartier halving carries an explicit Dickson exponent floor](../../catalog/instruments/MI-000310.md) | 316 |
| [MI-000311: A decomposable primitive in a polynomial Hopf algebra has a primitive root](../../catalog/instruments/MI-000311.md) | 316 |

## Source and method

The source revision is [`1581d4cbdd69a0faf34b2089614fe2a814316a6a`](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a). Its preprint tree is identical to the B001 snapshot; intervening upstream commits changed repository administration. Records give exact manuscript bindings, labelled source passages and SHA-256 hashes in the [source manifest](../../sources/batches/B025.json).

Eight instruments are extracted from four topology families. Complete selected algebraic proofs were read, with primary comparisons to Nakayama, Strickland groupoid character formulas and Tamanoi subgroup counts. The Hung author-report record was retrieved, but its full text was inaccessible; that comparison is explicitly limited. No global conjecture-resolution or novelty certification is claimed.

## Mathematical checks and scope

The [verification program](verification/check_instruments.py) and [results](verification/results.json) give eight exact finite check groups.

- Family 306: 12 nilpotent-ring complexes with nonfree homology, 12 sharp positive-power recurrences, all 1,638 matrices in GL_2 modulo 2, 4 and 8, and a torsion-containing chain complex. Floer construction and geometric gluing inputs remain unaudited.
- Family 310: 3,528 saturated-residue identities and 256 augmented shuffle identities. An unsaturated flag fails the residue rule. The component reductions and nonzero-cycle construction remain unaudited.
- Family 314: 288 groupoid functors, including 210 nonfaithful maps, 100 composition checks, 150 subgroup coefficient comparisons, 210 p-adic congruences and 224 triangular subgroup bases. No spectral character construction or chromatic gluing is verified.
- Family 316: 600 Steenrod-polynomial identities, 75 linear-change checks, 65 Dickson monomials, 90 floor checks and coproduct kernels through degree 24. The tensor obstruction and spherical-class classification remain unaudited.

No family-specific scope document or Comparator target is listed for these four families. No Lean build was performed. The immutable import edition is unchanged.

Potential applications are labelled as proposals. This extraction adds no claim of independent human review or exhaustive novelty certification.

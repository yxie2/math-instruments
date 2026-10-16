# B020: Combinatorial transfers and finite strategy certificates

Extraction date: 2026-10-16. This batch adds 4 previously uncatalogued families, 4 source manuscripts and 8 instruments. The original groups of 17 and 21 families remain together in B001.

## Instruments

| Instrument | Family |
| --- | --- |
| [MI-000263: Affine sign-pattern counting that retains boundary equalities](../../catalog/instruments/MI-000263.md) | 160 |
| [MI-000264: The first nonzero digit of a step transfers cyclic avoidance to product colorings](../../catalog/instruments/MI-000264.md) | 160 |
| [MI-000265: A strict kernel-density deficit gives an explicit finite-host threshold](../../catalog/instruments/MI-000265.md) | 161 |
| [MI-000266: Orthogonal fixed-density interpolation preserves nonconstancy at an exact equality](../../catalog/instruments/MI-000266.md) | 161 |
| [MI-000267: Principal-unit first-order maps and prime-to-residue torsion reduction](../../catalog/instruments/MI-000267.md) | 179 |
| [MI-000268: A binary identity couples two first-order character sums](../../catalog/instruments/MI-000268.md) | 179 |
| [MI-000269: Owned envelope intersections compose finite certificates against every reply](../../catalog/instruments/MI-000269.md) | 187 |
| [MI-000270: Reduced envelopes normalize exactly and commute with template composition](../../catalog/instruments/MI-000270.md) | 187 |

## Source and method

The source revision is [`1581d4cbdd69a0faf34b2089614fe2a814316a6a`](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a). Its preprint tree is identical to the B001 snapshot; intervening upstream commits changed repository administration. Records give exact manuscript bindings, labelled source passages and SHA-256 hashes in the [source manifest](../../sources/batches/B020.json).

This batch extracts eight combinatorial mechanisms from four families. Selected proofs were read in full, with primary comparisons to Stanley arrangements, Fox-Hunter digit/product methods, Lovasz-Szegedy sampling and Sieben proof trees. Seven Comparator definitions and targets were inspected; the literal older Snaky table was not reviewed entry by entry. The 21-move Snaky certificate received a complete finite reconstruction with a separately written parser.

## Mathematical checks and scope

The [verification program](verification/check_instruments.py) and [results](verification/results.json) contain eight check groups. The pinned Snaky certificate is included under its source Apache 2.0 license, with [provenance](verification/data/NOTICE.txt).

- Family 160: 36 affine arrangements and all two-digit lifts of 212 small valid cyclic colorings were checked, including composite bases and 44,052 integer progressions. The central superexponential coloring construction was not audited.
- Family 161: 18 exact expected-density models and nine even-subgraph expansions were checked. A triangle is only a small model of the interpolation argument; the claimed bipartite deficit was not verified.
- Family 179: 1,044 principal-unit product/inverse models and all 16 binary sign quadruples were checked. The odd-order alternating-product input is retained as a substantial unverified premise; no full Hadamard classification is certified.
- Family 187: the upstream short verifier passed. A separate parser reconstructed 728 numbered cards and 898 inline nodes, checking all 1,620 compositions, 4,089 references and 37,042 local reply classes. The final card has zero required cells, support size 251 and height 21. Normalization was checked at every node and in 1,000 additional finite models. This is complete finite reconstruction together with a read soundness argument, not an executable policy test, a proof of optimality or a Lean build. The older 25- and 35-move tables were not reconstructed.

Seven Comparator targets were inspected; no solution was built or kernel-checked. The actual SnakyConditional target is a global 35-move strategy, despite the scope table describing it as conditional templates. The fixed import edition remains unchanged.

Potential applications are labelled as proposals. This extraction adds no claim of independent human review or exhaustive novelty certification.

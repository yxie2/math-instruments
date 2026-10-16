# B021: Logical recovery and witness-preserving constructions

Extraction date: 2026-10-16. This batch adds 4 previously uncatalogued families, 4 source manuscripts and 9 instruments. The original groups of 17 and 21 families remain together in B001.

## Instruments

| Instrument | Family |
| --- | --- |
| [MI-000271: Four-value oracle recovery through a bounded binary feedback recurrence](../../catalog/instruments/MI-000271.md) | 241 |
| [MI-000272: Dense finite oracle transcripts remove auxiliary real parameters](../../catalog/instruments/MI-000272.md) | 241 |
| [MI-000273: Freeze inactive branches to preserve complete polynomial-witness uniqueness](../../catalog/instruments/MI-000273.md) | 242 |
| [MI-000274: A shifted inverse identity gives one natural-number code for each rational](../../catalog/instruments/MI-000274.md) | 242 |
| [MI-000275: Large-base binomial digits test binary containment with unique division witnesses](../../catalog/instruments/MI-000275.md) | 242 |
| [MI-000276: Ordinal slices assemble reverse injections from a classified seed](../../catalog/instruments/MI-000276.md) | 244 |
| [MI-000277: Least separating patterns select a coset covariantly](../../catalog/instruments/MI-000277.md) | 244 |
| [MI-000278: Finite derivations retain a system-wide normalization counterexample in a finite specification](../../catalog/instruments/MI-000278.md) | 245 |
| [MI-000279: Balanced signed dependencies turn mixed-variance equations into a Tarski operator](../../catalog/instruments/MI-000279.md) | 245 |

## Source and method

The source revision is [`1581d4cbdd69a0faf34b2089614fe2a814316a6a`](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a). Its preprint tree is identical to the B001 snapshot; intervening upstream commits changed repository administration. Records give exact manuscript bindings, labelled source passages and SHA-256 hashes in the [source manifest](../../sources/batches/B021.json).

Nine instruments are extracted from four logic families. The complete selected proofs were read, with primary comparisons to Sacks category avoidance as stated by Kumar-Shelah, Lutz-Siskind recovery, Cantone-Cuzziol-Omodeo single-fold specifications, Ryan-Smith local reflections of choice and Tarski fixed points. Five Comparator targets and their relevant definitions were inspected; no Lean solution was built.

## Mathematical checks and scope

The [verification program](verification/check_instruments.py) and [results](verification/results.json) give nine check groups.

- Family 241: 58 exact feedback recurrences, totaling 58,000 steps, and 256 finite cut-transcript tables. These test bounded discrepancy and transcript feasibility, not Borel uniformization, arbitrary oracle computation or the external representation theorem.
- Family 242: 36 complete guarded-case witness enumerations, 511 canonical rational codes, additional rational arithmetic and 5,151 exact binomial digit extractions. An unfrozen-variable control loses uniqueness. The single-fold power graph and machine compiler were not audited.
- Family 244: 500 finite slice presentations and 720 nonabelian selector/transport covariance checks. Computing at the unmoved data fails in 504 controls. Finite sets do not model the nonwellorderable branch or the forcing construction.
- Family 245: contextual beta-step sort support, including annotation reduction, and 180 mixed-order finite-lattice models with 32,760 comparable-pair checks. Controls retain a raw weakly normalizing term with an infinite reduction and an antitone map with no fixed point. The full candidate interface, observation-space and diagonal arguments were not audited.

The infinitary source hypotheses remain explicit. These finite models are not proof certification of the headline claims, and the primary comparisons are not exhaustive novelty audits. All five Comparator files contain targets rather than a proof build performed here. The immutable import edition is unchanged.

Potential applications are labelled as proposals. This extraction adds no claim of independent human review or exhaustive novelty certification.

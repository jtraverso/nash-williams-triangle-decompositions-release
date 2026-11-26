# Doubled ears: formal proof supplement

Juan Pablo Traverso Gianini  
Independent researcher, Santiago, Chile  
ORCID 0009-0003-6068-4096

*Companion to Sharp bounds for typed triangle absorbers of doubled ears*  
*Preprint 1.0 · 26 November 2026*

## 1. Statements checked in Lean

The formalization uses the predicate `IsAbsorber` of Paper II. It requires disjointness of $A$ and $P$ and mixed triangle decompositions of $A$ and $A\cup P$. The partition into two labels and the partition into three vertex roles are independent. In the table, declaration names are relative to `PartitionedTriangleAbsorption.SignedCertificate`.

| Namespace | Declaration | Conclusion |
|:--|:--|:--|
| DoubledEarEquality | `core_sensitive_bound` | Lower bound in Theorem 1 |
| DoubledEarEquality | `protected_centres_bound` | Lower bound with protected centres |
| DoubledEarEquality | `optimum_iff_routing_modes` | Equality in incidence form |
| DoubledEarEquality | `twoMode_of_routing_modes` | Transfer to the two-mode interface |
| TriangleFreeCore | `minimum_path_absorber` | Minimum 18 |
| LabelledPathMinimum | `minimum_labelled_path_absorber` | Minimum 21 |
| SubdividedClawMinimum | `minimum_subdivided_claw_absorber` | Minimum 36 |
| SubdividedClawMinimum | `no_connected_triple_partition` | Obstruction for the six-edge claw |

**Scope.** The formal lower bound counts the edges of $A$ whose two endpoints are centres. These are exactly $A\cap C$ under the induced-host assumption. The equality theorem assumes that $P$ consists of centre–ear edges in the host, all host edges of that type belong to $P$, all centre–centre edges belong to $C$, there are no ear–ear edges, and $|P|=4|C|$. Its conclusion characterizes equality by two mixed triangle packings of the specified role types with the same non-source edge set. The lemma `spoke_mem_iff` identifies the corresponding auxiliary neighbours at each centre. Section 2 derives the local permutations from these incidences for doubled ears. The transfer theorem additionally takes a mixed-decomposable return set disjoint from the host. For the family in Section 4, Lean checks the six-edge core, its optimum and its obstruction. The argument for arbitrary $k$ is the gluing and counting proof in that section.

## 2. Reproducing the verification

The [source commit](https://github.com/jtraverso/typed-triangle-absorption/tree/c7bae66dfd66370138d2f1a6ecc51d3aa29ea8e4) fixes Lean 4.35.0-rc3 and Mathlib revision `c55e6e786f49471c72fbddbec5415808896aec1e`. The [source ZIP](https://github.com/jtraverso/nash-williams-triangle-decompositions-release/releases/download/doubled-ears-preprint-1.0-r2/Doubled_ears_LEAN_SOURCE_v1.0.zip) contains all 1,588 tracked files, including 1,522 Lean source files and the dependency manifest. Lake obtains the external packages at the revisions recorded in that manifest.

After unpacking the archive, run the following commands from the directory containing `lean-toolchain`. The first command builds the statement and proof modules for this note. The second runs Comparator on a Linux installation with sandbox and Nanoda support.

```
lake build +DoubledEarsChallenge +DoubledEarsSolution
lake comparator --config comparator.doubled-ears.json
```

The challenge uses one `sorry` for each of the eight proposed statements. The solution imports the proofs through `DoubledEarsSolution`. Querying each declaration from that module reports exactly `propext`, `Classical.choice` and `Quot.sound`. On Windows the comparison used Lean’s default kernel with the sandbox and Nanoda disabled. The [verification record](https://github.com/jtraverso/nash-williams-triangle-decompositions-release/tree/doubled-ears-preprint-1.0-r2/series_notes/DOUBLED_EAR_ABSORBERS/preprint-1.0/formalization) gives the configuration and the output for all eight declarations.

**Source archive SHA-256**

`f740fb0a8db4003c2dd652d859feab62db259537c866037e0bb70a6906d195a2`

---
title: 'Triangle decompositions III: Physical typed absorption and prescribed statistics'
lang: en
version: '1.0'
date: '2026-11-01'
---

# Triangle decompositions III: Physical typed absorption and prescribed statistics

**Juan Pablo Traverso Gianini**  
Independent researcher, Santiago, Chile  
jtraverso@gmail.com  
ORCID: 0009-0003-6068-4096

**Paper III in the series Triangle decompositions.**  
**Preprint 1.0 — 1 November 2026.**

## Abstract

We study partitions of graph edges into triangles with prescribed combinations of vertex labels. We establish, with complete proofs verified in Lean, a sufficient criterion based on four conditions: an exact positive fractional covering, membership in the integer lattice of existing triangles, many typed common neighbours, and enough local exchanges called hinges. The construction prepares decomposable reserves before the uncovered edges are known. Every reserve, certificate and exchange lies inside the graph. The criterion is a variant of the partitioned framework announced by Delcourt and Postle, with stronger fractional and lattice hypotheses and an explicitly stated rooted hinge normalization.

A strengthened theorem controls linear triangle statistics and Pasch configurations in the same decomposition, with targets determined by the original fractional covering. Applications give Latin squares whose profiles determine their intercalate targets, and statistical refinements of known decompositions of the complete five-partite graph $K_{s,s,s,s,s}$ for $3\mid s$. For linear triangle statistics alone, Section 7 gives a computable tower bound depending on the parameters of T+.

The complete general proofs are in the accompanying Lean formalization, whose source snapshot passed reconstruction and the endpoint axiom audits. The paper explains the construction and proves the applications.

**Keywords:** triangle decomposition; labelled graphs; absorption; integer lattice; Latin square; Pasch configuration.

## 1. Introduction

Give each vertex of a graph a label, and specify which multisets of three labels are allowed. We seek a partition of the edges into triangles with those labels. A permitted multiset may repeat a label, but each triangle has three distinct vertices. The labels are on vertices, not on edges.

Our main result gives four sufficient conditions. They refer to the actual graph and its allowed triangles. Section 2 gives their precise definitions.

| Condition | What it supplies | Use in the construction |
|---|---|---|
| H1: an exact diffuse fractional seed | Positive triangle weights, of order $1/n$, summing to one at each edge | An exact starting point for approximate packing and later corrections |
| H2: the physical integer triangle lattice | An integer combination of existing triangles equal to the edge vector | The integer compatibility needed for absorption |
| H3: typed common neighbours | Many choices of a vertex with the required label | Placement of local pieces |
| H4: physical hinges | Many bounded auxiliary graphs allowing either of two local decompositions | Changes of triangle choices without losing decomposability |

These four conditions are checked in the given graph; no prior decomposition or external absorber is assumed. Here $n$ is the number of vertices, $I$ the label set and $\mathcal F$ the allowed family. The constants $C$, $\alpha$ and $h$ govern the seed bounds, local supply and maximum hinge order, respectively.

**Theorem T.** Fix $I,\mathcal F,\alpha,C,h$ with $\alpha>0$, $C\geq1$ and $h\geq6$. There is an integer $n_0$ such that every labelled graph G of order $n\geq n_0$ satisfying H1–H4 has an allowed triangle decomposition.

The strengthened theorem T+ in Section 2.3 produces a decomposition that also follows prescribed triangle statistics and a prescribed count of four-triangle Pasch configurations. Both targets come from the original fractional seed. The same decomposition satisfies all the requested estimates.

### 1.1. Absorption inside the graph

Absorption prepares for the edges left by an approximate decomposition. One reserves a small graph R before the residual M is known. The reserve has a decomposition of its own; it can also be decomposed together with any residual satisfying specified support, lattice and size conditions. We call such a residual admissible; Section 5.1 gives the terminal class. After covering the rest of the graph, one uses this second decomposition to finish. The difficulty is to prepare one reserve that works for every residual the construction may produce.

In an iterative construction, successive rounds move the uncovered edges into smaller vertex sets. Refined absorption, developed by Delcourt and Postle [6] and further presented by Postle [7], organizes many local absorption choices with controlled overlap. Iteration controls where the residual goes; refinement controls the local resources needed to absorb it.

We work within this direction. The word *physical* specifies how the objects are realized: every certificate uses triangles present in the graph, every auxiliary edge belongs to it, and every local replacement respects the allowed labels. An identity among label counts alone is insufficient. Even an integer identity among existing triangles may have negative coefficients; the construction must realize that identity by genuine decompositions. Section 3 explains this passage.

Papers I and II [1, 2] provide the construction on which this argument builds. Paper II develops the typed corrections and absorption pieces; Paper I organizes protected covering rounds and their iteration. Here we maintain these structures through the actual surviving graph and add statistical control through the completion. The reserves and collections of correction pieces are outputs of the proof, not extra assumptions of T.


The diagram in Figure \ref{fig:architecture} separates the reserve chosen once from the correction resources used during the rounds.

\begin{figure}[H]
\centering
\includegraphics[width=0.98\linewidth]{figures/architecture_en.pdf}
\caption{Schematic order of the construction. Preparation supplies the reserve and the correction resources before the corresponding demands are known. Each round leaves an actual child with an exact seed; iteration preserves the terminal reserve until the residual is absorbed. Arrows express dependencies, not inclusions or relative sizes.}
\label{fig:architecture}
\end{figure}


### 1.2. Applications and related work

Keevash's labelled-complex theorem [15, Theorem 3.1; 3, Theorem 4.18] requires regularity, lattice membership and rooted extendability. Applying it to T would require a translation verifying these conditions. We do not assert that reduction or claim greater generality. The closest stated criterion is Delcourt–Postle [14, Theorem 13.16]. For partitioned triangles, H3 is their anti-edgeful condition, and our hinge is their Definition 13.14. H1 strengthens their regular almost-packing to an exact seed. H2 supplies an integer certificate on actual triangles, implying their aggregate integral divisibility. H1 also implies fractional divisibility by summing its nonnegative edge equations over the parts and at each vertex.

There is a normalization difference: [14, Definition 13.15] prints $n^{i-2}$, whereas H4 uses $n^{i-4}$. Section 2.2 explains the latter from four fixed roots. We do not silently identify these printed conditions. Our contribution is an independent, formally verified proof of the variant stated here, together with the joint statistical conclusion T+ and the triangle-statistics tower bound. It is not a claim of priority for the partitioned criterion or the hinge mechanism.

Three vertex classes, representing rows, columns and symbols, turn a triangle decomposition into a Latin square. Section 8 applies T+ to prescribe linear statistics of a positive profile together with the number of intercalates, or two-by-two Latin subsquares. The existence of Latin squares with about one quarter of the square of the order intercalates is already known [9, 10]; our application imposes this count jointly with the prescribed tests. Section 8.1.4 keeps the coarse block targets fixed while varying the leading intercalate count. In Section 8.2, an explicit five-partite decomposition verifies the lattice condition, and T+ adds simultaneous control of statistics.

Labelled designs are treated in Keevash's general frameworks [3, 15], and multipartite decompositions in [11, 12]. Weighted pseudorandom matching results of Ehard, Glock and Joos [4] supply the approximate-packing setting, including weights on tuples. The task here is to retain that information through exact completion. For Latin squares, profile approximation [8], intercalate counts [9, 10] and discrepancy [13] provide the relevant context for the joint conclusions of Section 8.

The proof of [14, Theorem 13.16] is referred there to *Refined absorption for partitioned hypergraphs and beyond*. That separate manuscript had not been publicly released at the date of this preprint, as far as the bibliographic check of 1 November 2026 could establish. The construction here was developed from Paper II without access to it. The related note [5] concerns the accessible refined-absorption sources.

Section 2 states the hypotheses and statistical theorem. Sections 3–6 explain the construction and its final assembly. Section 7 gives the quantitative bound; Section 8 develops the applications. The companion formalization note records the exact Lean declarations, source freeze and audit scope. The technical preparation lemmas used in Sections 3–6 are identified there; these sections present their mechanism and assembly rather than a full reproduction of the formal library.

## 2. Physical triangles and the four hypotheses

Let G be a finite simple graph on a vertex set V, and write $n=|V|$. Let $I$ be a set of labels and let $\lambda:V\to I$ be a labelling. We impose no finiteness assumption on $I$. Let $\mathcal F$ be a set of multisets of labels.

A set $Q\subseteq V$ is an allowed triangle if it has three elements, every two of them are adjacent, and its label multiset belongs to $\mathcal F$. Write $\mathcal T=\mathcal T(G,\lambda,\mathcal F)$ for the set of allowed triangles. For such a triangle, $E(Q)$ is its three-edge set.

A decomposition of an edge set $J\subseteq E(G)$ is a family $\mathcal D\subseteq\mathcal T$ whose edge sets are pairwise disjoint and whose union is J. Vertices may occur in several triangles; edges may not.

### 2.1. The seed and the physical lattice

Fix a real constant $C\geq1$. An exact diffuse seed is a function $\mu:\mathcal T\to\mathbb R$ satisfying

$$
\frac{1}{Cn}\leq\mu(Q)\leq\frac{C}{n}
\qquad(Q\in\mathcal T),                                      \tag{2.1}
$$

and, for every edge $e\in E(G)$,

$$
\sum_{\substack{Q\in\mathcal T\\e\in E(Q)}}\mu(Q)=1.         \tag{2.2}
$$

Equation (2.2) is an equation for each physical edge. It says that the total fractional contribution at that edge is exactly one. The two bounds in (2.1) prevent zero weights on allowed triangles and prevent a single triangle from carrying a large fraction of an edge's mass. We call the existence of this seed **H1**.

For an edge set J, let $\mathbf1_J$ denote its integer indicator vector. The physical triangle lattice is

$$
\Lambda_G=\operatorname{span}_{\mathbb Z}
\{\mathbf1_{E(Q)}:Q\in\mathcal T\}.                           \tag{2.3}
$$

The ambient coordinates may be taken to be all unordered pairs of distinct vertices; vectors supported on the graph edges are extended by zero. Hypothesis **H2** is

$$
\mathbf1_{E(G)}\in\Lambda_G.                                \tag{2.4}
$$

This is an integer condition on triangles that exist in G. It is stronger information than a list of aggregate counts between label classes. It still does not give a decomposition: integer coefficients in (2.3) may be negative. When referring to a residual edge set, we use *physical* to mean that its indicator belongs to this lattice. Thus an admissible physical residual has an integer certificate, not just edges present in the graph.

### 2.2. Common neighbours and hinges

For distinct vertices u and v and a label k, define

$$
N_k(u,v)=\{w\in V:uw,vw\in E(G),\ \lambda(w)=k\}.
$$

Fix $\alpha>0$. Hypothesis **H3** requires

$$
|N_k(u,v)|\geq\alpha n                                      \tag{2.5}
$$

whenever $u\ne v$ and the multiset $\{\lambda(u),\lambda(v),k\}$ belongs to $\mathcal F$. The pair uv need not be an edge. This quantifier matters when a local construction has not yet completed the pair to a triangle.

To define H4, take two allowed triangles $T_a=\{u,v,a\}$ and $T_b=\{u,v,b\}$ with $a\ne b$. Their four vertices are distinct. Put

$$
W_a=\{ua,va\},\qquad W_b=\{ub,vb\}.
$$

A physical hinge for this pair is an edge set $J\subseteq E(G)$, disjoint from $E(T_a)\cup E(T_b)$, such that both $J\cup W_a$ and $J\cup W_b$ have allowed triangle decompositions. The auxiliary set J is the same in the two uses: it accommodates either wedge. For the complete multipartite example, see Appendix A and Figure \ref{fig:hinge}.

Its order is the number of vertices incident with J. Let $\mathcal H_i(T_a,T_b)$ be the family of these edge sets of order i. For an integer $h\geq6$, hypothesis **H4** is

$$
\text{for every such pair, there is }i\in\{6,\ldots,h\}
\text{ with }|\mathcal H_i(T_a,T_b)|\geq\alpha n^{i-4}.        \tag{2.6}
$$

The order i may depend on the root pair. We count edge sets, not vertex enumerations. All four roots belong to the vertices incident with J: covering each root wedge forces auxiliary edges at its vertices. Thus only $i-4$ vertices remain free. For fixed i there are at most $2^{\binom{i}{2}}n^{i-4}$ possible edge sets, which gives the natural normalization in (2.6) for edge sets with four fixed roots.

For comparison, [14, Definition 13.15] requires at least $\alpha n^{i-2}$ hinges for the fixed root pair. For fixed positive $\alpha$ and bounded i, the preceding upper bound is smaller than this requirement once n is sufficiently large. Thus the printed lower bound cannot hold in that range when such a root pair exists. In the proof of [14, Lemma 14.4], the constructed hinges have eight vertices and are counted with a lower bound of order $n^4=n^{8-4}$. These are the two counting statements being compared; we do not identify the printed conditions or assert an author-confirmed correction.

In fact i cannot be below six. In a decomposition of $J\cup W_a$, the triangles covering ua and va require third vertices outside the four roots, since J avoids both root triangles. These third vertices must be distinct, or the two triangles would share their edge to a. Hence the four roots require at least two further vertices.

### 2.3. Prescribed statistics

The threshold in T is chosen before the graph and its seed. No prepared core, bank, child graph or terminal absorber appears as an additional input. Their construction is part of the proof.

The following extension uses a specified seed, rather than only its existence. For a real function w on allowed triangles, define its fractional target by

$$
M_\mu(w)=\sum_{Q\in\mathcal T}\mu(Q)w(Q).                   \tag{2.7}
$$

A Pasch configuration is an unordered family of four triples on six vertices, with each vertex in exactly two triples and any two distinct triples meeting in at most one vertex. Let $\mathcal P(\mathcal A)$ be the set of Pasch configurations contained in a triangle family $\mathcal A$. Put

$$
P(\mathcal D)=|\mathcal P(\mathcal D)|,
\qquad
P_\mu=\sum_{S\in\mathcal P(\mathcal T)}\prod_{Q\in S}\mu(Q).
                                                                    \tag{2.8}
$$

There is no ordering factor in $P(\mathcal D)$: each four-triangle configuration is counted once.

**Theorem T+.** Fix $I,\mathcal F,\alpha,C,h$ as in Theorem T, together with $\eta>0$ and an integer $q\geq0$. There is an integer $n_0$ such that the following holds for every labelled graph G of order $n\geq n_0$ and every specified seed $\mu$ satisfying H1, provided H2–H4 hold. For every finite family $(w_j)_{j\in\mathcal J}$ with

$$
|\mathcal J|\leq n^q,
\qquad |w_j(Q)|\leq1\quad(j\in\mathcal J,\ Q\in\mathcal T),          \tag{2.9}
$$

there is one allowed triangle decomposition $\mathcal D$ such that

$$
\left|\sum_{Q\in\mathcal D}w_j(Q)-M_\mu(w_j)\right|
\leq\eta n^2\qquad(j\in\mathcal J),                                \tag{2.10}
$$

and

$$
|P(\mathcal D)-P_\mu|\leq\eta n^2.                                \tag{2.11}
$$

One decomposition satisfies every inequality, including the Pasch estimate; a different decomposition is not chosen for each test. Both targets use the original seed $\mu$. The threshold precedes the graph, seed and test family. T+ denotes this combined statement. The explicit bound in Section 7 concerns (2.10), not an explicit Pasch threshold. Agreement on tests specified in advance does not by itself assert closeness in cut distance.

## 3. What one round has to preserve

Appendix D states the preparation and completion estimates used below and explains their proofs. The full local construction is the formal proof identified in Section 9.

An approximate packing leaves uncovered edges. To iterate the construction, we need more than a small total number of them. We need to know where those edges lie, whether their indicator still has a physical certificate, and whether the remaining graph has enough local resources for another round.

The construction therefore works with a current graph, a smaller vertex window and a protected stock of auxiliary pieces. The stock is a packing of physical triangles. Parts of it may later be exchanged for local corrections, but the degree charged at each vertex is bounded throughout the round. A bank is a prepared collection of such choices together with the accounting needed to make several corrections simultaneously.

There are two separate choices of timing. First, the numerical tolerances and the admissible range of demands are fixed before the host graph is given. Second, once the host is available, the relevant reserves are placed before the particular residual demand is revealed. An absorber selected only after seeing the residual would not establish this order of choices.

The round has four jobs. It covers the edges that should not pass to the next window. It pays for every auxiliary edge it uses. It constructs an exact diffuse seed for the actual remaining child graph. Finally, it carries a physical certificate for the remaining demand into the graph in which the next correction will be made.

The last job cannot be replaced by divisibility in the original graph. A certificate might use triangles that have already been removed. The proof prepares a core in which the necessary lattice membership persists under the permitted deletions. This persistence is established from the original local hypotheses; it is not assumed in Theorem T.

### 3.1. The role of signed certificates

Write $A_G$ for the incidence map that sends triangle coefficients to their edge contributions:

$$
(A_Gc)(e)=\sum_{\substack{Q\in\mathcal T\\e\in E(Q)}}c(Q).
                                                                    \tag{3.1}
$$

Membership in $\Lambda_G$ says that an integer vector x can be written as $A_Gc=x$ with integer c. For simultaneous corrections, the size and concentration of c matter. A certificate with modest total mass can still put most of its load at one vertex and exhaust that vertex's reserve.

The certificate construction controls both total mass and vertex load. For a coefficient family c and an edge vector x, the relevant quantities are

$$
\|c\|_1=\sum_{Q\in\mathcal T}|c(Q)|,
\qquad
\operatorname{load}_v(c)=\sum_{\substack{Q\in\mathcal T\\v\in Q}}|c(Q)|,
                                                                    \tag{3.2}
$$

and the analogous absolute edge mass and incident mass of x. On the prepared host, the construction gives a constant L and bounds of the form

$$
\begin{aligned}
\|c\|_1&\leq L\|x\|_1,\\
\operatorname{load}_v(c)&\leq
 L\left(d_{|x|}(v)+\frac{\|x\|_1}{n}+1\right).
\end{aligned}                                                       \tag{3.3}
$$

Here $x\in\Lambda_G$, $\|x\|_1=\sum_{e\in E(G)}|x(e)|$, and $d_{|x|}(v)=\sum_{e\in E(G):v\in e}|x(e)|$. Formula (3.3) is a prepared-host estimate, with its preparation and order conditions retained. Concentrated demand contributes the first term; the average term distributes the remaining work. The additive unit is retained. The constant L here bounds certificate load; the integer L in (D.1) bounds quotient descent, and the L in (D.8) is a pair-codegree bound.

To see how the load estimate is used, read Appendix D.1 in the order (D.2), (D.3), (D.4). A certificate uses at most K triangle occurrences in absolute value, hence at most 3K vertex occurrences. For J demands the total is at most 3KJ. If a vertex is forbidden once it has been used q times, the number of forbidden vertices is at most 3KJ/q. Condition (D.2) makes this at most half the preparation budget. The next certificate can therefore be chosen away from them. Boundary vertices are counted separately by F_v. This explains both terms in (D.3): forced boundary use and auxiliary use distributed by the exclusion rule. Substitution of the routing bound gives (D.4), from which a single constant L absorbs the fixed coefficients in (3.3).

This argument uses the prepared-host certificate theorem. In particular, the right to avoid the forbidden set is a conclusion of preparation, not a consequence of integer-lattice membership alone. The finite descent in Appendix D.1 supplies persistence; the local quotient and certificate constructions are supplied by the formal proof supplement.

### 3.2. Positive corrections

Signed coefficients are useful for proving an identity, but a decomposition cannot use a triangle a negative number of times. The local gadgets replace signed exchanges by two genuine decompositions of a common auxiliary edge set. Hinges supply the elementary change between two root triangles. Longer exchanges are assembled from such physical pieces.

The placement is simultaneous. When placing a new piece, the construction excludes edges already used, vertices whose charge has reached its budget, and regions reserved for later stages. The supply bounds must survive all these exclusions together. Counting only one request in an otherwise unused graph would not prove the bank statement.

The resulting positive structures are inserted into a basal stock, meaning an edge set already equipped with an allowed decomposition. Replacing its decomposition on a chosen auxiliary set makes the required correction while keeping every triangle physical and allowed.

The elementary replacement can be checked directly in Appendix A. Expanding the first line of (A.2) gives the seven edges of J together with ua and va; expanding the second gives the same seven edges together with ub and vb. Every edge occurs once in its respective expansion. The two modes thus exchange one wedge for the other while keeping the auxiliary edge set fixed. The shared root edge uv belongs to neither wedge. Larger corrections must coordinate many such replacements: repeating this identity by itself does not guarantee that different auxiliary sets are disjoint. The simultaneous placement theorem is the additional construction that provides this disjointness under the load budgets.

## 4. Preparing the child graph

The child is the graph actually left after a round uses and reserves its edges. A reference is a preselected packing against which those changes are measured. Trimming means removing the specified vertices or edges; payments are decomposable pieces charged to the available resources when a correction uses auxiliary edges. All three operations are tracked on the same child graph, not merely on a sampled vertex set.

### 4.1. Exactness of the child seed

Let the actual child $G'$ be physical in its own triangle lattice, and let $\mu_0$ be supported on its allowed triangles. The first condition puts $\mathbf1_{E(G')}$ in the real column space of $A_{G'}$; the support condition puts $A_{G'}\mu_0$ in the same space. Their difference is therefore in the domain of the smooth inverse. At a child edge e this difference is

$$
r(e)=1-(A_{G'}\mu_0)(e).                                           \tag{4.1}
$$

To correct it, the smooth inverse produces a real triangle weighting $\xi$ with $A_{G'}\xi=r$. The corrected seed then satisfies

$$
A_{G'}(\mu_0+\xi)=A_{G'}\mu_0+r=\mathbf1_{E(G')}.                  \tag{4.2}
$$

The equality can be checked edge by edge: the correction contributes exactly $1-(A_{G'}\mu_0)(e)$, cancelling the deficit at that edge. This establishes exactness only. Positivity is a separate use of the bound on the inverse: the correction must be smaller than the margin between the preliminary weights and the permitted endpoints.

Equation (4.2) explains why an approximate edge equation is not enough. The proof must also bound $\xi$ so that $\mu_0+\xi$ remains positive and lies within the child diffuse bounds. The reference is chosen before the trimming step whose effect it measures. The smallness estimates and the charge paid for that reference are used together in the child construction.

This correction is made on the actual surviving host. Passing to another graph to obtain an inverse would require a further transport argument and would not prove the needed seed equation on $G'$.

The numerical margin is explicit in (D.5). Subtracting the largest possible correction from the preliminary lower bound leaves at least one quarter of the original reciprocal diffuse scale. For the upper bound, the corrected weight is at most twice the diffuse upper scale plus one quarter of the reciprocal scale; since C is at least one, this is at most four times the diffuse upper scale. These estimates establish positivity after exactification.

The existence step comes before this arithmetic. The proof of T uses `smooth_on_paid_prepared_child` in `VortexPaidChildSmooth.lean`. It constructs a prepared core after the paid edges are removed and applies the prepared-host inverse on that child. Its residual common-neighbour and hinge inputs are supplied by the surrounding construction. Then `exactify_of_smooth` in `SmoothExactification.lean` applies the inverse on its real image, with the physical target and supported weights just described. The corresponding explicit-order version, `paid_smooth_at_explicit`, belongs to the quantitative development in Section 7.

### 4.2. Integer certificates and local supply

Subtracting an allowed packing preserves lattice membership in the original ambient graph. Persistence inside the surviving graph requires more. The theorem `sparse_edge_deletion_host` in `SparseEdgeHost.lean` gives, for sufficiently large n and sufficiently small $\Delta(B)/n$ under H3–H4,

$$x\in\Lambda_{G-B}\quad\Longleftrightarrow\quad x\in\Lambda_G\ \text{and}\ x(e)=0\ (e\in B).$$

This is edge deletion, distinct from the vertex-deletion transport in Appendix D.1. For a dense physical reference $C_{\mathrm{ref}}$ and a disjoint physical payment Y, their union is physical and its complement has degree no larger than the complement of $C_{\mathrm{ref}}$. Applying persistence to that complement makes the surviving host itself physical. This is `intrinsic_H2_of_physical_reference_and_mode` in `G4ReferenceH2Generic.lean`.

The common-neighbour and hinge estimates are also transferred with explicit losses. The child state records the resulting parameters and the unused resources. Those parameters need not equal the initial $\alpha,C,h$; their admissible ranges are chosen as part of the construction. Theorem T nevertheless retains the original H1–H4 as its only graph hypotheses.

The interior and outer rounds have different duties. The outer round connects the original graph to the prepared chain and protects the terminal reserve. Interior rounds pass from one window to the next. Their constants are coordinated before the graph is chosen, so that a child delivered by one round lies within the range accepted by the next.

## 5. The adaptive chain and the terminal absorber

The chain follows successively smaller windows. Its geometric preparation restricts and rescales the original raw profile through those windows, with fixed parameters and a predetermined error schedule. It does not repeatedly use the newly exactified child seed as a fresh raw input and multiply its diffuse constant at every round. Actual packing choices remain adaptive: their state records previous bank activations and payments. These two levels separate fixed preparation from adaptive completion.

Each descent satisfies $16m_{j+1}\leq m_j$. Consequently $16^jm_j\leq n$, so positive child orders allow at most $\lfloor\log_{16}n\rfloor$ descents. The prepared chain stops at its fixed terminal scale t; in the Pasch argument one may stop earlier at the fourth-root cutoff of (D.9). The raw profile schedule and actual-child bounds are the invariants maintained by `VortexIntrinsicRawPathsPreparedVortex.lean` and the paid-layer construction.

A finite preparation index records which radius in the predetermined schedule is used. The terminal reserve must work for every possible value of this index. The construction first obtains a positive permissible rate and a size bound for each index, then takes the minimum of the rates and the maximum of the bounds. The index set is finite, so the common rate remains positive. This choice is made before the host reveals its index.

The induction has three checks at each transition. First, the packing and activated pieces account for every edge removed in that round, so the remaining edge set is the actual child. Second, the transferred common-neighbour, hinge and lattice properties hold in that child, and (4.2) restores its exact seed. Third, the child order and remaining budgets satisfy the input requirements of the next round. A statement that only produces a smaller vertex set would establish none of these three checks. The outer round also keeps R untouched. At termination, the same bookkeeping gives the four properties of M used in Section 5.2; these are precisely the conditions needed to apply the terminal reserve.

### 5.1. What the terminal reserve does

Let $G_{\mathrm{abs}}$ be the prepared graph in which absorption will occur, and let U be the terminal vertex window. The reserve R is selected so that R already has an allowed decomposition and, for every admissible physical edge set M supported on U, the union $R\cup M$ also has one. The reserve has bounded size and avoids the protected outer core.

The order of the quantifiers is

$$
\text{prepared graph and terminal window}
\quad\longrightarrow\quad R
\quad\longrightarrow\quad\text{every admissible }M.                \tag{5.1}
$$

The residual M is not used to choose R. There are only boundedly many possible edge subsets on a bounded terminal window, but realizing all the required absorbers disjointly and within the allowed charge is a construction, not a consequence of that finiteness alone.

The reserve in Figure 1 is the same R used here: it is placed before the residual demand is known and remains protected during the outer round.

### 5.2. Final assembly of Theorem T

For the final assembly, keep four outputs in view. Section 3 supplies physical integer certificates and their realizations in correction banks. Section 4 supplies the exact diffuse seed of the actual child, together with its surviving lattice and geometric conditions. Section 5.1 supplies the reserve R, chosen uniformly before the residual M. The rounds then supply the packing P covering the complement of the reserved remainder. The first two outputs make the rounds applicable; the last two are joined to obtain the decomposition. The numerical choices below precede all these host-dependent objects.

The numerical order can be read from `MainPaperIII.lean`. First fix the cleaned geometry $(\alpha,h)$ and C; then the quotient bounds $(d,T,L)$ and local layer tolerances; next the inner rates, the preparation schedule $\beta$ and its order requirements; then the terminal scale t; then the reserve rate and size $(q_R,K)$; then $q_{\mathrm{outer}}$, $\theta_T$ and the remaining order requirements. Finally choose $n_0$. In particular t does not depend on the reserve, and the reserve is chosen before the outer rate. The relevant dependency order is

$$ (\alpha,h,C)\longrightarrow(d,T,L)\longrightarrow\beta\longrightarrow t\longrightarrow(q_R,K)\longrightarrow q_{\mathrm{outer}}\longrightarrow\theta_T\longrightarrow n_0. $$

At final assembly the constructed objects are the prepared chain with its exact child seeds and physical certificates, the reserve R, the exterior packing P and the physical residual M. All their numerical requirements were fixed before the host. The final order is the maximum

$$
n_0=\max\left\{
n_{\mathrm{clean}},n_{\mathrm{raw}},n_{\mathrm{outer}},
\left\lceil\frac{K}{\theta_T}\right\rceil
\right\}.                                                         \tag{5.2}
$$

Here the first three terms pay for hinge preparation, the prepared chain and the outer round. The reserve has at most K edges, and $\theta_T>0$ is the outer tolerance. The last term ensures $K\leq\theta_T n$, so the outer construction can protect the reserve. These are the auxiliary quantities selected by the construction, not new parameters in the statement of T.

Given a host of order at least $n_0$, prepare the chain and embed its terminal window in $G_{\mathrm{abs}}$. Choose R using the uniform reserve statement. Run the outer round with R protected, and then run the interior assembly. The output consists of an allowed packing $\mathcal P$ and a residual M in $G_{\mathrm{abs}}$. The assembly establishes the following facts together: M is physical in $G_{\mathrm{abs}}$, its support lies in U, it is disjoint from R, and all edges outside the embedded $R\cup M$ are covered exactly once by $\mathcal P$.

The reserve property gives a decomposition $\mathcal A$ of $R\cup M$. Transport it into the original graph by the vertex embedding $\iota$. We obtain

$$
\mathcal D=\mathcal P\cup\iota(\mathcal A).                         \tag{5.3}
$$

Every triangle in the second family is allowed because the embedding preserves adjacency and labels. Its edges lie in the reserved remainder, so they are disjoint from the edges covered by $\mathcal P$. Within each family the edges are already disjoint. Finally, the partition supplied by the assembly says that their union is $E(G)$. This proves the final implication needed for Theorem T. The formalization companion identifies the technical existence lemmas used in this assembly.

## 6. Keeping the prescribed statistics

### 6.1. Signed triangle tests

For bounded triangle weights, completing a large packing has a simple error cost. If $\mathcal P\subseteq\mathcal D$ and $|w(Q)|\leq1$, then

$$
\left|\sum_{Q\in\mathcal D}w(Q)-\sum_{Q\in\mathcal P}w(Q)\right|
\leq|\mathcal D\setminus\mathcal P|.                               \tag{6.1}
$$

Indeed, the difference is the sum over the newly added triangles. Its absolute value is at most the sum of their absolute weights, and each is at most one. The triangle inequality then combines this completion error with the discrepancy already achieved by the packing.

The packing stage records the desired tests along with the local tests needed by the construction. A positive-weight matching argument does not automatically accept an arbitrary signed test. The monitored packing construction performs the required conversion and retains the error measured against the original seed. The number of prescribed tests is bounded by $n^q$, with q fixed before choosing the threshold.

The relevant lemma is `signed_envelope_sparse_packing` in `SignedEnvelopePacking.lean`; its explicit-order counterpart is `signed_envelope_sparse_packing_explicit`. Its inputs include H1, H3, positive constants $B,c,\tau$ and envelopes satisfying $0\leq A\leq1$, $|W|\leq BA$ and $cn\leq M(A)$. Here $\varphi$ is the specified seed, $M(f)=\sum_Q\varphi(Q)f(Q)$ and $S(f)=\sum_{Q\in\mathcal P}f(Q)$. The lower mass bound is needed by the matching theorem and cannot be omitted.

Set $J_0=A/2$ and $J_1=(W/B+2A)/3$. Then $A/3\leq J_1\leq A$ and $0\leq J_0,J_1\leq1$; both tests have mass at least $cn/3$. Also $W=3BJ_1-4BJ_0$. If the packing controls each nonnegative test with relative error $\varepsilon$, then

$$\begin{aligned}|S(W)-M(W)|&\leq3B\varepsilon M(J_1)+4B\varepsilon M(J_0)\\&\leq3B\varepsilon M(A)+2B\varepsilon M(A)=5B\varepsilon M(A).\end{aligned}$$

Choose $\varepsilon\leq\tau/(5B)$, also below the required leftover-degree tolerance. Two tests per envelope fit the bound $2n^q\leq n^{q+1}$ for $n\geq2$. One packing then controls all signed tests and leftover degrees. The envelope preserves the local mass scale of the error.

### 6.2. Why Pasch needs further tracking

A Pasch count depends on four triangles at a time. Adding a single triangle can create several configurations with earlier triangles, so (6.1) does not apply directly to this count.

For a triangle family $\mathcal A$, let

$$
I_{\mathcal A}(Q)=
|\{S\in\mathcal P(\mathcal A):Q\in S\}|.
$$

For any two families $\mathcal A,\mathcal B$, a configuration present in one but not the other contains a triangle from the corresponding set difference. Counting through such a triangle gives

$$
\begin{aligned}
|P(\mathcal A)-P(\mathcal B)|
&\leq\sum_{Q\in\mathcal A\setminus\mathcal B}I_{\mathcal A}(Q)\\
&\quad+\sum_{Q\in\mathcal B\setminus\mathcal A}I_{\mathcal B}(Q).
\end{aligned}                                                       \tag{6.2}
$$

A configuration can be charged more than once, which is harmless for this upper bound. The difficulty is to bound the total charge along the actual completion.

The Pasch construction records incidences through partially specified configurations and tracks the bank pieces activated by the previous rounds. The adaptive state therefore carries more information than the edge remainder. This is used to bound the contribution of subsequent bank activations and of the final reserve. The comparison target remains $P_\mu$ from (2.8); it is not recomputed from a later seed.

The final proof uses separate positive budgets for triangle tests and Pasch counts. For Pasch, the base packing $\mathcal P_0$ approximates $P_\mu$ from both sides. Throughout completion, $\mathcal P_0\subseteq\mathcal D_{\mathrm{paid}}\subseteq\mathcal D$, so monotonicity preserves the lower estimate. The tracked available family contains the paid family and supplies the upper estimate. Thus the argument uses both a monotone sandwich and the upper growth budget; it is not an absolute-error estimate obtained from growth alone.

Write D for the fixed inner growth coefficient and $q_{\mathrm{outer}}$ for the first sampling rate. The outer layer spends at most $(\tau/2)n^2$. Its first child has order $m_0\leq2q_{\mathrm{outer}}n$, so the initial inner potential satisfies $\Phi_0=2Dnm_0\leq4Dq_{\mathrm{outer}}n^2\leq(\tau/2)n^2$ once $8Dq_{\mathrm{outer}}\leq\tau$. This rate condition is imposed by `adaptiveOuterRate_spec`, and `TrackingState.initial` combines the two halves. Appendix D.4 then pays for all later mixed configurations within that potential.

The final error budget can be read without assuming that Pasch counts add across rounds. At each stage, (6.2) charges changed configurations to changed triangles. The ambient family includes earlier triangles, so mixed configurations are included in this charge. Appendix D.4 bounds each stage's charge and sums it with the decreasing potential (D.7). At the stopping point, each remaining added triangle is charged at most n times. The bound on the number of added triangles in (D.9) then gives the terminal error. The three contributions are the initial discrepancy, the tracked growth and the terminal contribution; (D.10) allocates them within the prescribed tolerance.

## 7. Extracting a quantitative threshold

The existence of a natural number defined by a finiteness argument does not by itself give an evaluable bound. The quantitative development replaces the relevant finite-existence and asymptotic choices by arithmetic majorants. We describe one algebraic step explicitly before giving the scope of the final bound.

### 7.1. A bound for grouping charges

Let d, B and R be nonnegative integers. Suppose $z_i\in\mathbb Z^d$ are finitely many indexed charge vectors with coordinates of absolute value at most B. Let $\Gamma\leq\mathbb Z^d$ be generated by integer vectors whose coordinates have absolute value at most R. Assume $\sum_i z_i\in\Gamma$. The grouping construction partitions the indices into blocks whose individual sums lie in $\Gamma$.

Define a sequence of bounds recursively by

$$
K_0(D)=1,\qquad
K_{d+1}(D)=(2D+1)K_d\bigl(D(2D+1)\bigr).                           \tag{7.1}
$$

**Proposition 7.1.** The blocks can be chosen to have size at most $K_d(\max\{B,R\})$. Moreover,

$$
K_d(D)\leq(2D+1)^{2^d-1}.                                         \tag{7.2}
$$

*Explanation of the grouping bound.* In one coordinate, order a zero-sum family by choosing a nonpositive next term when the current partial sum is nonnegative, and a nonnegative next term when it is negative. The required sign is available because the remaining terms must cancel the partial sum. All partial sums stay in the integer interval $[-D,D]$. In an inclusion-minimal nonempty zero-sum family, the partial sums before the final return to zero are distinct; otherwise a proper consecutive block would already sum to zero. There are at most $2D+1$ such values.

In higher dimension, partition by minimal zero-sum blocks in one coordinate. Each block has at most $2D+1$ terms. The sums in the remaining coordinates have absolute value at most $D(2D+1)$. Apply the induction to these block sums and expand the chosen blocks. This gives (7.1) for a nonempty zero-sum subfamily. Irreducibility then bounds a whole minimal kernel relation.

For sums modulo $\Gamma$, the construction lifts a minimal charge family to an integer zero-sum relation by adjoining signed generator columns. All columns have bound $\max\{B,R\}$. To see why, choose a nonempty subfamily minimal for having sum in the lattice, express the negative of its sum using signed generator columns, and minimize the number of added columns. A proper zero-sum subfamily containing no original token could be removed from the lift. One containing some, but not all, original tokens would contradict minimality of the charge family. One containing all original tokens would shorten the generator representation. Thus the lift is irreducible. The kernel bound therefore bounds the number of original tokens; removing such a block and repeating gives a partition. The lift retains the actual integer lattice, including torsion in the quotient.

*Proof of (7.2).* The case $d=0$ is equality. For the induction step, put $A=2D+1$. Then

$$
2D(2D+1)+1\leq A^2.
$$

Using (7.1) and the induction hypothesis,

$$
\begin{aligned}
K_{d+1}(D)
&\leq A\bigl(2D(2D+1)+1\bigr)^{2^d-1}\\
&\leq A(A^2)^{2^d-1}
=A^{2^{d+1}-1}.
\end{aligned}
$$

Thus the original grouping constant satisfies

$$
\operatorname{groupBound}(d,B,R)
\leq\bigl(2\max\{B,R\}+1\bigr)^{2^d-1}.                           \tag{7.3}
$$

The point of this bound is its specified dependence on the input integers. It is not offered as a sharp estimate.

### 7.2. The triangle-monitor threshold

Let $\lceil x\rceil_+=\max\{0,\lceil x\rceil\}$. Normalize the inputs by

$$
K=\max\{2,h,q,\lceil\alpha\rceil_+,\lceil1/\alpha\rceil_+,
\lceil C\rceil_+,\lceil\eta\rceil_+,\lceil1/\eta\rceil_+\}.          \tag{7.4}
$$

Define the base-two tower by

$$
\operatorname{tow}_2(0)=1,\qquad
\operatorname{tow}_2(r+1)=2^{\operatorname{tow}_2(r)}.                \tag{7.5}
$$

The quantitative development specifies a natural-number program $H(K,h,q)$ whose associated tower bounds the order required by the triangle-monitor construction. Its successive stages bound input normalization, the finite schedule, the layer orders, the terminal scale and the reserve. Once the ceilings in (7.4) have been supplied, this height uses natural-number arithmetic and finite recursions. Appendix C gives the exact source definition and its dependencies.

**Theorem 7.2.** With the parameters and H1–H4 of Theorem T+, the conclusion (2.10), for one allowed decomposition and every test in the given family, holds whenever

$$
n\geq\operatorname{tow}_2\bigl(H(K,h,q)\bigr).                     \tag{7.6}
$$

The bound is independent of the host, the particular seed, the tests and the number of labels. The statement here makes no claim about (2.11).

For example, the rational inputs

$$
\alpha=\frac1{100},\quad C=2,\quad\eta=\frac1{1000},
\quad h=6,\quad q=2
$$

give $K=1000$. Hence (7.6) is the definite integer expression $\operatorname{tow}_2(H(1000,6,2))$. We have not evaluated its decimal expansion. Specifying its finite arithmetic definition is distinct from asserting that the resulting bound is useful for computation at moderate orders.

The accompanying file `HEIGHT_PROGRAM_en.md` prints all 312 arithmetic definitions in dependency order. The theorem `TypedTriangle.PrintedHeight.height_agrees` identifies this expansion with the original height. Thus (7.4)–(7.6), together with that finite program, specify the bound including its dependence on $\eta$ and q; no asymptotic placeholder is used.

There are two different operations in the quantitative bound. Equation (7.4) first replaces real tolerances and their reciprocals by a common integer majorant. The reciprocals matter because smaller positive tolerances require larger orders. Appendix C then follows the order of the construction: input normalization, the finite agenda of requirements, the layer scale, the terminal scale and the reserve scale. Its last function majorizes these requirements by a tower height. Finally (7.6) applies the tower to that height. The arithmetic program in the supplement fixes the actual functions in this composition; their names alone are not an alternative definition of an elementary closed formula.

## 8. Applications

The applications below use the same theorem in two different hosts. We first treat Latin squares through the complete tripartite graph, then rainbow triangles in a balanced five-partite graph. Each application verifies H1–H4 before prescribing statistics.

### 8.1. Latin squares with a prescribed profile

Let A be a set of size m. Use three disjoint copies of A as the row, column and symbol classes of $K_{m,m,m}$. Its allowed triangles are the triples $(r,c,s)\in A^3$.

A decomposition selects exactly one s for each pair $(r,c)$, so it defines a function $L:A^2\to A$. Covering each row-symbol edge once says that every symbol appears once in each row. Covering each column-symbol edge once gives the corresponding column condition. Thus L is a Latin square. Conversely, every Latin square gives this decomposition.

Let $p:A^3\to\mathbb R$ be a profile with all three line marginals equal to one:

$$
\sum_s p(r,c,s)=1,\qquad
\sum_c p(r,c,s)=1,\qquad
\sum_r p(r,c,s)=1.                                                  \tag{8.1}
$$

Fix $a>0$ and $b\in\mathbb R$, and suppose

$$
\frac a m\leq p(r,c,s)\leq\frac b m.                               \tag{8.2}
$$

The host order is $3m$. Consequently (8.1)–(8.2) give H1 with

$$
C=\max\left\{1,3b,\frac1{3a}\right\}.                             \tag{8.3}
$$

For the lower diffuse bound, $C\geq1/(3a)$ gives $1/(3Cm)\leq a/m$. For the upper bound, $C\geq3b$ gives $b/m\leq C/(3m)$. The line equations are exactly the three kinds of edge equations.

H2 has an explicit witness. Identify A with $\mathbb Z/m\mathbb Z$ and take the triples satisfying $r+c+s=0$. Each pair determines the third coordinate uniquely, so these triangles decompose the graph. Their indicators sum to the full edge indicator.

The following counts come directly from the sizes of the parts in the complete multipartite host. For H3, a compatible pair of labels has exactly m common neighbours in the third class. For H4, the hinge in Appendix A gives $(m-1)^2$ distinct six-vertex edge sets for each pair of root triangles. When $m\geq2$,

$$
(m-1)^2\geq\frac{m^2}{4}
=\frac1{36}(3m)^2.                                                 \tag{8.4}
$$

Thus H3 and H4 follow from part sizes and the explicit hinge with $\alpha=1/36$ and $h=6$. H1 follows from the profile and (8.3); H2 follows from the cyclic decomposition. Summing the profile bounds along a line gives $a\leq1\leq b$, so positivity of b needs no extra assumption.

#### 8.1.1. The profile theorem

For a profile p, define

$$
\begin{aligned}
\Pi(p)=\frac14
\sum_{r\ne r'}\sum_{c\ne c'}\sum_{s\ne s'}
&p(r,c,s)p(r,c',s')\\[-2pt]
&{}\cdot p(r',c,s')p(r',c',s).
\end{aligned}                                                       \tag{8.5}
$$

Each sum is over ordered pairs of distinct elements of A. The factor $1/4$ will be justified below. Let $\operatorname{int}(L)$ be the number of intercalates of L, counted as unordered four-cell configurations.

**Theorem 8.1.** Fix $a>0$, $b\in\mathbb R$, $\eta>0$ and an integer $q\geq0$. There is an integer M such that for every finite set A of size $m\geq M$, every profile satisfying (8.1)–(8.2), and every family of at most $m^q$ real tests $w_j:A^3\to[-1,1]$, there is a Latin square L with

$$
\left|\sum_{r,c}w_j(r,c,L(r,c))-
\sum_{r,c,s}p(r,c,s)w_j(r,c,s)\right|\leq\eta m^2                  \tag{8.6}
$$

for all j, and

$$
|\operatorname{int}(L)-\Pi(p)|\leq\eta m^2.                         \tag{8.7}
$$

*Proof.* The preceding calculations verify H1–H4. Apply Theorem T+ with precision $\eta/9$ to the host of order $3m$. The test-family size is admissible because $m^q\leq(3m)^q$, and the error is $(\eta/9)(3m)^2=\eta m^2$. Translate the decomposition back to a Latin square.

A Pasch in the tripartite triangle family has two vertices in each class. Indeed, each class has four incidences among the four triangles, and every vertex has degree two within the configuration. After choosing a root triangle $(r,c,s)$, the other vertices $r',c',s'$ determine the remaining three triangles as

$$
(r,c',s'),\qquad(r',c,s'),\qquad(r',c',s).                           \tag{8.8}
$$

Conversely, each choice of three ordered pairs of distinct coordinates in (8.5) produces four distinct allowed triples of the form (8.8) together with the root. They have six vertices, each used twice, and form a Pasch. Each unordered Pasch has exactly four root triangles, giving the factor $1/4$. In a Latin-square decomposition this configuration is exactly a two-by-two subsquare with alternating symbols. Thus the unordered Pasch count equals the intercalate count, proving (8.7).

#### 8.1.2. The uniform target

For $p=1/m$, there are $m^3$ choices of root and $(m-1)^3$ choices of the three other coordinates. Each configuration is counted four times and each product has weight $m^{-4}$. Hence

$$
\Pi(1/m)=\frac{m^3(m-1)^3}{4m^4}
=\frac{(m-1)^3}{4m}.                                               \tag{8.9}
$$

**Corollary 8.2.** For every $\eta>0$ and integer $q\geq0$, every sufficiently large order admits a Latin square satisfying (8.6) for the uniform profile and every prescribed family of at most $m^q$ bounded signed tests, together with

$$
\left|\operatorname{int}(L)-\frac{(m-1)^3}{4m}\right|
\leq\eta m^2.                                                       \tag{8.10}
$$

The leading intercalate count alone is an established existence conclusion [9, 10]. Here it is imposed jointly with all the prescribed tests. The exact finite-order expression in (8.9) is retained. Replacing it by its leading term would conceal the normalization of the unordered count.

#### 8.1.3. A nonuniform profile

Let $\sigma,\tau,\upsilon:A\to\{-1,1\}$ each have sum zero, and fix $0\leq\theta<1$. Define

$$
p(r,c,s)=\frac{1+\theta\sigma(r)\tau(c)\upsilon(s)}m.               \tag{8.11}
$$

Summing in any coordinate eliminates the signed term, so (8.1) holds. Also $(1-\theta)/m\leq p\leq(1+\theta)/m$. Theorem 8.1 therefore applies with $a=1-\theta$ and $b=1+\theta$, uniformly over the balanced signs.

We compute the target. For any balanced sign function $\sigma$,

$$
\sum_{x\ne y}1=m(m-1),\qquad
\sum_{x\ne y}\sigma(x)=0,\qquad
\sum_{x\ne y}\sigma(x)\sigma(y)=-m.                                \tag{8.12}
$$

The last equality follows by subtracting the diagonal terms from $(\sum_x\sigma(x))^2=0$; each diagonal term is one. The other two identities follow by counting the $m-1$ choices of y for each x and then using balance.

Write $a,a',b,b',c,c'$ for the six signs in an ordered box. Since their squares are one, expansion gives

$$
\begin{aligned}
&(1+\theta abc)(1+\theta ab'c')
 (1+\theta a'bc')(1+\theta a'b'c)\\
&=1+\theta^4
 +(\theta+\theta^3)(abc+ab'c'+a'bc'+a'b'c)\\
&\quad+2\theta^2(aa'bb'+aa'cc'+bb'cc').
\end{aligned}                                                       \tag{8.13}
$$

After summing over distinct pairs in all three coordinates, the terms linear in each chosen sign vanish by (8.12). The constant part contributes $(1+\theta^4)m^3(m-1)^3$. Each of the three quadratic products contributes $m^3(m-1)$ before multiplication by $2\theta^2$: two signed-pair sums equal $-m$, and the remaining unsigned-pair sum equals $m(m-1)$. Dividing by the normalization $4m^4$ in (8.5), we obtain

$$
\Pi(p)=\frac{(1+\theta^4)(m-1)^3}{4m}
+\frac{3\theta^2(m-1)}{2m}.                                        \tag{8.14}
$$

**Corollary 8.3.** For each fixed $0\leq\theta<1$, $\eta>0$ and integer $q\geq0$, all sufficiently large orders carrying balanced signs admit a Latin square with the profile statistics (8.6) and intercalate target (8.14), each with error at most $\eta m^2$. The threshold is uniform over the signs and the tests.

For every even m, balanced signs can be constructed by assigning +1 to a subset of size $m/2$ and −1 to its complement. Taking $\sigma=\tau=\upsilon$ and $\theta=1/2$ gives the concrete target

$$
\Pi(p)=\frac{17(m-1)^3}{64m}+\frac{3(m-1)}{8m}.                     \tag{8.15}
$$

Thus a specific nonuniform profile is available at every sufficiently large even order. The conclusion concerns one square realizing that profile's tests and its intercalate target simultaneously.

#### 8.1.4. The same block profile with different intercalate counts

The preceding example links one profile to one intercalate target. We now keep the coarse profile fixed and change that target. The extra freedom comes from a second division inside each half. Its contribution cancels in the marginal sums, but survives in the four-factor expression (8.5).

Fix $0\leq\theta<1$ and $0\leq t<1$. Write $p_0$ for (8.11), and set

$$
M_0(w)=\sum_{r,c,s}p_0(r,c,s)w(r,c,s),\qquad
S_w(L)=\sum_{r,c}w(r,c,L(r,c)),\qquad
\kappa(\theta,t)=\frac{(1+\theta^4)(1+t^4)}4.                 \tag{8.16}
$$

**Theorem 8.4.** Fix $\varepsilon>0$ and an integer $q\geq0$. For every sufficiently large m divisible by four, every balanced choice of the coarse signs, and every prescribed family $\mathcal W$ of at most $m^q$ tests $w:A^3\to[-1,1]$, there are Latin squares $L_0,L_t$ such that

$$
\begin{aligned}
|S_w(L_i)-M_0(w)|&\leq\varepsilon m^2
&& (w\in\mathcal W,\ i\in\{0,t\}),\\
|\operatorname{int}(L_0)-\kappa(\theta,0)m^2|&\leq\varepsilon m^2,\\
|\operatorname{int}(L_t)-\kappa(\theta,t)m^2|&\leq\varepsilon m^2.
\end{aligned}                                                   \tag{8.17}
$$

The threshold depends only on $\theta,t,\varepsilon,q$. The same squares can also satisfy the eight block estimates

$$
\left|\#\{(r,c)\in R_a\times C_b:L_i(r,c)\in S_d\}
       -\frac{1+\theta abd}{8}m^2\right|\leq\varepsilon m^2,
\quad a,b,d\in\{-1,1\},\ i\in\{0,t\}.                       \tag{8.18}
$$

Here the letters R, C and S denote the row, column and symbol copies of A, and their subscripts specify the coarse signs. The tests are chosen before the squares. The Latin condition is exact; the statistics and block counts have the displayed additive errors.

*Proof.* We give the construction and keep track of the errors.

**Step 1: a second balanced division.** Choose fine signs $\xi,\zeta,\chi$, each balanced separately inside its two coarse halves. Every coarse/fine sign pair then occurs $m/4$ times in its coordinate. Define

$$
p_t(r,c,s)=p_0(r,c,s)[1+t\xi(r)\zeta(c)\chi(s)].              \tag{8.19}
$$

The numerator expands as

$$
1+\theta\sigma\tau\upsilon+t\xi\zeta\chi
  +\theta t(\sigma\xi)(\tau\zeta)(\upsilon\chi).              \tag{8.20}
$$

In each coordinate the coarse sign, fine sign and their product all sum to zero. Summing (8.20) in any one coordinate therefore leaves m, so every marginal of (8.19) is one. Moreover,

$$
\frac{a_*}{m}\leq p_t\leq\frac{b_*}{m},\qquad
a_*=(1-\theta)(1-t)>0,\qquad b_*=(1+\theta)(1+t).             \tag{8.21}
$$

These bounds also hold for $p_0$. Inside each coarse block, the sum of the perturbation factors into three fine-sign sums and is zero. Thus the two seeds have exactly the same block targets in (8.18).

**Step 2: the four-factor target.** For a real x, average

$$
(1+xabc)(1+xab'c')(1+xa'bc')(1+xa'b'c)
$$

over independent uniform signs. A term survives the expansion precisely when every sign has even multiplicity. With no coordinate pair identified, only the empty selection and the selection of all four factors survive. Identifying one pair gives the same result. With two pairs identified, average $(1+xabc)^2(1+xabc')^2$; with three pairs, average $(1+xabc)^4$. The four averages, in order, are

$$
1+x^4,\qquad 1+x^4,\qquad (1+x^2)^2,\qquad 1+6x^2+x^4.     \tag{8.22}
$$

The coarse and fine averages multiply: for every free vertex the four pairs of signs occur equally often. This remains true on each diagonal where coordinate pairs are identified. Put

$$
\begin{aligned}
A_*&=(1+\theta^4)(1+t^4),\\
B_*&=(1+\theta^2)^2(1+t^2)^2,\\
C_*&=(1+6\theta^2+\theta^4)(1+6t^2+t^4).
\end{aligned}
$$

The unrestricted numerator sum is $m^6A_*$. Each of the three single diagonals contributes $m^5A_*$, each of the three double diagonals contributes $m^4B_*$, and the triple diagonal contributes $m^3C_*$. Inclusion-exclusion, followed by division by $4m^4$, proves the exact identity

$$
\Pi(p_t)=\frac{A_*(m^2-3m)+3B_*-C_*/m}{4}.                 \tag{8.23}
$$

It holds for every balanced choice of the fine signs. There is also a useful error bound without cancellation: removing the three diagonals from the sum of products of profile weights deletes at most $3m^5$ nonnegative terms, each at most $(b_*/m)^4$. Hence

$$
0\leq\kappa(\theta,t)m^2-\Pi(p_t)\leq\frac{3b_*^4m}{4}.    \tag{8.24}
$$

The same upper bound applies to the difference for $p_0$ and $\kappa(\theta,0)$.

**Step 3: retain the prescribed tests.** Put $Q=q+1$. Fix balanced $\zeta,\chi$. Pair the rows within each coarse half. Give each pair $(r_\ell,r'_\ell)$ an independent uniform sign $e_\ell$, and set $\xi(r_\ell)=e_\ell$, $\xi(r'_\ell)=-e_\ell$. Balance holds for every outcome. For a test w, let

$$
\begin{aligned}
a_w(r)&=\sum_{c,s}p_0(r,c,s)\zeta(c)\chi(s)w(r,c,s),\\
d_\ell&=t[a_w(r_\ell)-a_w(r'_\ell)],\qquad
M_t(w)=\sum_{r,c,s}p_t(r,c,s)w(r,c,s).
\end{aligned}
$$

Nonnegativity and the exact marginals give $|a_w(r)|\leq m$. Consequently

$$
M_t(w)-M_0(w)=\sum_\ell e_\ell d_\ell,\qquad
\sum_\ell d_\ell^2\leq2t^2m^3.                              \tag{8.25}
$$

The elementary inequality $\cosh u\leq\exp(u^2/2)$ follows by comparing series, since $(2k)!\geq2^k k!$. Independence, Markov's inequality and optimization of the exponential parameter give, for $t>0$,

$$
\Pr\bigl(|M_t(w)-M_0(w)|\geq\delta m^2\bigr)
\leq2\exp\left(-\frac{\delta^2m}{4t^2}\right)
\leq2\exp\left(-\frac{\delta^2m}{4}\right).                  \tag{8.26}
$$

Here is the exponential estimate used in (8.26). Put $X=\sum_\ell e_\ell d_\ell$ and $V=\sum_\ell d_\ell^2$. Independence gives $\mathbb E e^{uX}=\prod_\ell\cosh(ud_\ell)\leq e^{u^2V/2}$. Markov's inequality then gives $\Pr(X\geq a)\leq e^{-ua+u^2V/2}$. For $V>0$, choose $u=a/V$ and apply the same argument to $-X$, obtaining $2e^{-a^2/(2V)}$. Substituting $a=\delta m^2$ and $V\leq2t^2m^3$ gives (8.26). If $V=0$, then $X=0$ and no estimate is needed.

For $t=0$ the difference is zero. A union bound over at most $m^Q$ tests shows that, for sufficiently large m, some balanced choice retains every target within $\delta m^2$. Formula (8.23) still holds for that choice.

**Step 4: round both seeds.** Add the eight block indicators to the test family. For $m\geq12$, its size is at most $m^{q+1}$. Set $\delta=\eta=\varepsilon/4$. Choose the threshold from Theorem 8.1 for $a_*,b_*,\eta,Q$, and increase it until, for every subsequent m,

$$
m\geq12,\qquad m\geq\frac{3b_*^4}{\varepsilon},\qquad
2m^Q\exp(-\varepsilon^2m/64)<1.                              \tag{8.27}
$$

Choose the fine signs first, then apply Theorem 8.1 to each seed. For $L_t$, the error in a prescribed test is at most $(\eta+\delta)m^2=\varepsilon m^2/2$; for $L_0$ it is at most $\eta m^2$. The block targets agree exactly before rounding. By (8.24), each intercalate error relative to its leading term is at most $\eta m^2+3b_*^4m/4\leq\varepsilon m^2/2$. This proves all the stated bounds.

The order of choices is essential here. The test family, including the eight block indicators, is fixed before the random signs are sampled. For each test, (8.26) bounds its failure probability. Multiplying by the number of tests gives the last expression in (8.27), which is less than one; consequently at least one choice fails none of the tests. Fix that choice before rounding. For a prescribed test, the difference between the integral value and the original target splits into rounding error and seed perturbation error. For intercalates it splits into rounding error and the finite-order correction (8.24). The block perturbation is exactly zero, so block errors require only the rounding allowance.

No new host hypothesis was used. The verification preceding Theorem 8.1 supplies H1 with $C=\max\{1,3b_*,1/(3a_*)\}$, H2 from the cyclic decomposition, H3 with $\alpha=1/36$, and H4 with $h=6$. The threshold here uses the existential joint Pasch result, not the triangle-only tower bound.

For a concrete consequence, take $\theta=1/2$. Call a coarse block favoured when the product of its three signs is positive. Each such block has target $3m^2/16$, and each other block has target $m^2/16$. Relative to a row-column block of size $m^2/4$, these are the proportions 75% and 25%, with error at most $4\varepsilon$. Taking $t=2^{-1/4}$ gives

$$
\kappa(1/2,0)=\frac{17}{64},\qquad
\kappa(1/2,2^{-1/4})=\frac{51}{128}=\frac32\frac{17}{64},
\qquad
\operatorname{int}(L_t)-\operatorname{int}(L_0)
\geq\left(\frac{17}{128}-2\varepsilon\right)m^2.              \tag{8.28}
$$

Thus the leading coefficients differ by 50%, and the counts are separated whenever $\varepsilon<17/256$.  More generally, every coefficient

$$
c\in[17/64,17/32),\qquad t=(64c/17-1)^{1/4},                \tag{8.29}
$$

is available with the same coarse profile and prescribed linear targets. The threshold depends on c; the upper endpoint is excluded because $t=1$ loses the positive lower bound in (8.21). 

The family of linear tests is fixed before either square is chosen, as required in Theorem 8.4.


\begin{figure}[htbp]
\centering
\includegraphics[width=0.94\linewidth]{figures/profile_en.pdf}
\caption{The leading intercalate coefficient for a fixed coarse profile. The endpoint at t = 1 is excluded; the theorem has an additive error and a threshold depending on t.}
\end{figure}

### 8.2. Five parts and rainbow triangles

Consider the complete five-partite graph $K_{s,s,s,s,s}$, allowing precisely the triangles meeting three distinct classes. It has $5s$ vertices and $10s^2$ edges. A triangle decomposition requires $3\mid10s^2$, hence $3\mid s$. Write $s=3m$.

#### 8.2.1. A physical witness

Appendix B lists thirty triangles decomposing $K_{3,3,3,3,3}$. Replace every vertex of this base graph by a copy of a finite abelian group A of order m. Above each base triangle, choose the triples of group elements satisfying $x+y+z=0$.

For an edge between two blown-up base vertices, the base pair lies in exactly one base triangle. Its two group coordinates then determine the third uniquely. Therefore every edge is covered once, and the lifted triangles give a decomposition of the five-partite graph with class size $3m$. Taking $A=\mathbb Z/m\mathbb Z$ supplies every positive m. This establishes H2 by a physical witness, without appealing to an abstract divisibility criterion.

#### 8.2.2. The remaining hypotheses and the conclusion

By completeness between the parts, every edge has exactly $3s$ common neighbours in the other three classes. The uniform weight $\mu(Q)=1/(3s)$ has edge sums one. With host order $5s$, H1 holds for $C=5/3$: its upper diffuse bound equals $1/(3s)$, and the lower bound is smaller.

For each compatible third label, a pair has s common neighbours. Appendix A gives $(s-1)^2$ hinges of order six. Thus H3 and H4 hold with $\alpha=1/100$ and $h=6$, because for $s\geq2$,

$$
(s-1)^2\geq\frac{s^2}{4}=\frac1{100}(5s)^2.                        \tag{8.30}
$$

**Corollary 8.5.** Fix $\eta>0$ and an integer $q\geq0$. For every sufficiently large integer m, put $s=3m$. For every family of at most $s^q$ signed tests on the rainbow triangles of $K_{s,s,s,s,s}$, each bounded in absolute value by one, there is a rainbow decomposition $\mathcal D$ such that

$$
\left|\sum_{Q\in\mathcal D}w_j(Q)
-\frac1{3s}\sum_{Q\in\mathcal T}w_j(Q)\right|\leq\eta s^2          \tag{8.31}
$$

for every j, and

$$
\left|P(\mathcal D)-\frac{|\mathcal P(\mathcal T)|}{(3s)^4}\right|
\leq\eta s^2.                                                       \tag{8.32}
$$

*Proof.* The uniform seed verifies H1, the lifted base decomposition verifies H2, and the part sizes and Appendix A verify H3 and H4. Apply Theorem T+ with precision $\eta/25$. The host order is $5s$, so its error becomes $\eta s^2$. Each Pasch contains four triangles of weight $1/(3s)$, giving (8.32).

The base construction already proves existence at these orders. The added conclusion is simultaneous control of the prescribed statistics and Pasch count. No closed expression for $|\mathcal P(\mathcal T)|$ is needed for this application.

## 9. Formal proof and the audited freeze

The proof object for T is `TypedTriangle.Vortex.main_theorem_T`, in `MainPaperIII.lean`; the joint result is `TypedTriangle.Vortex.main_theorem_T_with_triangle_monitors_and_pasch`, in `MainPaperIIIPasch.lean`. The general theorems use these complete formal proofs. Sections 3–6 and Appendix D explain their interfaces and assembly; they do not reproduce every local construction lemma as an independent prose proof.

Theorem 8.4 has the assembled endpoint `TypedTriangle.Applications.Latin.TwoScale.latin_two_scale_with_blocks`, in `ApplicationsTwoScaleFinal.lean`. It constructs the fine signs, proves simultaneous concentration, verifies the seed and rounds both profiles. Its count-gap corollary is `intercalate_gap_of_targets`. The proof uses the bound (8.24); the exact finite identity (8.23) is proved above and is not asserted to be a separately assembled Lean identity.

The source supplement has 1,141 project modules and six successful endpoint axiom audits, using only `propext`, `Classical.choice` and `Quot.sound`. The companion records the archive SHA-256, source manifest, validated object reuse and recompilation of fifteen files whose comments alone were updated. The mathematical Lean code and H1–H4 are unchanged. The profile and one-scale Latin endpoints are `latin_square_with_profile_statistics`, `uniform_with_intercalates` and `signed_profile_with_intercalates`, in the namespace `TypedTriangle.Applications.Latin`. The five-partite endpoint is `TypedTriangle.Applications.FivePartite.main_theorem`. The companion lists their separate build targets and audit queries.

## Acknowledgments

The author is deeply grateful to his wife María Paz and his children Lucas, Juan Cristóbal, Francisca, Raimundo and Benjamín for their love, patience and support.


## Use of artificial intelligence and computational tools

Claude, by Anthropic, and ChatGPT/Codex, by OpenAI, were used to explore and check arguments and to prepare the manuscript. Aristotle, by Harmonic, contributed to exploring approaches, searching for counterexamples, developing proofs, and formalizing and reviewing them in Lean. Its role was not limited to translating finished proofs.

Certo [16] and Jacobian [17] were used to explore finite instances, check identities and assess candidate constructions. These computations informed the development of the arguments; finite checks were not treated as proofs of universal statements.

The author remains responsible for the arguments, citations, code and presentation. No AI system is listed as an author.


## Appendix A. A six-vertex physical hinge

The underlying graph is the octahedron $K_{2,2,2}$ with parts $\{u,x\}$, $\{v,y\}$ and $\{a,b\}$, with the two root faces removed. This is the 2-sphere hinge of [14, Definition 14.3], and belongs to the octahedral exchange construction in [15, Section 5.1]. Here we give its labelled realization and count. Let $\{u,v,a\}$ and $\{u,v,b\}$ be rainbow triangles with $a\ne b$. Choose x in the class of u with $x\ne u$, and y in the class of v with $y\ne v$. Set

$$
J=\{uy,xv,xy,xa,xb,ya,yb\}.                                       \tag{A.1}
$$

All six vertices are distinct. The labels of a and b may coincide; both differ from the labels of u and v. The edges of J avoid both root triangles. Its two decompositions are

$$
\begin{aligned}
J\cup W_a&=E(\{u,y,a\})\,\dot\cup\,
 E(\{x,v,a\})\,\dot\cup\,E(\{x,y,b\}),\\
J\cup W_b&=E(\{u,y,b\})\,\dot\cup\,
 E(\{x,v,b\})\,\dot\cup\,E(\{x,y,a\}).
\end{aligned}                                                       \tag{A.2}
$$

\begin{figure}[H]
\centering
\includegraphics[width=0.98\linewidth]{figures/hinge_en.pdf}
\caption{The six-vertex hinge of Appendix A. The left panel shows the seven-edge auxiliary graph J. Each of the other panels partitions J together with one wedge into three rainbow triangles, distinguished by both colour and line style. Crossings are not vertices. This example belongs to the complete multipartite applications; H4 allows other hinges.}
\label{fig:hinge}
\end{figure}

Every triangle displayed is rainbow. Expanding its three edges verifies (A.2) and the pairwise disjointness of those edge sets. Every one of the six vertices is incident with J, so the hinge order is six.

If each class has size m, there are $(m-1)^2$ choices. They give distinct edge sets: y is recovered as the unique neighbour of u in J, and x as the unique neighbour of v in J. This is a count of physical hinges, with no division by a labelling multiplicity.

## Appendix B. The thirty-block five-partite base

Write $i_a$ for vertex a in class i, where $i\in\{0,1,2,3,4\}$ and $a\in\{0,1,2\}$. The following thirty triples are the base witness used in Section 8.2. Each triple meets three distinct classes. Each cross-class pair occurs exactly once; the finite verification is also recorded in the source.

| | | |
|---|---|---|
| $\{0_0,1_0,4_0\}$ | $\{0_1,2_1,4_2\}$ | $\{1_0,3_0,4_1\}$ |
| $\{0_0,1_1,3_2\}$ | $\{0_1,3_1,4_0\}$ | $\{1_1,2_1,4_0\}$ |
| $\{0_0,1_2,2_1\}$ | $\{0_2,1_0,3_1\}$ | $\{1_1,2_2,3_0\}$ |
| $\{0_0,2_0,4_1\}$ | $\{0_2,1_1,2_0\}$ | $\{1_1,3_1,4_2\}$ |
| $\{0_0,2_2,3_1\}$ | $\{0_2,1_2,4_2\}$ | $\{1_2,2_0,3_1\}$ |
| $\{0_0,3_0,4_2\}$ | $\{0_2,2_1,3_0\}$ | $\{1_2,2_2,4_1\}$ |
| $\{0_1,1_0,2_2\}$ | $\{0_2,2_2,4_0\}$ | $\{1_2,3_2,4_0\}$ |
| $\{0_1,1_1,4_1\}$ | $\{0_2,3_2,4_1\}$ | $\{2_0,3_0,4_0\}$ |
| $\{0_1,1_2,3_0\}$ | $\{1_0,2_0,4_2\}$ | $\{2_1,3_1,4_1\}$ |
| $\{0_1,2_0,3_2\}$ | $\{1_0,2_1,3_2\}$ | $\{2_2,3_2,4_2\}$ |

There are $\binom52\cdot3^2=90$ cross-class edges and thirty triples, each with three edges. Checking pair occurrence therefore verifies an exact decomposition, not merely the correct total number of blocks.

## Appendix C. Identifying the tower height

The height H in (7.6) is specified by the following composition of natural-number functions. Their exact definitions are supplied in the fixed source snapshot and indexed in the formalization companion. Thus evaluating the bound requires those definitions; this displayed composition alone is not their expansion.

$$
\begin{aligned}
h_*&=2h-3,\\
M&=\operatorname{triangleThresholdInputMajorant}(K,h,q),\\
A&=\operatorname{thresholdAgendaMajorant}(M),\\
R&=\operatorname{thresholdLayerScale}(A,h_*),\\
T&=\operatorname{thresholdTerminalScale}(R),\\
U&=\operatorname{thresholdReserveScale}(T,h_*),\\
H(K,h,q)&=\operatorname{triangleThresholdFinalMajorant}(U,h_*).
\end{aligned}                                                       \tag{C.1}
$$

## Appendix D. Preparation and completion estimates

The constants in this appendix are local to each construction. In particular, the bounds called K and D below need not be the normalization K in (7.4) or the same bounds in another subsection. We retain the notation used in each estimate.

### D.1. Preparation and certificates

A prepared core has four properties after every deletion of at most a fixed fraction of its vertices: common-neighbour supply, hinge supply, a lower order bound and persistence of the physical integer lattice. These are simultaneous properties of one core, not fresh choices for each demand.

Here is the finite descent behind persistence. Let the physical local quotients in a nested deletion chain have rank at most d, torsion order at most T, and surjective transition maps. Read these surjections from the smaller host to the larger host, that is, opposite to the deletion order. In this direction, at most d steps decrease the rank. In a constant-rank interval, every noninjective map decreases torsion order by a factor of at least two. Thus the number of noninjective steps is at most

$$
L=d+(d+1)\lfloor\log_2T\rfloor. \tag{D.1}
$$

Fix a deletion budget b with all sets of size at most (L+1)b inside the admissible window. If every set A of size at most Lb admitted a further deletion of at most b causing noninjectivity, choose such deletions successively, starting from the empty set. After j steps the union has size at most jb. This constructs L+1 noninjective steps, a contradiction. Hence one A works for every later deletion of at most b. Restriction places each surviving demand in the new local group; injectivity then preserves its lattice membership. The local quotient and restriction lemmas used here are part of the formal construction.

We spell out the quotient argument. For a host J, let $M_J$ be its local group of integer edge demands: demands vanish off J and at each vertex their incident demand is an integer combination of the incident vectors of allowed triangles. Let $\Lambda_J$ be its triangle lattice. Every triangle incidence vector satisfies these local conditions, so $\Lambda_J\subseteq M_J$. For nested hosts $J'\subseteq J$ with the same labels, extending triangle coefficients by zero gives inclusions of both groups. Hence inclusion induces $M_{J'}/\Lambda_{J'}\longrightarrow M_J/\Lambda_J$. Its kernel consists exactly of classes of demands $x\in M_{J'}\cap\Lambda_J$. It is injective if and only if $M_{J'}\cap\Lambda_J=\Lambda_{J'}$: an old lattice demand that is still local in the smaller host has a certificate there.

The locality qualification must be checked before using this equality. In the construction it is supplied by the small-deletion local-window result, used in `physical_vertex_first_entry_lattice` in `VertexFirstEntry.lean`. The finite descent gives injectivity uniformly for every subsequent deletion within the budget. These two facts have distinct roles: the local-window result places the surviving demand in the domain group, and injectivity makes its class zero there. The geometric local-window result remains a construction lemma of the formal supplement; injectivity alone would not replace it.

Finally we pass from deleting edges incident to vertices to the genuine induced host. Extend a demand on the surviving vertices by zero on all other edges. Extend a triangle certificate by the same rule; its incidence equation is preserved, because each triangle uses only surviving vertices. If the demand also vanishes at a further deleted set, its zero extension does too. Apply persistence in the ambient vertex set, and restrict the resulting certificate to the remaining vertices. All its triangles already avoid the deleted sets, so restriction preserves every surviving edge equation. Restricting the original zero extension returns the original demand. This proves the transport used in `induced_lattice_persistence` in `PreparedCoreConstruction.lean`.

A bounded certificate for a demand avoiding a forbidden vertex set is now constructed in the surviving host and extended by zero. This preserves its incidence equation and norm. For simultaneous demands, let K bound each certificate norm, J be their number, and let the admissible forbidden size be at least half of the preparation budget. Choose an integer q satisfying

$$
q\geq1,\qquad 6KJ\leq q\beta n. \tag{D.2}
$$

Here $\beta>0$ is the permitted vertex-deletion fraction. Usage counts earlier certificates containing v outside their demand frontiers, once per certificate; it is not the sum of coefficient multiplicities. Before each choice, forbid vertices with usage at least q, except those on the current frontier. A certificate of norm at most K meets at most 3K vertices, so total usage is at most 3KJ. Condition (D.2) leaves at most half the preparation budget forbidden. The next certificate exists and keeps each auxiliary usage at most q. If $F_v$ counts frontiers containing v, summing certificates gives

$$
\|c\|_1\leq KJ,\qquad \operatorname{load}_v(c)\leq K(F_v+q). \tag{D.3}
$$

To obtain the numerical bound, use the choice $q=\max\{1,\lceil6KJ/(\beta n)\rceil\}$ from the certificate construction, with $\beta>0$ and $n>0$. It satisfies $q\leq6KJ/(\beta n)+1$. This local load parameter is separate from the exponent q in T+. Here the frontier of a demand is the set of endpoints of its nonzero edges. The routed demands satisfy the following frontier estimate, with $\delta>0$ and $D\geq0$. Substitute the bound on q into (D.3), use the bound on J, and bound the remaining ceiling by its argument plus one. The two rounding errors give the additive term in the last line:

$$
\begin{aligned}J&\leq2e,\quad e=\|x\|_1,\\ F_v&\leq(4D+3)d_{|x|}(v)+\left\lceil\frac{32De}{\delta n}\right\rceil+2D,\\ \operatorname{load}_v(c)&\leq K\left((4D+3)d_{|x|}(v)+\left(\frac{32D}{\delta}+\frac{12K}{\beta}\right)\frac e n+2D+2\right).\end{aligned}\tag{D.4}
$$

### D.2. The exact seed belongs to the actual child

Let J be the actual child after payments and reference trimming, with order $n>0$. Assume $\mathbf1_{E(J)}\in\Lambda_J$, and that $\mu_0$ vanishes outside its allowed triangles. Take $C\geq1$, $\varepsilon\geq0$, and a smooth inverse of norm constant K on the real image of $A_J$. The remaining assumptions are $1/(2Cn)\leq\mu_0(Q)\leq2C/n$ for allowed Q, $\|r\|_\infty\leq\varepsilon$ for $r=\mathbf1_{E(J)}-A_J\mu_0$, and $K\varepsilon\leq1/(4C)$. Physicality and support put r in the real image. The inverse therefore supplies a supported correction $\xi$ with

$$
\begin{gathered}A_J\xi=r,\qquad |\xi(Q)|\leq\frac{K\varepsilon}{n},\\
A_J(\mu_0+\xi)=\mathbf1_{E(J)},\qquad \frac1{4Cn}\leq\mu_0(Q)+\xi(Q)\leq\frac{4C}{n}.\end{gathered}\tag{D.5}
$$

Exactness follows by adding the edge equations. The lower bound follows by subtracting the correction margin; the upper bound uses C at least one. The construction supplies the inverse and preliminary seed on this J. Applying an inverse from the original host would not prove this statement.

### D.3. A reserve selected before the residual

Suppose the terminal window has at most u vertices. Enumerate the admissible residuals: physical edge sets supported on that window. Robust supply here means that each such nonempty residual has an absorber of at most s edges avoiding any forbidden edge set within a fixed maximum-degree budget. The proof of T uses the uniform reserve theorem `uniform_terminal_absorber_avoiding_outer_core`; its explicit-order counterpart is used only for Section 7. Place the absorbers successively, forbidding the protected graph, all terminal-window edges and all earlier absorbers.

$$
\#\{M\}\leq2^{u^2},\qquad |R|\leq s2^{u^2}. \tag{D.6}
$$

The forbidden maximum degree is bounded by the protected degree plus u plus the displayed reserve size. The order threshold makes this fit the robust-supply budget. The absorbers are pairwise edge-disjoint and avoid the terminal window edges. Their inactive modes, which decompose each absorber without adding a residual, together decompose R. For a later residual M, activate its absorber and keep every other absorber in its inactive mode. This decomposes the union of R and M. The choice of R preceded M.

### D.4. Paying for mixed Pasch configurations

Start with the previous available family, whose pair-codegree is at most L. The new stock adds at most 1, the withdrawal universe at most 63, and the bank modes at most 2. These three additions give L+66. Adding the new packing contributes at most one more, giving L+67. Withdrawn and activated payments already belong to these unions. Counts of Pasches need not add across the constituent families. The initial family for the inner stages is the output of the exterior layer, which applies this estimate with an empty previous family: the stock, withdrawal universe, bank modes and packing give $1+63+2+1=67$. This is the bound passed to `TrackingState.initial` from `PaschConcreteOuterLayer.lean` at $j=0$; each subsequent inner layer adds at most 67, giving $L\leq67+67j$.

The local insertion estimates charge a newly created Pasch to a changed triangle and bound its three other triangle choices by a cubic pair-codegree factor. For each successive ambient union they give a fixed geometry coefficient times $nm_j(L+\ell)^3$, where n is the original order, $m_j$ the current order, and $\ell\leq184$ a local offset. Summing these coefficients gives G. Since $L\leq67+67j$, (D.8) bounds the cube by $318^3(j+1)^3$. The source sets $D=(|G|+1)318^3$, yielding the layer bound below. The geometric insertion estimates are the local formal lemmas assembled in `PaschConcreteInnerAdaptiveLayers.lean`; this argument explains how their bounds give the global recurrence.

The next host contracts by at least sixteen. Define its remaining allowance by

$$
\begin{gathered}16m_{j+1}\leq m_j,\qquad \Delta P_j\leq Dn(j+1)^3m_j,\\ \Phi_j=2Dn8^jm_j,\qquad (j+1)^3\leq8^j,\\ Dn(j+1)^3m_j+\Phi_{j+1}\leq Dn8^jm_j+16Dn8^jm_{j+1}\leq\Phi_j.\end{gathered}\tag{D.7}
$$

The cubic bound starts with equality at j = 0. Its induction step follows from $(j+2)/(j+1)\leq2$. Also, substituting the definition of $\Phi_{j+1}$ gives the factor 16 in the last line of (D.7); the contraction then bounds that term by $Dn8^jm_j$. The inequality proves by induction that the current Pasch count plus its remaining allowance never exceeds its initial budget. The coefficient D is fixed before the host. Its formal definition bounds the stock, withdrawal, bank, packing and cover increments in consecutive ambient unions. The shift 318 arises from a pair-codegree bound of 67+67j and a maximal local offset of 184:

$$
L+184\leq251+67j\leq318(j+1).\tag{D.8}
$$

The numerical shifts in this estimate come from bounds on unions of available triangle families. For any pair of vertices, the number of triangles in a union containing that pair is at most the sum of the corresponding numbers in its constituents; overlaps can only lower it. This explains the addition of codegree budgets. In `PaschDenseWeightedWithdrawal.lean` the withdrawal universe has bound 63, assembled as 2+61. In `PaschConcreteStructuredLayer.lean` it is combined with a packing of bound 1. The bank contributes the further bound 2 recorded above. The proof in `PaschConcreteInnerAdaptiveLayers.lean` bounds its intermediate shifts by 184 and then applies the affine codegree estimate. Substitution of the previous bound 67+67j gives (D.8). The value 318 is a convenient uniform majorant, not a new density hypothesis. These local family bounds are inputs from the formal construction; (D.7) explains how they enter the global error estimate.

Stop when the current order is at most the integer fourth root of n. The remaining exact completion, including the terminal reserve, adds at most K plus the square of that order triangles. Taking n at least the two ceilings below bounds this number by $2\tau n$.

$$
n\geq\lceil K/\tau\rceil,\quad n\geq\lceil1/\tau^2\rceil,\qquad K+m_j^2\leq2\tau n.\tag{D.9}
$$

The cutoff gives $m_j^2\leq\sqrt n$. The first order condition gives $K\leq\tau n$; the second gives $\sqrt n\leq\tau n$, since $\tau>0$. Adding the two bounds proves (D.9).

Fix two distinct vertices a and b of a root triangle Q. In a Pasch containing Q, each of a and b belongs to exactly one further triangle, say A and B. These are distinct: otherwise that triangle would share the edge ab with Q. Any two triangles in a Pasch meet in exactly one vertex. They cannot be disjoint: they would then exhaust the six vertices, and a third triangle could meet each in at most one vertex, leaving room for at most two of its three vertices. Thus A and B meet at a vertex x outside Q. In the ambient packing the pair ax determines A uniquely, and bx determines B uniquely, since an edge occurs in at most one triangle. The three triangles Q, A and B determine the fourth: precisely the three vertices currently of degree one must belong to it. Thus two rooted Pasches assigned the same x are equal. This injects the rooted configurations into the vertices outside Q, giving at most n−3 configurations, and hence the bound n used here. Charging each new Pasch to its first added triangle bounds the terminal contribution by $2\tau n^2$. Combining initial error $\sigma$, tracked growth $\tau$ and terminal error $2\tau$ gives

$$
|P(\mathcal D)-P_\mu|\leq(\sigma+3\tau)n^2=\eta n^2,\qquad \sigma=\tau=\eta/4.\tag{D.10}
$$

## References

[1] J. P. Traverso Gianini, *Triangle decompositions I: Formalizing the Nash–Williams theorem in Lean*. Preprint 1.0, 20 October 2026. [doi:10.5281/zenodo.23428173](https://doi.org/10.5281/zenodo.23428173).

[2] J. P. Traverso Gianini, *Triangle decompositions II: Robust absorption for typed triangles*. Preprint 1.0, 20 October 2026. [doi:10.5281/zenodo.23502224](https://doi.org/10.5281/zenodo.23502224).

[3] P. Keevash, *Coloured and directed designs*. arXiv:1807.05770, version 2, 2020. [arXiv](https://arxiv.org/abs/1807.05770v2).

[4] S. Ehard, S. Glock and F. Joos, *Pseudorandom hypergraph matchings*. Combinatorics, Probability and Computing **29** (2020), 868–885. [doi:10.1017/S0963548320000280](https://doi.org/10.1017/S0963548320000280).

[5] J. P. Traverso Gianini, *Formalizing Delcourt–Postle’s refined absorption in Lean*. Research note, preprint 1.0.1, 27 October 2026. [doi:10.5281/zenodo.23715622](https://doi.org/10.5281/zenodo.23715622).

[6] M. Delcourt and L. Postle, *Refined Absorption: A New Proof of the Existence Conjecture*. arXiv:2402.17855v1, 2024. [arXiv](https://arxiv.org/abs/2402.17855v1).

[7] L. Postle, *Refined Absorption: A New Proof of the Existence Conjecture and its Applications to Extremal and Probabilistic Design Theory*. arXiv:2510.19978v1, 2025. [arXiv](https://arxiv.org/abs/2510.19978v1).

[8] F. Garbe, R. Hancock, J. Hladký and M. Sharifzadeh, *Limits of Latin Squares*. Discrete Analysis **2023:8**. [doi:10.19086/da.83253](https://doi.org/10.19086/da.83253).

[9] M. Kwan, A. Sah and M. Sawhney, *Large deviations in random Latin squares*. Bulletin of the London Mathematical Society **54** (2022), 1420–1438. [doi:10.1112/blms.12638](https://doi.org/10.1112/blms.12638).

[10] M. Kwan, A. Sah, M. Sawhney and M. Simkin, *Substructures in Latin squares*. arXiv:2202.05088v4, 2022. [arXiv](https://arxiv.org/abs/2202.05088v4).

[11] B. Barber, D. Kühn, A. Lo, D. Osthus and A. Taylor, *Clique decompositions of multipartite graphs and completion of Latin squares*. Journal of Combinatorial Theory, Series A **151** (2017), 146–201. [doi:10.1016/j.jcta.2017.04.005](https://doi.org/10.1016/j.jcta.2017.04.005).

[12] R. Montgomery, *Fractional clique decompositions of dense partite graphs*. Combinatorics, Probability and Computing **26** (2017), 911–943. [doi:10.1017/S0963548317000165](https://doi.org/10.1017/S0963548317000165).

[13] M. Kwan and B. Sudakov, *Intercalates and Discrepancy in Random Latin Squares*. arXiv:1607.04981v2, 2017. [arXiv](https://arxiv.org/abs/1607.04981v2).

[14] M. Delcourt and L. Postle, *A Proof of Nash-Williams’ Conjecture*. arXiv:2606.11178v1, 2026. [arXiv](https://arxiv.org/abs/2606.11178v1).

[15] P. Keevash, *The existence of designs II*. arXiv:1802.05900v1, 2018. [arXiv](https://arxiv.org/abs/1802.05900v1).

[16] J. P. Traverso Gianini, *Certo*, software repository. <https://github.com/jtraverso/certo-math>.

[17] *Jacobian*, software repository. <https://github.com/morluto/jacobian>.

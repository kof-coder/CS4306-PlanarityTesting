# Planarity Testing – Hopcroft–Tarjan (HT) and Baseline

# Problem / Output

# Given an undirected graph G = (V, E), decide PLANAR if all blocks (biconnected components)

# admit an embedding without edge crossings; otherwise NON-PLANAR.

# Inputs / Definitions (HT)

# order[u]: DFS discovery time of u

# low[u]: minimum order reachable from u (via tree or back edges)

# parent[u]: DFS parent of u

# EDGE_STACK: stack collecting edges of the current DFS block

# A "block" (biconnected component) is formed by popping from EDGE_STACK under the closing rule.

PROCEDURE PLANARITY_HT(G):
time ← 0
for each vertex u in V(G):
order[u] ← -1
low[u] ← -1
parent[u] ← -1
clear EDGE_STACK

    for each vertex u in V(G):
        if order[u] = -1:
            if DFS(u) = NON-PLANAR:
                return NON-PLANAR
            # (Optional) If EDGE_STACK still has edges here, pop them as a residual block
            # and run EMBED_BLOCK once more if your implementation requires it.

    return PLANAR   # no block embedding failed

# Depth-First Search with block detection

PROCEDURE DFS(u):
order[u] ← time
low[u] ← time
time ← time + 1

    for each v in adj[u]:
        if order[v] = -1 then
            # Tree edge
            parent[v] ← u
            PUSH(EDGE_STACK, (u, v))

            if DFS(v) = NON-PLANAR:
                return NON-PLANAR

            low[u] ← MIN(low[u], low[v])

            # Closing rule: a biconnected component (block) completed
            if low[v] ≥ order[u] then
                B ← ∅
                repeat
                    e ← POP(EDGE_STACK)
                    ADD_TO_SET(B, e)
                until e = (u, v)

                if EMBED_BLOCK(B) = FALSE then
                    return NON-PLANAR

        else if v ≠ parent[u] AND order[v] < order[u] then
            # Back edge to an ancestor
            PUSH(EDGE_STACK, (u, v))
            low[u] ← MIN(low[u], order[v])

    return PLANAR

# Block embedding interface (combinatorial embedding at high level)

# Maintain circular order of half-edges per vertex; adding each item must preserve:

# - existing circular orders at every vertex

# - consistency with current face boundaries

# - no creation of crossing "conflict pairs"

PROCEDURE EMBED_BLOCK(B):
E ← INIT_EMBEDDING(B) # data structure for circular orders around vertices

    for each item in DFS_CONSISTENT_ORDER(B) do
        ok ← ADD_TO_EMBEDDING(E, item)
        if ok = FALSE then
            return FALSE

    return TRUE

## Baseline (Naïve) – Validation Only

This baseline invokes a library planarity checker (e.g., NetworkX `check_planarity`) strictly as a yardstick.
We rely on it to confirm that our Hopcroft–Tarjan implementation agrees on PLANAR/NON-PLANAR outcomes for canonical graphs such as K5 and K3,3.
It remains outside the project’s main focus; we make no claims about its performance beyond the library call itself.
The baseline records only the boolean verdict—no embeddings or runtime data—so comparisons stay simple.
Keeping this lightweight validator available helps us spot regressions quickly while preserving attention on the primary algorithm.

PROCEDURE NAIVE_PLANARITY(G):
return LIBRARY_CHECK_PLANARITY(G) # e.g., NetworkX check_planarity(...)

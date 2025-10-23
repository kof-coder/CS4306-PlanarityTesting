# Planarity Testing – Hopcroft–Tarjan (HT) and Baseline

## Problem / Output
Given an undirected graph G=(V,E), decide PLANAR if all blocks (biconnected components) admit an embedding without edge crossings; otherwise NON-PLANAR.

---

## Inputs / Definitions (HT)
- `order[u]`: DFS discovery time of u
- `low[u]`: minimum `order` reachable from u (via tree or back edges)
- `parent[u]`: DFS parent of u
- **Edge stack**: collects edges of current DFS block
- **Block (biconnected component)**: popped by closing rule and sent to embedder

---

## HT Step Breakdown (from R)
- **Scope**: handle one connected component at a time (DFS restarts on unvisited vertices).
- **Global arrays**: initialize `order[]`, `low[]`, `parent[]`; start time counter at 0.
- **Edge stack**: push edges as they’re discovered to accumulate the current block.
- **DFS**: for each unvisited u, run DFS(u).
- **Tree edge (u,v)**:
  - push (u,v); recurse to v; on return: `low[u] = min(low[u], low[v])`.
- **Back edge (u,v)** with v an ancestor of u:
  - push (u,v); update `low[u] = min(low[u], order[v])`.
- **Closing rule**: when returning from (u,v) with `low[v] >= order[u]`:
  - pop from edge stack until (u,v) popped → edges form block B.
  - send B to `EMBED-BLOCK(B)`; if it fails → NON-PLANAR immediately.
- **Embedding structure idea**:
  - maintain circular order of half-edges around each vertex;
  - every attachment must preserve existing circular orders and face boundaries;
  - back-edge attachments must not create “conflict pairs”.
- **Decision**: if any block fails → NON-PLANAR; if all succeed → PLANAR.
- **Complexity**: one DFS + linear-time embedding per block ⇒ overall **O(n + m)**.
- **Mini example**: discover (u,v) → finish v → `low[v] ≥ order[u]` → pop component → embed → resume DFS.

---

## Pseudocode (HT)


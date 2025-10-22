Input: an undirected graph G = (V, E), possibly disconnected.

Output: PLANAR if all blocks can be embedded without crossing; otherwise NON-PLANAR.

Scope: handle one connected component at a time (DFS restarts on unvisited vertices).

Initialize global counters and arrays:

order[u] = discovery time of vertex u,

low[u] = lowest reachable discovery order from u (including back edges),

parent[u] = DFS parent of u.

Maintain an edge stack to collect edges belonging to the current DFS block.

For each unvisited vertex u, run a depth-first search.

On visiting a new vertex v from u, push edge (u, v) onto the edge stack.

For each tree edge (u, v) discovered in DFS:

recursively explore vertex v.

after returning, update low[u] = min(low[u], low[v]).

For each back edge (u, v) (where v is an ancestor of u):

push (u, v) onto the edge stack,

update low[u] = min(low[u], order[v]).

Closing rule: when low[v] >= order[u], the DFS subtree rooted at v has finished a block.

Pop edges from the stack until (u, v) is removed to form the block B.

Send block B to EMBED-BLOCK(B) for planarity testing and embedding.

EMBED-BLOCK(B):

initialize embedding structure E for block B.

maintain circular order of half-edges around each vertex.

ensure each attachment preserves this circular order.

check that no new attachment conflicts with existing face boundaries.

enforce that back-edge attachments do not create “conflict pairs.”

If any edge or attachment violates these constraints, EMBED-BLOCK(B) returns False.

If any block fails embedding, stop immediately and return NON-PLANAR.

If all blocks succeed, return PLANAR.

Example: DFS discovers (u, v), later finds low[v] >= order[u], pops all edges for that component, sends them to EMBED-BLOCK, and resumes DFS on remaining edges.

Complexity: one DFS pass plus linear-time block embedding → overall O(n + m).

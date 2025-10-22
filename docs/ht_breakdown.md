1. Input: an undirected graph G = (V, E), possibly disconnected.

2. Output: PLANAR if all blocks can be embedded without crossing; otherwise NON-PLANAR.

3. Scope: handle one connected component at a time (DFS restarts on unvisited vertices).

4. Initialize global counters and arrays:

5. order[u] = discovery time of vertex u,

6. low[u] = lowest reachable discovery order from u (including back edges),

7. parent[u] = DFS parent of u.

8. Maintain an edge stack to collect edges belonging to the current DFS block.

9. For each unvisited vertex u, run a depth-first search.

10. On visiting a new vertex v from u, push edge (u, v) onto the edge stack.

11. For each tree edge (u, v) discovered in DFS:

12. recursively explore vertex v.

13. after returning, update low[u] = min(low[u], low[v]).

14. For each back edge (u, v) (where v is an ancestor of u):

15. push (u, v) onto the edge stack,

16. update low[u] = min(low[u], order[v]).

17. Closing rule: when low[v] >= order[u], the DFS subtree rooted at v has finished a block.

18. Pop edges from the stack until (u, v) is removed to form the block B.

19. Send block B to EMBED-BLOCK(B) for planarity testing and embedding.

20. EMBED-BLOCK(B):

21. initialize embedding structure E for block B.

22. maintain circular order of half-edges around each vertex.

23. ensure each attachment preserves this circular order.

24. check that no new attachment conflicts with existing face boundaries.

25. enforce that back-edge attachments do not create “conflict pairs.”

26. If any edge or attachment violates these constraints, EMBED-BLOCK(B) returns False.

27. If any block fails embedding, stop immediately and return NON-PLANAR.

28. If all blocks succeed, return PLANAR.

Example: DFS discovers (u, v), later finds low[v] >= order[u], pops all edges for that component, sends them to EMBED-BLOCK, and resumes DFS on remaining edges.

Complexity: one DFS pass plus linear-time block embedding → overall O(n + m).

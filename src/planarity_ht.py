# src/planarity_ht.py

class HopcroftTarjanPlanarity:
    def __init__(self, G):
        """
        G: Graph instance (from graph.py)
        We'll prepare all the arrays we need for DFS.
        """
        self.G = G
        n = G.n

        self.order = [-1] * n      # discovery time
        self.low = [-1] * n        # lowest reachable discovery time
        self.parent = [-1] * n     # DFS parent
        self.time = 0              # global timestamp counter
        self.edge_stack = []       # stack of edges (u,v)
        self.non_planar = False    # gets set if any block fails

    def is_planar(self):
        """
        Driver.
        Runs DFS from every unvisited vertex (to handle disconnected graphs).
        Returns True if the whole graph is planar, False otherwise.
        """
        for u in range(self.G.n):
            if self.order[u] == -1:
                self.dfs(u)

                if self.non_planar:
                    return False

                # Optional cleanup:
                # If there are still edges in edge_stack here, that's a block.
                # In full HT we would flush it and embed it. We'll skip for now
                # because that case shouldn't matter for correctness of the check
                # with our current placeholder.
                if self.edge_stack:
                    block_edges = []
                    while self.edge_stack:
                        block_edges.append(self.edge_stack.pop())
                    ok = self.embed_block(block_edges)
                    if not ok:
                        self.non_planar = True
                        return False

        return (not self.non_planar)

    def dfs(self, u):
        """
        Depth-first search.
        - Assign order[u], low[u]
        - Explore neighbors
        - Track tree edges and back edges
        - Extract a biconnected component (block) when low[v] >= order[u]
        """
        self.order[u] = self.time
        self.low[u] = self.time
        self.time += 1

        for v in self.G.adj[u]:
            # Case 1: Tree edge (v not visited yet)
            if self.order[v] == -1:
                self.parent[v] = u
                # push edge (u,v) on the edge stack
                self.edge_stack.append((u, v))

                # recurse
                self.dfs(v)
                if self.non_planar:
                    return  # early exit if already broken

                # update low[u] after returning
                self.low[u] = min(self.low[u], self.low[v])

                # Closing rule:
                # if v (child) can't reach an ancestor of u,
                # we just finished a block.
                if self.low[v] >= self.order[u]:
                    block_edges = []
                    # pop edges until we pop (u,v)
                    while True:
                        e = self.edge_stack.pop()
                        block_edges.append(e)
                        if e == (u, v) or e == (v, u):
                            break

                    # Check this block for planarity via embedding
                    ok = self.embed_block(block_edges)
                    if not ok:
                        self.non_planar = True
                        return

            # Case 2: Back edge to an ancestor
            elif v != self.parent[u] and self.order[v] < self.order[u]:
                # push edge (u,v)
                self.edge_stack.append((u, v))
                # update low[u] using ancestor's discovery time
                self.low[u] = min(self.low[u], self.order[v])

        # done with dfs(u)

    def embed_block(self, block_edges):
        """
        Placeholder for Week 4.
        block_edges is the list of edges (u,v) belonging to one biconnected component.

        Final version will maintain/merge circular orders and detect conflicts.
        For now we just return True so the algorithm can run end-to-end.
        """
        # TODO: real combinatorial embedding + conflict-pair logic in Week 4
        return True

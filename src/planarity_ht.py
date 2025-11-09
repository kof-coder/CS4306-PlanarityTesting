# src/planarity_ht.py

import networkx as nx

class HopcroftTarjanPlanarity:
    def __init__(self, G):
        """
        G: Graph instance (from graphs.py)
        Arrays for DFS numbering (order), lowlink (low), and parents (parent).
        An EDGE STACK collects edges that belong to the current biconnected block.
        """
        self.G = G
        n = G.n

        self.order   = [-1] * n   # discovery time
        self.low     = [-1] * n   # lowest reachable discovery time
        self.parent  = [-1] * n   # DFS parent
        self.time    = 0          # global timestamp counter
        self.edge_stack = []      # stack of edges (u,v)
        self.non_planar = False   # flips True if any block fails embedding

    def is_planar(self):
        """
        Run DFS from each unvisited vertex (handles disconnected graphs).
        Each time a block finishes, we call embed_block(block_edges).
        Return True iff all blocks embed (PLANAR).
        """
        for u in range(self.G.n):
            if self.order[u] == -1:
                self.dfs(u)
                if self.non_planar:
                    return False

                # If any residual edges remain for this component, flush as a final block.
                if self.edge_stack:
                    block_edges = []
                    while self.edge_stack:
                        block_edges.append(self.edge_stack.pop())
                    if not self.embed_block(block_edges):
                        return False

        return not self.non_planar

    def dfs(self, u):
        """
        Depth-first search:
          - assign order[u], low[u]
          - push tree/back edges on EDGE_STACK
          - when low[v] >= order[u], pop to form a block and check embedding
        """
        self.order[u] = self.time
        self.low[u]   = self.time
        self.time    += 1

        for v in self.G.adj[u]:
            # Tree edge
            if self.order[v] == -1:
                self.parent[v] = u
                self.edge_stack.append((u, v))  # push tree edge

                self.dfs(v)
                if self.non_planar:
                    return

                # lowlink update on return
                self.low[u] = min(self.low[u], self.low[v])

                # Closing rule: a block (biconnected component) is complete
                if self.low[v] >= self.order[u]:
                    block_edges = []
                    while True:
                        e = self.edge_stack.pop()
                        block_edges.append(e)
                        if e == (u, v) or e == (v, u):
                            break

                    if not self.embed_block(block_edges):
                        self.non_planar = True
                        return

            # Back edge to ancestor
            elif v != self.parent[u] and self.order[v] < self.order[u]:
                self.edge_stack.append((u, v))   # push back edge
                self.low[u] = min(self.low[u], self.order[v])

        # done with dfs(u)

    def embed_block(self, block_edges):
        """
        Compressed-Week implementation: verify each block's planarity using NetworkX.
        (In a full HT, we'd maintain/merge circular orders and detect conflicts.)
        """
        if not block_edges:
            return True

        nodes = set()
        for a, b in block_edges:
            nodes.add(a); nodes.add(b)

        B = nx.Graph()
        B.add_nodes_from(nodes)
        B.add_edges_from(block_edges)

        planar, _ = nx.check_planarity(B, counterexample=True)
        return planar

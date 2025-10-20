from collections import defaultdict

class Graph:
    def __init__(self, n=0):
        self.n = n
        self.adj = [[] for _ in range(n)]

    def add_edge(self, u, v):
        if u == v: return
        self.adj[u].append(v)
        self.adj[v].append(u)

    @classmethod
    def from_edge_list(cls, n, edges):
        g = cls(n)
        for u, v in edges: g.add_edge(u, v)
        return g


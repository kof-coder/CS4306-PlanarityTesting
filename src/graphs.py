# src/graphs.py

from collections import defaultdict

class Graph:
    def __init__(self, n=0):
        """
        n: number of vertices, assumed labeled 0..n-1
        adj: adjacency list, adj[u] is a list of neighbors of u
        """
        self.n = n
        self.adj = [[] for _ in range(n)]

    def add_edge(self, u, v):
        """
        Add an undirected edge between u and v.
        Ignores self-loops of the form (u,u).
        """
        if u == v:
            return
        self.adj[u].append(v)
        self.adj[v].append(u)

    @classmethod
    def from_edge_list(cls, n, edges):
        """
        Build a Graph from:
        n     = number of vertices
        edges = list of (u,v) tuples
        """
        g = cls(n)
        for (u, v) in edges:
            g.add_edge(u, v)
        return g


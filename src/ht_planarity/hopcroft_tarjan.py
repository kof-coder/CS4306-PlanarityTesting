from dataclasses import dataclass

@dataclass
class DFSInfo:
    parent: list
    order: list
    low: list
    visited: list
    time: int = 0

class HopcroftTarjanPlanarity:
    def __init__(self, G):
        self.G = G
        n = G.n
        self.info = DFSInfo(parent=[-1]*n, order=[-1]*n, low=[-1]*n, visited=[False]*n)

    def is_planar(self):
        # 1) run DFS to get order/low + biconnected decomposition hooks
        self._dfs_all()
        # 2) for each biconnected component: run embedding feasibility checks
        #    (placeholder; to be filled Week 3/4)
        return True  # temp stub

    def _dfs_all(self):
        for v in range(self.G.n):
            if not self.info.visited[v]:
                self._dfs(v)

    def _dfs(self, u):
        self.info.visited[u] = True
        self.info.order[u] = self.info.low[u] = self.info.time; self.info.time += 1
        for v in self.G.adj[u]:
            if not self.info.visited[v]:
                self.info.parent[v] = u
                self._dfs(v)
                self.info.low[u] = min(self.info.low[u], self.info.low[v])
            elif v != self.info.parent[u]:
                # back-edge
                self.info.low[u] = min(self.info.low[u], self.info.order[v])


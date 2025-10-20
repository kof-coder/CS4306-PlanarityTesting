# Educational baseline for small graphs: delegate to networkx.planarity if allowed.
# If not allowed, later we can add simple K5/K3,3 minor detectors for tiny n.
import networkx as nx

def naive_is_planar(n, edges):
    G = nx.Graph(); G.add_nodes_from(range(n)); G.add_edges_from(edges)
    planar, _ = nx.check_planarity(G, counterexample=True)
    return planar


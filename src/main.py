from utils.io import load_edgelist
from graphs import Graph
from ht_planarity.hopcroft_tarjan import HopcroftTarjanPlanarity
from brute_force.naive_planarity import naive_is_planar

def run(path):
    n, edges = load_edgelist(path)
    G = Graph.from_edge_list(n, edges)
    ht = HopcroftTarjanPlanarity(G)
    is_planar_ht = ht.is_planar()
    is_planar_naive = naive_is_planar(n, edges)  # baseline
    print(f"HT: {is_planar_ht} | Baseline: {is_planar_naive}")

if __name__ == "__main__":
    run("data/samples/k5.edgelist")


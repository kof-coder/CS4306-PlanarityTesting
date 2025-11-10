# main.py

from src.graphs import Graph
from src.planarity_ht import HopcroftTarjanPlanarity
from src.brute_force.naive_planarity import naive_is_planar
from src.utils.timing import bench


def load_edgelist_file(path):
    """
    Reads an edgelist file like:
        0 1
        0 2
        1 2
    Returns:
        n      = max node index + 1
        edges  = list of (u,v)
    """
    edges = []
    nodes_seen = set()
    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            u_str, v_str = line.split()
            u = int(u_str); v = int(v_str)
            edges.append((u, v))
            nodes_seen.update([u, v])
    n = max(nodes_seen) + 1 if nodes_seen else 0
    return n, edges


def run_on_file(path):
    print(f"=== Testing graph from {path} ===")
    n, edges = load_edgelist_file(path)

    # Build our Graph and HT instance
    G = Graph.from_edge_list(n, edges)
    ht = HopcroftTarjanPlanarity(G)

    # Time HT
    ht_result, ht_ms = bench(ht.is_planar)()

    # Time baseline
    base_result, base_ms = bench(naive_is_planar)(n, edges)

    print(f"HT says:        {'PLANAR' if ht_result else 'NON-PLANAR'}  ({ht_ms:.2f} ms)")
    print(f"Baseline says:  {'PLANAR' if base_result else 'NON-PLANAR'}  ({base_ms:.2f} ms)")
    print()


if __name__ == "__main__":
    # Core non-planar samples
    run_on_file("data/samples/k5.edgelist")
    run_on_file("data/samples/k3_3.edgelist")

    # Planar samples
    run_on_file("data/samples/grid_3x3.edgelist")
    run_on_file("data/samples/cycle_6.edgelist")

    # Extra samples (add these files below)
    run_on_file("data/samples/tree_10.edgelist")
    run_on_file("data/samples/wheel_6.edgelist")

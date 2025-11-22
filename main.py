# main.py

from src.graphs import Graph
from src.planarity_ht import HopcroftTarjanPlanarity
from src.brute_force.naive_planarity import naive_is_planar
from src.utils.timing import bench


def load_edgelist_file(path):
    edges = []
    nodes_seen = set()
    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            u_str, v_str = line.split()
            u = int(u_str)
            v = int(v_str)
            edges.append((u, v))
            nodes_seen.update([u, v])
    n = max(nodes_seen) + 1 if nodes_seen else 0
    return n, edges


def run_on_file(path):
    print(f"=== Testing graph from {path} ===")
    n, edges = load_edgelist_file(path)

    # Build Graph and HT instance
    G = Graph.from_edge_list(n, edges)
    ht = HopcroftTarjanPlanarity(G)

    # Run HT
    ht_result, ht_ms = bench(ht.is_planar)()
    print(f"HT says:        {'PLANAR' if ht_result else 'NON-PLANAR'}  ({ht_ms:.2f} ms)")

    # Run factorial baseline only if small enough
    if n <= 8:
        base_result, base_ms = bench(naive_is_planar)(n, edges)
        print(f"Baseline says:  {'PLANAR' if base_result else 'NON-PLANAR'}  ({base_ms:.2f} ms)")
    else:
        print("Baseline skipped: n too large for factorial brute force")

    print()


if __name__ == "__main__":
    # Small non-planar
    run_on_file("data/samples/k5.edgelist")
    run_on_file("data/samples/k3_3.edgelist")

    # Small planar
    run_on_file("data/samples/grid_3x3.edgelist")
    run_on_file("data/samples/cycle_6.edgelist")

    # Medium / large planar graphs (HT only)
    run_on_file("data/samples/tree_10.edgelist")
    run_on_file("data/samples/wheel_6.edgelist")
    run_on_file("data/samples/path_12.edgelist")
    run_on_file("data/samples/grid_4x4.edgelist")

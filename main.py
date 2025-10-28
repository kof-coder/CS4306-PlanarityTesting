# main.py

from src.graph import Graph
from src.planarity_ht import HopcroftTarjanPlanarity

# If J has created src/baseline_check.py with naive_planarity(), we can import it.
# For now we’ll wrap that import in a try so main still runs even if it's not there yet.
try:
    from src.baseline_check import naive_planarity
    HAVE_BASELINE = True
except ImportError:
    HAVE_BASELINE = False


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
            u = int(u_str)
            v = int(v_str)
            edges.append((u, v))
            nodes_seen.add(u)
            nodes_seen.add(v)

    n = max(nodes_seen) + 1 if nodes_seen else 0
    return n, edges


def run_on_file(path):
    print(f"=== Testing graph from {path} ===")

    # 1. Load edge list
    n, edges = load_edgelist_file(path)

    # 2. Build our Graph
    G = Graph.from_edge_list(n, edges)

    # 3. Run Hopcroft–Tarjan
    ht = HopcroftTarjanPlanarity(G)
    ht_result = ht.is_planar()

    print("HT says:", "PLANAR" if ht_result else "NON-PLANAR")

    # 4. (Optional) Compare with baseline/naive checker if available
    if HAVE_BASELINE:
        base_res = naive_planarity(n, edges)
        print("Baseline says:", "PLANAR" if base_res else "NON-PLANAR")

    print()


if __name__ == "__main__":
    # Try on the sample graphs your team already added
    run_on_file("data/samples/k5.edgelist")
    run_on_file("data/samples/k3_3.edgelist")
    # You can add these once you fill them in:
    # run_on_file("data/samples/grid_3x3.edgelist")
    # run_on_file("data/samples/cycle_6.edgelist")


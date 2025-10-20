def load_edgelist(path):
    edges, nodes = [], set()
    with open(path) as f:
        for line in f:
            if not line.strip() or line.startswith('#'): continue
            u, v = map(int, line.split())
            edges.append((u, v))
            nodes.update([u, v])
    n = max(nodes) + 1 if nodes else 0
    return n, edges


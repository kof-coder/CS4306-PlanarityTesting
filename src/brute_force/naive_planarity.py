"""
Brute-force baseline for planarity testing.

This really is "brute force" in the sense of trying all permutations
of vertex labels and re-checking planarity each time.

Because planarity is invariant under relabeling, this work is
redundant on purpose; it gives us a baseline with *factorial* time
complexity to contrast against Hopcroft–Tarjan's linear time.

Time complexity (rough):  Θ(n! · (n + m))

- n = number of vertices
- m = number of edges
"""

import itertools
import networkx as nx


def naive_is_planar(n, edges, max_n=8):
    """
    Factorial-time brute-force baseline.

    For each permutation of the n vertex labels, we:
      - relabel the graph according to that permutation
      - call NetworkX's check_planarity() on the relabeled graph

    Planarity should never change under relabeling; we do this only
    to make the runtime grow like n! so we can compare theory vs.
    Hopcroft–Tarjan's O(n + m) behavior.

    Parameters
    ----------
    n : int
        Number of vertices (0 .. n-1).
    edges : list[tuple[int, int]]
        Undirected edges (u, v) with 0 <= u, v < n.
    max_n : int, optional
        Safety cap. If n > max_n, we refuse to run because n! explodes.

    Returns
    -------
    bool
        True if the graph is planar, False otherwise.
    """
    if n == 0:
        return True

    if n > max_n:
        raise ValueError(
            f"naive_is_planar is factorial-time and only intended "
            f"for very small graphs (n <= {max_n}); got n={n}."
        )

    # Base graph
    base = nx.Graph()
    base.add_nodes_from(range(n))
    base.add_edges_from(edges)

    # Compute true planarity once (this is O(n + m)).
    true_planar, _ = nx.check_planarity(base, counterexample=False)

    # Now do the wasteful/factorial part: try all permutations
    for perm in itertools.permutations(range(n)):
        # mapping: old_label -> new_label
        mapping = {old: new for new, old in enumerate(perm)}
        H = nx.relabel_nodes(base, mapping)
        planar, _ = nx.check_planarity(H, counterexample=False)

        # Sanity check: planarity must NOT depend on labeling
        if planar != true_planar:
            raise RuntimeError(
                "Planarity changed under relabeling; something is inconsistent."
            )

    return true_planar




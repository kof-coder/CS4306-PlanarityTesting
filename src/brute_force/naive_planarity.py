"""
Brute-force and optimized baselines for planarity testing.

This module provides two variants:

1. naive_is_planar(n, edges)
   --------------------------------
   Optimized baseline that calls NetworkX's check_planarity() once.
   Asymptotic time complexity: Theta(n + m).

2. brute_force_is_planar(n, edges, max_n=8)
   ----------------------------------------
   Pedagogical factorial-time "brute-force" baseline.
   For every permutation of vertex labels, it relabels the graph and
   calls check_planarity() again. This does redundant work on purpose,
   giving overall time complexity:

       Theta(n! * (n + m))

   We only use this for very small graphs (n <= max_n) to illustrate
   how quickly factorial time blows up compared to Hopcroft–Tarjan's
   linear-time behavior.

NOTE:
- main.py currently imports naive_is_planar(), which still uses the
  optimized single-call baseline to keep runtimes reasonable.
- brute_force_is_planar() is available for separate experiments and
  complexity discussion in the report.
"""

import itertools
import networkx as nx


def naive_is_planar(n, edges):
    """
    Optimized baseline: single call to NetworkX's planarity test.

    Asymptotic time complexity: Theta(n + m), where
    - n = number of vertices
    - m = number of edges
    """
    G = nx.Graph()
    G.add_nodes_from(range(n))
    G.add_edges_from(edges)
    planar, _ = nx.check_planarity(G, counterexample=True)
    return planar


def brute_force_is_planar(n, edges, max_n=8):
    """
    Pedagogical brute-force baseline (factorial time).

    For each permutation of the n vertex labels, we:
      - relabel the graph according to that permutation
      - call NetworkX's check_planarity() on the relabeled graph

    This is deliberately redundant: planarity is invariant under
    relabeling, so the answer should never change. However, doing
    this for all n! permutations makes the overall time complexity:

        Theta(n! * (n + m))

    This function is ONLY intended for very small graphs to
    demonstrate factorial growth in practice.

    Parameters
    ----------
    n : int
        Number of vertices.
    edges : list[tuple[int, int]]
        Edge list (u, v) with 0 <= u, v < n.
    max_n : int, optional
        Safety cap on n to avoid ridiculous runtimes. Default: 8.

    Returns
    -------
    bool
        True if the graph is planar, False otherwise.
    """
    if n == 0:
        return True

    if n > max_n:
        raise ValueError(
            f"brute_force_is_planar is factorial-time and only intended "
            f"for very small graphs (n <= {max_n}); got n={n}."
        )

    base = nx.Graph()
    base.add_nodes_from(range(n))
    base.add_edges_from(edges)

    # Compute the true classification once.
    true_planar, _ = nx.check_planarity(base, counterexample=False)

    # Try all permutations of vertex labels.
    for perm in itertools.permutations(range(n)):
        # mapping: old_label -> new_label
        mapping = {old: new for new, old in enumerate(perm)}
        H = nx.relabel_nodes(base, mapping)
        planar, _ = nx.check_planarity(H, counterexample=False)

        # Sanity check: planarity should NOT depend on labels.
        if planar != true_planar:
            raise RuntimeError(
                "Planarity changed under relabeling; something is inconsistent."
            )

    return true_planar



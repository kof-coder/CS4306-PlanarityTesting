"""NetworkX-backed baseline checks for graph planarity.

Provides a thin wrapper around ``networkx.check_planarity`` so that the
Hopcroft–Tarjan implementation can be validated against a trusted library.
"""

from __future__ import annotations

from collections.abc import Iterable
from typing import Tuple, Union

import networkx as nx

Edge = Tuple[int, int]


def _to_networkx_graph(n: int, edges: Iterable[Edge]) -> nx.Graph:
    """Convert our integer-labelled graph into a NetworkX graph."""
    graph = nx.Graph()
    graph.add_nodes_from(range(n))
    graph.add_edges_from(edges)
    return graph


def naive_planarity(
    n: int,
    edges: Iterable[Edge],
    *,
    return_certificate: bool = False,
) -> Union[bool, Tuple[bool, Union[nx.PlanarEmbedding, nx.Graph]]]:
    """Check planarity using NetworkX.

    Args:
        n: Number of labelled vertices in the graph.
        edges: Iterable of undirected edges ``(u, v)``.
        return_certificate: When ``True`` also return the embedding or
            Kuratowski certificate produced by NetworkX.

    Returns:
        Either a ``bool`` (if ``return_certificate`` is ``False``) or a
        ``(bool, certificate)`` tuple mirroring ``networkx.check_planarity``.
    """
    nx_graph = _to_networkx_graph(n, edges)
    is_planar, certificate = nx.check_planarity(
        nx_graph, counterexample=return_certificate
    )
    if return_certificate:
        return is_planar, certificate
    return is_planar


__all__ = ["naive_planarity"]

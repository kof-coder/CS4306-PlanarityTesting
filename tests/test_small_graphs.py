from pathlib import Path

import networkx as nx

from src.baseline_check import naive_planarity
from src.utils.io import load_edgelist

FIXTURE_DIR = Path(__file__).resolve().parents[1] / "data" / "samples"


def _load_sample(name: str):
	n, edges = load_edgelist(str(FIXTURE_DIR / name))
	return n, edges


def test_k5_is_non_planar():
	n, edges = _load_sample("k5.edgelist")
	assert not naive_planarity(n, edges)


def test_k3_3_is_non_planar():
	n, edges = _load_sample("k3_3.edgelist")
	assert not naive_planarity(n, edges)


def test_triangle_is_planar():
	n = 3
	edges = [(0, 1), (1, 2), (2, 0)]
	assert naive_planarity(n, edges)


def test_return_certificate_flag_planar():
	n = 3
	edges = [(0, 1), (1, 2), (2, 0)]
	is_planar, certificate = naive_planarity(n, edges, return_certificate=True)
	assert is_planar
	assert isinstance(certificate, nx.PlanarEmbedding)


def test_return_certificate_flag_non_planar():
	n, edges = _load_sample("k5.edgelist")
	is_planar, certificate = naive_planarity(n, edges, return_certificate=True)
	assert not is_planar
	assert isinstance(certificate, nx.Graph)


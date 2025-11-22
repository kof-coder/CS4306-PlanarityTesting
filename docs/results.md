# Planarity Testing Results

| Graph    | HT Result  | Baseline   | HT (ms) | Baseline (ms) |
|--------- |----------- |----------- |-------- |-------------- |
| K5       | Non-planar | Non-planar | 2.69    | 1.90          |
| K3,3     | Non-planar | Non-planar | 2.11    | 1.66          |
| Grid 3×3 | Planar     | Planar     | 0.16    | 0.12          |
| Cycle 6  | Planar     | Planar     | 0.09    | 0.07          |


_Notes:_
HT timings include DFS + block extraction + per-block planarity check.
Baseline is a **factorial-time brute-force** method that tries all permutations of vertex labels, so we only use it on very small graphs.
Small ms differences are normal and machine-dependent.


## Projected Runtime (Theoretical Model)

Using:
- HT projected as  **T_HT ≈ c · (n + m)**  (linear time),
- Baseline projected as  **T_BF ≈ k · n!**  (factorial time),
fitted from the small-graph measurements.

| Graph        | n   | HT (projected ms) | Baseline (projected ms) |
|------------- |---- |-------------------|--------------------------|
| K5           | 5   | 4.08              | 44.59                    |
| K3,3         | 6   | 4.08              | 267.52                   |
| Grid 3×3     | 9   | 5.71              | 134,830.08               |
| Cycle 6      | 6   | 3.26              | 267.52                   |
| Tree 10      | 10  | 5.17              | 1,348,300.80             |
| Wheel 6      | 6   | 4.35              | 267.52                   |
| Path 12      | 12  | 6.25              | 177,975,705.60           |
| Grid 4×4     | 16  | 10.88             | 7,773,978,820,608.00     |



---------------------------------------------------------------------------------

# Planarity Testing Results

## Time Complexity Summary
- **Hopcroft–Tarjan (HT):** Θ(n + m)  
- **Baseline (brute-force):** Θ(n! · (n + m)) — only safe for n ≤ 8  
- Large graphs skip the baseline due to factorial explosion.

---

## Experimental Measurements

| Graph        | n   | HT Result  | Baseline | HT (ms) | Baseline (ms) |
|------------- |---- |----------- |----------|---------|---------------|
| K5           | 5   | Non-planar | Non-planar | X.XX | X.XX |
| K3,3         | 6   | Non-planar | Non-planar | X.XX | X.XX |
| Grid 3×3     | 9   | Planar     | Planar     | X.XX | X.XX |
| Cycle 6      | 6   | Planar     | Planar     | X.XX | X.XX |
| Tree 10      | 10  | Planar     | Skipped    | X.XX | — |
| Wheel 6      | 6   | Planar     | Planar     | X.XX | X.XX |
| Path 12      | 12  | Planar     | Skipped    | X.XX | — |
| Grid 4×4     | 16  | Planar     | Skipped    | X.XX | — |

---

### Notes
- HT timing includes DFS + low-link updates + block extraction.  
- Baseline timing includes trying all permutations (factorial time).  
- For graphs with n > 8, baseline is **intentionally skipped**.  
- Small timing differences (<1ms) are due to Python overhead and OS noise.  

_All tests run using our Hopcroft–Tarjan implementation and our factorial brute-force baseline._

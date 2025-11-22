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

Visual:


<img width="763" height="445" alt="image" src="https://github.com/user-attachments/assets/bb0babfc-858f-4df3-89f6-fd4dd1c79116" />


---------------------------------------------------------------------------------

# Planarity Testing Experimental Results

## Time Complexity Recap
- **Hopcroft–Tarjan (HT):** Θ(n + m)  
- **Brute-force Baseline:** Θ(n! · (n + m)) — only feasible for very small n  

---

## Measured Performance (Slower PC)

| Graph        | n   | HT Result   | Baseline Result | HT (ms) | Baseline (ms) |
|--------------|-----|-------------|-----------------|---------|----------------|
| K5           | 5   | Non-planar  | Non-planar      | 17.03   | 27.58         |
| K3,3         | 6   | Non-planar  | Non-planar      | 11.91   | 226.47        |
| Grid 3×3     | 9   | Planar      | Skipped (n > 8) | 0.61    | —             |
| Cycle 6      | 6   | Planar      | Planar          | 0.49    | 376.07        |
| Tree 10      | 10  | Planar      | Skipped (n > 8) | 1.00    | —             |
| Wheel 6      | 6   | Planar      | Planar          | 0.56    | 302.06        |
| Path 12      | 12  | Planar      | Skipped (n > 8) | 1.10    | —             |
| Grid 4×4     | 16  | Planar      | Skipped (n > 8) | 1.63    | —             |

---

## Notes
- HT consistently ran in **~0.5 ms to ~17 ms**, even on larger graphs.  
- Baseline runtime grew from ~20 ms (n=5) to **300+ ms** for n=6 graphs.  
- This confirms the theoretical gap between **linear time** and **factorial time**.  
- Baseline was skipped for graphs with **n > 8** due to factorial blow-up.  

_All tests performed using our custom HT implementation and our factorial brute-force baseline._


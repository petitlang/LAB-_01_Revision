## File Structure:

```
/LAB _07/
├── exercise1_divide_conquer.py
├── exercise2_fractal_drawing.py
├── exercise3_procedural_generation.py
└── README.md
```

---

## Team members and assigned exercises

Team: T14

Mouzheng LI: 1 & 3
Yuefan LIU: 2 & 3

Collaborate : 3 & Final Question

---

## Dependencies and Language version

Please use **python 3.11 or higher version**.

Please use **JDK 17 or a higher version**.

---

# Brief description of each solution

## Solution of exercise1_divide_conquer


This exercise uses **divide and conquer** to recursively split a 2D rectangular space into smaller regions.

The function `split_region()` divides one region into four equal quadrants until the region becomes smaller than the minimum size.

Then `count_points_in_region()` checks how many points fall inside a given rectangle.

Finally, `find_dense_regions()` combines recursive splitting and point counting to detect regions whose point density is higher than a given threshold.

This solution is useful for  **spatial partitioning, clustering, and dense area detection** .

---

## Solution of exercise2_fractal_drawing


This exercise focuses on  **recursive fractal generation and analysis** .

The function `draw_sierpinski()` builds a Sierpinski triangle by recursively drawing three smaller triangles at each step.

The function `draw_tree()` creates a recursive tree structure by splitting each branch into two smaller branches with different angles.

The function `fractal_dimension()` estimates the complexity of a fractal by using the  **box-counting method** , which counts non-empty boxes at different scales and computes the slope in the log-log graph.

This solution demonstrates both **fractal drawing** and  **fractal measurement** .

---

## Solution of exercise3_procedural_generation


This exercise applies recursion to  **terrain and line generation** .

The function `midpoint_displacement()` recursively divides a line segment and adds a random offset to the midpoint, producing a rough natural-looking curve.

The function `generate_terrain()` uses the **diamond-square algorithm** to recursively refine a 2D grid and generate terrain heights from four corner values.

The function `detect_artifacts()` scans the generated terrain and identifies suspicious cells where the height difference between neighboring positions is too large.

This solution is suitable for  **procedural generation, terrain modeling, and artifact detection** .

---

# Complexity analysis summary

## Complexity of exercise1_divide_conquer

The function `split_region()` divides one region into four smaller quadrants at each recursive step, so its time complexity is  **O(4^d)** , where `d` is the recursion depth, and its space complexity is **O(d)** because of the recursive call stack.

The function `count_points_in_region()` scans all input points once, so its time complexity is **O(N)** and its space complexity is  **O(1)** .

The function `find_dense_regions()` combines recursive splitting with point counting. Since each recursive call may scan all `N` points and the number of recursive calls grows like `4^d`, the overall time complexity is  **O(N · 4^d)** , while the recursive stack space is  **O(d)** .

---

## Complexity of exercise2_fractal_drawing

For `draw_sierpinski()`, each triangle generates three smaller recursive calls, so the time complexity is **O(3^d)** and the space complexity is  **O(d)** .

For `draw_tree()`, each branch generates two smaller branches, so the time complexity is **O(2^d)** and the space complexity is  **O(d)** .

For `fractal_dimension()`, the algorithm tests several box sizes and counts non-empty boxes for each size. If the image has `M` pixels and there are `k` tested box sizes, the total time complexity is approximately  **O(k · M)** , while the space complexity is **O(k)** for storing logarithm values.

---

## Complexity of exercise3_procedural_generation

Exercise 3 applies recursion to line subdivision and terrain generation.

For `midpoint_displacement()`, each segment is divided into two smaller segments at each recursive step, so the time complexity is **O(2^d)** and the space complexity is  **O(d)** .

For `generate_terrain()`, the `diamond_square()` process recursively divides the terrain into four smaller regions, so its time complexity is approximately  **O(4^d)** , with recursive stack space  **O(d)** . In practice, the total work is also related to the number of grid cells being refined.

For `detect_artifacts()`, the algorithm scans the terrain grid once and compares neighboring cells, so if the grid contains `W × H` cells, the time complexity is **O(W · H)** and the space complexity is  **O(A)** , where `A` is the number of detected suspicious cells.

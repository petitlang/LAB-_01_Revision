import random
from typing import List, Tuple


class Canvas:
    """
    Simple canvas that records line segments.
    This avoids GUI dependency and is convenient for testing.
    """

    def __init__(self):
        self.lines = []

    def draw_line(self, x1: float, y1: float, x2: float, y2: float) -> None:
        self.lines.append((round(x1, 4), round(y1, 4), round(x2, 4), round(y2, 4)))

    def clear(self) -> None:
        self.lines.clear()

    def count(self) -> int:
        return len(self.lines)

    def preview(self, limit: int = 10) -> None:
        for line in self.lines[:limit]:
            print(line)
        if len(self.lines) > limit:
            print(f"... ({len(self.lines) - limit} more lines)")


# ---------------------------------------------------
# 1. midpoint_displacement(x1, y1, x2, y2, roughness, depth)
# ---------------------------------------------------
def midpoint_displacement(
    canvas: Canvas,
    x1: float,
    y1: float,
    x2: float,
    y2: float,
    roughness: float,
    depth: int
) -> None:
    """
    Recursive midpoint displacement.

    Base case:
        depth == 0 -> draw one line

    Recursive case:
        compute midpoint with random vertical offset
        then recursively subdivide into 2 segments
    """
    if depth < 0:
        raise ValueError("depth must be non-negative")
    if roughness < 0:
        raise ValueError("roughness must be non-negative")

    if depth == 0:
        canvas.draw_line(x1, y1, x2, y2)
    else:
        xm = (x1 + x2) / 2
        ym = (y1 + y2) / 2 + roughness * random.uniform(-1, 1)

        midpoint_displacement(canvas, x1, y1, xm, ym, roughness, depth - 1)
        midpoint_displacement(canvas, xm, ym, x2, y2, roughness, depth - 1)


# ---------------------------------------------------
# 2. generate_terrain(width, height, roughness, depth)
# Auxiliary: diamond_square(...)
# ---------------------------------------------------
def diamond_square(
    terrain: List[List[float]],
    x1: int,
    y1: int,
    x2: int,
    y2: int,
    roughness: float,
    depth: int
) -> None:
    """
    Recursive diamond-square refinement on a subregion.
    """
    if depth == 0:
        return

    if x2 - x1 < 2 or y2 - y1 < 2:
        return

    xm = (x1 + x2) // 2
    ym = (y1 + y2) // 2

    # center
    center = (
        terrain[x1][y1]
        + terrain[x1][y2]
        + terrain[x2][y1]
        + terrain[x2][y2]
    ) / 4.0
    terrain[xm][ym] = center + roughness * random.uniform(-1, 1)

    # edges
    terrain[x1][ym] = (terrain[x1][y1] + terrain[x1][y2]) / 2.0 + roughness * random.uniform(-1, 1)
    terrain[x2][ym] = (terrain[x2][y1] + terrain[x2][y2]) / 2.0 + roughness * random.uniform(-1, 1)
    terrain[xm][y1] = (terrain[x1][y1] + terrain[x2][y1]) / 2.0 + roughness * random.uniform(-1, 1)
    terrain[xm][y2] = (terrain[x1][y2] + terrain[x2][y2]) / 2.0 + roughness * random.uniform(-1, 1)

    diamond_square(terrain, x1, y1, xm, ym, roughness / 2, depth - 1)
    diamond_square(terrain, xm, y1, x2, ym, roughness / 2, depth - 1)
    diamond_square(terrain, x1, ym, xm, y2, roughness / 2, depth - 1)
    diamond_square(terrain, xm, ym, x2, y2, roughness / 2, depth - 1)


def generate_terrain(width: int, height: int, roughness: float, depth: int) -> List[List[float]]:
    """
    Generate a 2D terrain grid using recursive diamond-square refinement.
    """
    if width <= 0 or height <= 0:
        raise ValueError("width and height must be positive")
    if roughness < 0:
        raise ValueError("roughness must be non-negative")
    if depth < 0:
        raise ValueError("depth must be non-negative")

    terrain = [[0.0 for _ in range(height)] for _ in range(width)]

    terrain[0][0] = 0.0
    terrain[0][height - 1] = 0.0
    terrain[width - 1][0] = 0.0
    terrain[width - 1][height - 1] = 0.0

    diamond_square(terrain, 0, 0, width - 1, height - 1, roughness, depth)
    return terrain


# ---------------------------------------------------
# 3. detect_artifacts(terrain_grid, threshold)
# ---------------------------------------------------
def detect_artifacts(terrain_grid: List[List[float]], threshold: float) -> List[Tuple[int, int]]:
    """
    Scan the terrain grid and detect suspicious coordinates where
    height differences with neighbors exceed the threshold.
    """
    if threshold < 0:
        raise ValueError("threshold must be non-negative")
    if not terrain_grid or not terrain_grid[0]:
        raise ValueError("terrain_grid must not be empty")

    rows = len(terrain_grid)
    cols = len(terrain_grid[0])

    artifacts = []

    for i in range(rows - 1):
        for j in range(cols - 1):
            if (
                abs(terrain_grid[i][j] - terrain_grid[i + 1][j]) > threshold
                or abs(terrain_grid[i][j] - terrain_grid[i][j + 1]) > threshold
            ):
                artifacts.append((i, j))

    return artifacts


# ---------------------------------------------------
# Helper functions for pretty printing
# ---------------------------------------------------
def print_terrain(terrain: List[List[float]], limit_rows: int = 8, limit_cols: int = 8) -> None:
    rows = min(len(terrain), limit_rows)
    cols = min(len(terrain[0]), limit_cols)

    for i in range(rows):
        row_values = [f"{terrain[i][j]:6.2f}" for j in range(cols)]
        print(" ".join(row_values))

    if len(terrain) > limit_rows or len(terrain[0]) > limit_cols:
        print("...")


def main():
    random.seed(42)  # reproducible results

    print("=== Ex3 Python Implementation ===")

    # ---------------------------------------------------
    # Normal Example
    # ---------------------------------------------------
    print("\n--- Normal Example: midpoint_displacement ---")
    canvas = Canvas()
    midpoint_displacement(canvas, 0, 0, 100, 0, roughness=1, depth=4)
    print("Number of final line segments:", canvas.count())
    canvas.preview(10)

    print("\n--- Normal Example: generate_terrain ---")
    terrain = generate_terrain(9, 9, roughness=1, depth=3)
    print("Generated terrain preview:")
    print_terrain(terrain)

    print("\n--- Normal Example: detect_artifacts ---")
    artifacts = detect_artifacts(terrain, threshold=0.8)
    print("Number of suspicious coordinates:", len(artifacts))
    print("First few artifacts:", artifacts[:10])

    # ---------------------------------------------------
    # Test set for edge cases
    # ---------------------------------------------------
    print("\n=== Test set for edge cases ===")

    # 1. midpoint_displacement(x1, y1, x2, y2, roughness, depth)
    print("\n1. midpoint_displacement(x1, y1, x2, y2, roughness, depth)")

    # Edge Case 1 — depth = 0
    try:
        print("\nEdge Case 1 — depth = 0")
        c = Canvas()
        midpoint_displacement(c, 0, 0, 100, 0, roughness=1, depth=0)
        print("Expected result: only one straight line is drawn.")
        print("Actual number of lines:", c.count())
        c.preview()
    except Exception as e:
        print("Error:", e)

    # Edge Case 2 — roughness = 0
    try:
        print("\nEdge Case 2 — roughness = 0")
        c = Canvas()
        midpoint_displacement(c, 0, 0, 100, 0, roughness=0, depth=4)
        print("Expected result: the generated line remains smooth and regular.")
        print("Actual number of lines:", c.count())
        c.preview(10)
    except Exception as e:
        print("Error:", e)

    # Edge Case 3 — negative depth
    try:
        print("\nEdge Case 3 — negative depth")
        c = Canvas()
        midpoint_displacement(c, 0, 0, 100, 0, roughness=1, depth=-1)
        print("Expected result: invalid input should be rejected.")
    except Exception as e:
        print("Expected result: invalid input should be rejected.")
        print("Actual result: Error caught ->", e)

    # 2. generate_terrain(width, height, roughness, depth)
    print("\n2. generate_terrain(width, height, roughness, depth)")

    # Edge Case 1 — depth = 0
    try:
        print("\nEdge Case 1 — depth = 0")
        terrain0 = generate_terrain(9, 9, roughness=1, depth=0)
        print("Expected result: no recursive refinement is applied.")
        print("Actual terrain preview:")
        print_terrain(terrain0)
    except Exception as e:
        print("Error:", e)

    # Edge Case 2 — roughness = 0
    try:
        print("\nEdge Case 2 — roughness = 0")
        terrain1 = generate_terrain(9, 9, roughness=0, depth=3)
        print("Expected result: terrain is smoother and more regular.")
        print("Actual terrain preview:")
        print_terrain(terrain1)
    except Exception as e:
        print("Error:", e)

    # Edge Case 3 — invalid grid size
    try:
        print("\nEdge Case 3 — invalid grid size")
        terrain2 = generate_terrain(0, 9, roughness=1, depth=2)
        print("Expected result: input should be rejected.")
        print("Actual result:", terrain2)
    except Exception as e:
        print("Expected result: input should be rejected.")
        print("Actual result: Error caught ->", e)

    # 3. detect_artifacts(terrain_grid, threshold)
    print("\n3. detect_artifacts(terrain_grid, threshold)")

    # Edge Case 1 — threshold = 0
    try:
        print("\nEdge Case 1 — threshold = 0")
        terrain_test = generate_terrain(9, 9, roughness=1, depth=3)
        result = detect_artifacts(terrain_test, threshold=0)
        print("Expected result: almost all changing cells are flagged as suspicious.")
        print("Actual number of suspicious coordinates:", len(result))
        print("First few:", result[:10])
    except Exception as e:
        print("Error:", e)

    # Edge Case 2 — very large threshold
    try:
        print("\nEdge Case 2 — very large threshold")
        terrain_test = generate_terrain(9, 9, roughness=1, depth=3)
        result = detect_artifacts(terrain_test, threshold=1000)
        print("Expected result: almost no suspicious coordinates are detected.")
        print("Actual result:", result)
    except Exception as e:
        print("Error:", e)

    # Edge Case 3 — negative threshold
    try:
        print("\nEdge Case 3 — negative threshold")
        terrain_test = generate_terrain(9, 9, roughness=1, depth=3)
        result = detect_artifacts(terrain_test, threshold=-1)
        print("Expected result: input should be rejected.")
        print("Actual result:", result)
    except Exception as e:
        print("Expected result: input should be rejected.")
        print("Actual result: Error caught ->", e)


if __name__ == "__main__":
    main()
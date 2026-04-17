import random
from typing import List, Tuple, Dict


Point = Tuple[int, int]
Region = Tuple[int, int, int, int]  # (x, y, width, height)


def split_region(x: int, y: int, width: int, height: int, min_size: int) -> List[Region]:
    """
    Recursively split a rectangular region into 4 quadrants
    until width <= min_size or height <= min_size.

    Returns a list of final leaf regions.
    """
    if width <= 0 or height <= 0:
        raise ValueError("width and height must be positive")
    if min_size <= 0:
        raise ValueError("min_size must be positive")

    if width <= min_size or height <= min_size:
        return [(x, y, width, height)]

    half_w = width // 2
    half_h = height // 2

    # Prevent invalid split when integer division gives 0
    if half_w == 0 or half_h == 0:
        return [(x, y, width, height)]

    regions = []
    regions.extend(split_region(x, y, half_w, half_h, min_size))
    regions.extend(split_region(x + half_w, y, width - half_w, half_h, min_size))
    regions.extend(split_region(x, y + half_h, half_w, height - half_h, min_size))
    regions.extend(split_region(x + half_w, y + half_h, width - half_w, height - half_h, min_size))
    return regions


def count_points_in_region(points: List[Point], region: Region) -> int:
    """
    Count how many points fall inside the region.
    Region uses half-open interval:
    x <= px < x+width, y <= py < y+height
    """
    x, y, width, height = region

    if width <= 0 or height <= 0:
        raise ValueError("region width and height must be positive")

    count = 0
    for px, py in points:
        if x <= px < x + width and y <= py < y + height:
            count += 1
    return count


def find_dense_regions(
    points: List[Point],
    x: int,
    y: int,
    width: int,
    height: int,
    min_size: int,
    density_threshold: float
) -> List[Dict]:
    """
    Recursively split the space and return only leaf regions
    whose density > density_threshold.

    Density = number_of_points / area
    """
    if width <= 0 or height <= 0:
        raise ValueError("width and height must be positive")
    if min_size <= 0:
        raise ValueError("min_size must be positive")
    if density_threshold < 0:
        raise ValueError("density_threshold must be non-negative")

    region = (x, y, width, height)
    point_count = count_points_in_region(points, region)
    area = width * height
    density = point_count / area

    if width <= min_size or height <= min_size:
        if density > density_threshold:
            return [{"region": region, "count": point_count, "density": density}]
        return []

    half_w = width // 2
    half_h = height // 2

    if half_w == 0 or half_h == 0:
        if density > density_threshold:
            return [{"region": region, "count": point_count, "density": density}]
        return []

    results = []
    results.extend(find_dense_regions(points, x, y, half_w, half_h, min_size, density_threshold))
    results.extend(find_dense_regions(points, x + half_w, y, width - half_w, half_h, min_size, density_threshold))
    results.extend(find_dense_regions(points, x, y + half_h, half_w, height - half_h, min_size, density_threshold))
    results.extend(find_dense_regions(points, x + half_w, y + half_h, width - half_w, height - half_h, min_size, density_threshold))
    return results


def generate_random_points(num_points: int, max_x: int, max_y: int) -> List[Point]:
    """Generate random integer points in [0, max_x-1] x [0, max_y-1]."""
    if num_points < 0:
        raise ValueError("num_points must be non-negative")
    if max_x <= 0 or max_y <= 0:
        raise ValueError("max_x and max_y must be positive")

    return [(random.randint(0, max_x - 1), random.randint(0, max_y - 1)) for _ in range(num_points)]


def print_regions(title: str, regions: List):
    print(f"\n{title}")
    if not regions:
        print("  None")
        return
    for item in regions:
        print(" ", item)


def main():
    print("=== Ex1: Divide & Conquer – Spatial Splitting ===")

    # -------------------------------------------------
    # Normal Example
    # -------------------------------------------------
    print("\n--- Normal Example ---")
    points = generate_random_points(100, 100, 100)
    final_regions = split_region(0, 0, 100, 100, 10)
    print(f"Total final regions after splitting: {len(final_regions)}")

    sample_region = (0, 0, 50, 50)
    c = count_points_in_region(points, sample_region)
    print(f"Points inside region {sample_region}: {c}")

    dense_regions = find_dense_regions(points, 0, 0, 100, 100, 10, 0.02)
    print(f"Number of dense regions found: {len(dense_regions)}")
    for item in dense_regions[:10]:
        print(item)

    # -------------------------------------------------
    # Test set for edge cases
    # -------------------------------------------------
    print("\n=== Test set for edge cases ===")

    # 1. split_region(x, y, width, height, min_size)
    print("\n1. split_region(x, y, width, height, min_size)")

    # Edge Case 1 — region already at min_size
    try:
        print("\nEdge Case 1 — width = 10, height = 10, min_size = 10")
        result = split_region(0, 0, 10, 10, 10)
        print("Expected result: only one region is returned.")
        print("Actual result:", result)
    except Exception as e:
        print("Error:", e)

    # Edge Case 2 — width = 0
    try:
        print("\nEdge Case 2 — width = 0")
        result = split_region(0, 0, 0, 10, 5)
        print("Expected result: invalid input should be rejected.")
        print("Actual result:", result)
    except Exception as e:
        print("Expected result: invalid input should be rejected.")
        print("Actual result: Error caught ->", e)

    # Edge Case 3 — negative min_size
    try:
        print("\nEdge Case 3 — min_size = -1")
        result = split_region(0, 0, 20, 20, -1)
        print("Expected result: invalid input should be rejected.")
        print("Actual result:", result)
    except Exception as e:
        print("Expected result: invalid input should be rejected.")
        print("Actual result: Error caught ->", e)

    # 2. count_points_in_region(points, region)
    print("\n2. count_points_in_region(points, region)")

    # Edge Case 1 — empty points list
    try:
        print("\nEdge Case 1 — empty points list")
        result = count_points_in_region([], (0, 0, 10, 10))
        print("Expected result: 0")
        print("Actual result:", result)
    except Exception as e:
        print("Error:", e)

    # Edge Case 2 — all points outside region
    try:
        print("\nEdge Case 2 — all points outside region")
        outside_points = [(20, 20), (30, 30), (40, 40)]
        result = count_points_in_region(outside_points, (0, 0, 10, 10))
        print("Expected result: 0")
        print("Actual result:", result)
    except Exception as e:
        print("Error:", e)

    # Edge Case 3 — invalid region size
    try:
        print("\nEdge Case 3 — invalid region width = -5")
        result = count_points_in_region([(1, 1), (2, 2)], (0, 0, -5, 10))
        print("Expected result: invalid input should be rejected.")
        print("Actual result:", result)
    except Exception as e:
        print("Expected result: invalid input should be rejected.")
        print("Actual result: Error caught ->", e)

    # 3. find_dense_regions(points, min_size, density_threshold)
    print("\n3. find_dense_regions(points, x, y, width, height, min_size, density_threshold)")

    # Edge Case 1 — no points
    try:
        print("\nEdge Case 1 — no points")
        result = find_dense_regions([], 0, 0, 20, 20, 5, 0.01)
        print("Expected result: no dense regions.")
        print("Actual result:", result)
    except Exception as e:
        print("Error:", e)

    # Edge Case 2 — all points clustered in one corner
    try:
        print("\nEdge Case 2 — all points clustered in one corner")
        clustered_points = [(0, 0), (1, 1), (1, 0), (0, 1), (2, 2), (1, 2), (2, 1), (0, 2)]
        result = find_dense_regions(clustered_points, 0, 0, 16, 16, 4, 0.2)
        print("Expected result: dense regions should appear near the top-left corner.")
        print("Actual result:")
        for item in result:
            print(" ", item)
    except Exception as e:
        print("Error:", e)

    # Edge Case 3 — negative density_threshold
    try:
        print("\nEdge Case 3 — density_threshold = -0.5")
        result = find_dense_regions([(1, 1), (2, 2)], 0, 0, 10, 10, 5, -0.5)
        print("Expected result: invalid input should be rejected.")
        print("Actual result:", result)
    except Exception as e:
        print("Expected result: invalid input should be rejected.")
        print("Actual result: Error caught ->", e)


if __name__ == "__main__":
    main()
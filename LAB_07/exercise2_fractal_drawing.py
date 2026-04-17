import math
from typing import List, Tuple


class Canvas:
    """
    Simple canvas that records drawing commands.
    This avoids GUI dependency and is convenient for testing.
    """

    def __init__(self):
        self.commands = []

    def draw_triangle(self, x: float, y: float, size: float) -> None:
        self.commands.append(("triangle", round(x, 4), round(y, 4), round(size, 4)))

    def draw_line(self, x1: float, y1: float, x2: float, y2: float) -> None:
        self.commands.append(
            ("line", round(x1, 4), round(y1, 4), round(x2, 4), round(y2, 4))
        )

    def clear(self) -> None:
        self.commands.clear()

    def count(self) -> int:
        return len(self.commands)

    def preview(self, limit: int = 10) -> None:
        for cmd in self.commands[:limit]:
            print(cmd)
        if len(self.commands) > limit:
            print(f"... ({len(self.commands) - limit} more commands)")


# ---------------------------------------------------
# 1. draw_sierpinski(canvas, x, y, size, depth)
# ---------------------------------------------------
def draw_sierpinski(canvas: Canvas, x: float, y: float, size: float, depth: int) -> None:
    """
    Draw a Sierpinski triangle recursively.

    Base case:
        depth == 0 -> draw one triangle

    Recursive case:
        split into 3 smaller triangles
    """
    if depth < 0:
        raise ValueError("depth must be non-negative")
    if size < 0:
        raise ValueError("size must be non-negative")
    if size == 0:
        return

    if depth == 0:
        canvas.draw_triangle(x, y, size)
    else:
        half = size / 2
        draw_sierpinski(canvas, x, y, half, depth - 1)
        draw_sierpinski(canvas, x + half, y, half, depth - 1)
        draw_sierpinski(canvas, x + half / 2, y - half, half, depth - 1)


# ---------------------------------------------------
# 2. draw_tree(canvas, x, y, length, angle, depth)
# ---------------------------------------------------
def draw_tree(
    canvas: Canvas,
    x: float,
    y: float,
    length: float,
    angle: float,
    depth: int
) -> None:
    """
    Draw a recursive tree.

    Always draws the current branch.
    If depth > 0, recursively draw two smaller branches.
    """
    if depth < 0:
        raise ValueError("depth must be non-negative")
    if length < 0:
        raise ValueError("length must be non-negative")
    if length == 0:
        return

    rad = math.radians(angle)
    x2 = x + length * math.cos(rad)
    y2 = y + length * math.sin(rad)

    canvas.draw_line(x, y, x2, y2)

    if depth > 0:
        new_length = length * 0.7
        draw_tree(canvas, x2, y2, new_length, angle + 30, depth - 1)
        draw_tree(canvas, x2, y2, new_length, angle - 30, depth - 1)


# ---------------------------------------------------
# 3. fractal_dimension(...)
# ---------------------------------------------------
def count_non_empty_boxes(fractal_image: List[List[int]], size: int) -> int:
    """
    Count how many boxes of side length 'size'
    contain at least one non-zero pixel.
    """
    if size <= 0:
        raise ValueError("box size must be positive")
    if not fractal_image or not fractal_image[0]:
        return 0

    rows = len(fractal_image)
    cols = len(fractal_image[0])
    count = 0

    for r in range(0, rows, size):
        for c in range(0, cols, size):
            found = False
            for i in range(r, min(r + size, rows)):
                for j in range(c, min(c + size, cols)):
                    if fractal_image[i][j] != 0:
                        found = True
                        break
                if found:
                    break
            if found:
                count += 1

    return count


def slope_of_best_fit_line(X: List[float], Y: List[float]) -> float:
    """
    Compute slope m of the best-fit line using least squares.
    """
    n = len(X)
    if n != len(Y):
        raise ValueError("X and Y must have the same length")
    if n < 2:
        return 0.0

    sumX = sum(X)
    sumY = sum(Y)
    sumXY = sum(x * y for x, y in zip(X, Y))
    sumX2 = sum(x * x for x in X)

    denominator = n * sumX2 - sumX * sumX
    if denominator == 0:
        return 0.0

    m = (n * sumXY - sumX * sumY) / denominator
    return m


def fractal_dimension(fractal_image: List[List[int]], box_sizes: List[int]) -> float:
    """
    Estimate fractal dimension using box counting.
    """
    if not fractal_image or not fractal_image[0]:
        raise ValueError("fractal_image must not be empty")
    if not box_sizes:
        raise ValueError("box_sizes must not be empty")

    log_sizes = []
    log_counts = []

    for size in box_sizes:
        if size <= 0:
            raise ValueError("all box sizes must be positive")

        count = count_non_empty_boxes(fractal_image, size)
        if count > 0:
            log_sizes.append(math.log(1 / size))
            log_counts.append(math.log(count))

    if len(log_sizes) < 2:
        return 0.0

    dimension = slope_of_best_fit_line(log_sizes, log_counts)
    return dimension


# ---------------------------------------------------
# Helper: build simple binary images for testing
# ---------------------------------------------------
def make_empty_image(rows: int, cols: int) -> List[List[int]]:
    return [[0 for _ in range(cols)] for _ in range(rows)]


def make_line_image(size: int) -> List[List[int]]:
    """
    Create a simple diagonal line in a square binary image.
    """
    image = make_empty_image(size, size)
    for i in range(size):
        image[i][i] = 1
    return image


def make_filled_square_image(size: int) -> List[List[int]]:
    """
    Create a fully filled square binary image.
    """
    return [[1 for _ in range(size)] for _ in range(size)]


# ---------------------------------------------------
# Main: normal tests + edge cases
# ---------------------------------------------------
def main():
    print("=== Ex2 Python Implementation ===")

    # ---------------------------------------------------
    # Normal Example
    # ---------------------------------------------------
    print("\n--- Normal Example: draw_sierpinski ---")
    canvas1 = Canvas()
    draw_sierpinski(canvas1, 0, 0, 100, 3)
    print("Number of triangles drawn:", canvas1.count())
    canvas1.preview(10)

    print("\n--- Normal Example: draw_tree ---")
    canvas2 = Canvas()
    draw_tree(canvas2, 0, 0, 80, 90, 3)
    print("Number of line segments drawn:", canvas2.count())
    canvas2.preview(10)

    print("\n--- Normal Example: fractal_dimension ---")
    line_image = make_line_image(16)
    square_image = make_filled_square_image(16)
    box_sizes = [1, 2, 4, 8]

    line_dim = fractal_dimension(line_image, box_sizes)
    square_dim = fractal_dimension(square_image, box_sizes)

    print("Estimated fractal dimension of line image:", round(line_dim, 4))
    print("Estimated fractal dimension of filled square image:", round(square_dim, 4))

    # ---------------------------------------------------
    # Test set for edge cases
    # ---------------------------------------------------
    print("\n=== Test set for edge cases ===")

    # 1. draw_sierpinski(canvas, x, y, size, depth)
    print("\n1. draw_sierpinski(canvas, x, y, size, depth)")

    # Edge Case 1 — depth = 0
    try:
        print("\nEdge Case 1 — depth = 0")
        c = Canvas()
        draw_sierpinski(c, 0, 0, 100, 0)
        print("Expected result: only one triangle is drawn.")
        print("Actual number of triangles:", c.count())
        c.preview()
    except Exception as e:
        print("Error:", e)

    # Edge Case 2 — size = 0
    try:
        print("\nEdge Case 2 — size = 0")
        c = Canvas()
        draw_sierpinski(c, 0, 0, 0, 3)
        print("Expected result: no visible triangle, or drawing is ignored safely.")
        print("Actual number of triangles:", c.count())
    except Exception as e:
        print("Error:", e)

    # Edge Case 3 — negative depth
    try:
        print("\nEdge Case 3 — negative depth")
        c = Canvas()
        draw_sierpinski(c, 0, 0, 100, -1)
        print("Expected result: invalid input should be rejected.")
    except Exception as e:
        print("Expected result: invalid input should be rejected.")
        print("Actual result: Error caught ->", e)

    # 2. draw_tree(canvas, x, y, length, angle, depth)
    print("\n2. draw_tree(canvas, x, y, length, angle, depth)")

    # Edge Case 1 — depth = 0
    try:
        print("\nEdge Case 1 — depth = 0")
        c = Canvas()
        draw_tree(c, 0, 0, 80, 90, 0)
        print("Expected result: only one line segment is drawn.")
        print("Actual number of line segments:", c.count())
        c.preview()
    except Exception as e:
        print("Error:", e)

    # Edge Case 2 — length = 0
    try:
        print("\nEdge Case 2 — length = 0")
        c = Canvas()
        draw_tree(c, 0, 0, 0, 90, 3)
        print("Expected result: no visible branch.")
        print("Actual number of line segments:", c.count())
    except Exception as e:
        print("Error:", e)

    # Edge Case 3 — negative depth
    try:
        print("\nEdge Case 3 — negative depth")
        c = Canvas()
        draw_tree(c, 0, 0, 80, 90, -1)
        print("Expected result: invalid input should be rejected.")
    except Exception as e:
        print("Expected result: invalid input should be rejected.")
        print("Actual result: Error caught ->", e)

    # 3. fractal_dimension(fractal_image, box_sizes)
    print("\n3. fractal_dimension(fractal_image, box_sizes)")

    # Edge Case 1 — empty image
    try:
        print("\nEdge Case 1 — empty image")
        result = fractal_dimension([], [1, 2, 4, 8])
        print("Expected result: no valid dimension, or empty-box case handled safely.")
        print("Actual result:", result)
    except Exception as e:
        print("Expected result: no valid dimension, or empty-box case handled safely.")
        print("Actual result: Error caught ->", e)

    # Edge Case 2 — invalid box size
    try:
        print("\nEdge Case 2 — invalid box size")
        img = make_line_image(16)
        result = fractal_dimension(img, [0, 2, 4])
        print("Expected result: invalid size should be rejected.")
        print("Actual result:", result)
    except Exception as e:
        print("Expected result: invalid size should be rejected.")
        print("Actual result: Error caught ->", e)

    # Edge Case 3 — only one box size
    try:
        print("\nEdge Case 3 — only one box size")
        img = make_line_image(16)
        result = fractal_dimension(img, [4])
        print("Expected result: dimension estimation is unreliable or undefined.")
        print("Actual result:", result)
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
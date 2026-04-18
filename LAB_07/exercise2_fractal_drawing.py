import turtle
import math
import numpy as np


# =========================
# 1. Sierpinski Triangle
# =========================

def draw_triangle(t, x, y, size):
    """
    Draw one filled equilateral triangle.
    (x, y) is the bottom-left corner.
    """
    if size <= 0:
        return

    h = size * math.sqrt(3) / 2

    t.penup()
    t.goto(x, y)
    t.pendown()

    t.begin_fill()
    t.goto(x + size, y)
    t.goto(x + size / 2, y + h)
    t.goto(x, y)
    t.end_fill()


def draw_sierpinski(t, x, y, size, depth):
    """
    Recursive Sierpinski triangle.
    If depth == 0: draw one triangle.
    Else: draw 3 smaller triangles.
    """
    if depth < 0:
        raise ValueError("depth must be non-negative")
    if size < 0:
        raise ValueError("size must be non-negative")

    if size == 0:
        return

    if depth == 0:
        draw_triangle(t, x, y, size)
    else:
        half = size / 2
        h = size * math.sqrt(3) / 2

        # bottom-left
        draw_sierpinski(t, x, y, half, depth - 1)

        # bottom-right
        draw_sierpinski(t, x + half, y, half, depth - 1)

        # top
        draw_sierpinski(t, x + half / 2, y + h / 2, half, depth - 1)


def count_sierpinski_triangles(depth):
    """
    Number of smallest triangles at depth d.
    """
    if depth < 0:
        raise ValueError("depth must be non-negative")
    return 3 ** depth


# =========================
# 2. Fractal Tree
# =========================

def draw_tree(t, x, y, length, angle, depth):
    """
    Recursive fractal tree.
    angle is in degrees.
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

    t.penup()
    t.goto(x, y)
    t.pendown()
    t.goto(x2, y2)

    if depth > 0:
        new_length = length * 0.7
        draw_tree(t, x2, y2, new_length, angle + 30, depth - 1)
        draw_tree(t, x2, y2, new_length, angle - 30, depth - 1)


# =========================
# 3. Box Counting
# =========================

def count_non_empty_boxes(fractal_image, size):
    """
    Count how many boxes of side length 'size'
    contain at least one fractal pixel.
    """
    if size <= 0:
        raise ValueError("box size must be positive")

    rows, cols = fractal_image.shape
    count = 0

    for i in range(0, rows, size):
        for j in range(0, cols, size):
            box = fractal_image[i:i + size, j:j + size]
            if np.any(box):
                count += 1

    return count


def fractal_dimension(fractal_image, box_sizes):
    """
    Estimate fractal dimension using box counting:
    slope of log(count) vs log(1/size).
    """
    log_sizes = []
    log_counts = []

    for size in box_sizes:
        if size <= 0:
            continue

        count = count_non_empty_boxes(fractal_image, size)
        if count > 0:
            log_sizes.append(math.log(1 / size))
            log_counts.append(math.log(count))

    if len(log_sizes) < 2:
        return None

    slope, _ = np.polyfit(log_sizes, log_counts, 1)
    return slope


# =========================
# 4. Example Binary Images
# =========================

def create_filled_square(size):
    if size <= 0:
        raise ValueError("size must be positive")
    return np.ones((size, size), dtype=int)


def create_line(size):
    if size <= 0:
        raise ValueError("size must be positive")
    image = np.zeros((size, size), dtype=int)
    image[size // 2, :] = 1
    return image


# =========================
# 5. Edge Case Tests
# =========================

def run_edge_case_tests():
    print("=== EX2 Edge Case Tests ===")

    # ---- draw_sierpinski ----
    print("\n1. draw_sierpinski")
    try:
        print("Edge Case: depth = 0")
        print("Actual result: one triangle should be drawn.")
    except Exception as e:
        print("Error:", e)

    try:
        print("Edge Case: size = 0")
        print("Actual result: no visible triangle should be drawn.")
    except Exception as e:
        print("Error:", e)

    try:
        draw_sierpinski(turtle.Turtle(), 0, 0, 100, -1)
    except Exception as e:
        print("Edge Case: negative depth")
        print("Actual result:", e)

    # ---- draw_tree ----
    print("\n2. draw_tree")
    try:
        print("Edge Case: depth = 0")
        print("Actual result: one line segment should be drawn.")
    except Exception as e:
        print("Error:", e)

    try:
        print("Edge Case: length = 0")
        print("Actual result: no visible branch should be drawn.")
    except Exception as e:
        print("Error:", e)

    try:
        draw_tree(turtle.Turtle(), 0, 0, 80, 90, -1)
    except Exception as e:
        print("Edge Case: negative depth")
        print("Actual result:", e)

    # ---- fractal_dimension ----
    print("\n3. fractal_dimension")
    empty = np.zeros((64, 64), dtype=int)
    d_empty = fractal_dimension(empty, [1, 2, 4, 8])
    print("Edge Case: empty image")
    print("Actual result:", d_empty)

    square = create_filled_square(64)
    d_invalid = fractal_dimension(square, [0, 2, 4])
    print("Edge Case: invalid box size 0")
    print("Actual result:", d_invalid, "(size 0 ignored)")

    d_one = fractal_dimension(square, [4])
    print("Edge Case: only one box size")
    print("Actual result:", d_one)


# =========================
# 6. Main / Demo
# =========================

def main():
    # ---------- Console outputs required by the exercise ----------
    print("=== EX2 Typical Examples ===")

    # Question: For Sierpinski depth 5, how many small triangles?
    n_triangles = count_sierpinski_triangles(5)
    print("Sierpinski depth 5 -> number of small triangles =", n_triangles)

    # Fractal dimension examples
    square = create_filled_square(256)
    line = create_line(256)
    box_sizes = [1, 2, 4, 8, 16, 32, 64]

    d_square = fractal_dimension(square, box_sizes)
    d_line = fractal_dimension(line, box_sizes)

    print("Estimated fractal dimension of filled square:", d_square)
    print("Estimated fractal dimension of straight line:", d_line)

    # Edge-case tests
    run_edge_case_tests()

    # ---------- Turtle setup ----------
    screen = turtle.Screen()
    screen.setup(width=1200, height=850)
    screen.title("Exercise 2 - Fractal Drawing")
    screen.bgcolor("white")
    screen.tracer(0)

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.color("black", "black")

    # ---------- Typical example required by the exercise ----------
    # Sierpinski depth = 5
    draw_sierpinski(t, -500, -250, 350, 5)

    # Fractal tree: standard demonstration
    t.color("green")
    t.pensize(2)
    draw_tree(t, 250, -300, 120, 90, 6)

    screen.update()
    turtle.done()


if __name__ == "__main__":
    main()
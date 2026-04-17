import turtle
import math
import numpy as np


# =========================
# 1. Sierpinski Triangle
# =========================

def draw_triangle(t, x, y, size):
    """
    Draw a filled equilateral triangle.
    (x, y) is the bottom-left corner.
    """
    h = size * math.sqrt(3) / 2

    t.up()
    t.goto(x, y)
    t.down()

    t.begin_fill()
    t.goto(x + size, y)
    t.goto(x + size / 2, y + h)
    t.goto(x, y)
    t.end_fill()


def draw_sierpinski(t, x, y, size, depth):
    """
    Recursive Sierpinski triangle.
    """
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


# =========================
# 2. Fractal Tree
# =========================

def draw_tree(t, x, y, length, angle, depth):
    """
    Recursive fractal tree.
    angle is in degrees.
    """
    rad = math.radians(angle)
    x2 = x + length * math.cos(rad)
    y2 = y + length * math.sin(rad)

    t.up()
    t.goto(x, y)
    t.down()
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

    fractal_image should be a 2D NumPy array
    with values 0/1.
    """
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
    Estimate the fractal dimension using box counting:
    plot log(count) vs log(1/size), slope = dimension
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

    slope, intercept = np.polyfit(log_sizes, log_counts, 1)
    return slope


# =========================
# 4. Example Binary Images
# =========================

def create_filled_square(size):
    """
    Create a binary image of a filled square.
    Expected fractal dimension մոտ 2.
    """
    return np.ones((size, size), dtype=int)


def create_line(size):
    """
    Create a binary image of a horizontal line.
    Expected fractal dimension մոտ 1.
    """
    image = np.zeros((size, size), dtype=int)
    image[size // 2, :] = 1
    return image


# =========================
# 5. Main / Demo
# =========================

def main():
    # ---------- Turtle setup ----------
    screen = turtle.Screen()
    screen.setup(width=1000, height=800)
    screen.title("Exercise 2 - Fractal Drawing")

    t = turtle.Turtle()
    t.speed(0)
    t.color("black", "black")

    # ---------- Draw Sierpinski Triangle ----------
    draw_sierpinski(t, -300, -250, 300, 4)

    # ---------- Draw Fractal Tree ----------
    t.color("green")
    draw_tree(t, 250, -300, 100, 90, 6)

    screen.update()

    # ---------- Box-counting tests ----------
    square = create_filled_square(256)
    line = create_line(256)
    box_sizes = [1, 2, 4, 8, 16, 32, 64]

    d_square = fractal_dimension(square, box_sizes)
    d_line = fractal_dimension(line, box_sizes)

    print("Estimated fractal dimension of filled square:", d_square)
    print("Estimated fractal dimension of straight line:", d_line)

    # Keep the turtle window open
    turtle.done()


if __name__ == "__main__":
    main()
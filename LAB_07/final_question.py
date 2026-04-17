import random
import math
import turtle
from typing import List, Tuple


Point = Tuple[int, int]
Region = Tuple[int, int, int, int]


# =========================================================
# Turtle drawing helpers
# =========================================================
def setup_screen(width: int = 900, height: int = 900, title: str = "Recursive Pattern Generator"):
    screen = turtle.Screen()
    screen.setup(width, height)
    screen.title(title)
    screen.bgcolor("white")
    screen.tracer(0, 0)
    return screen


def create_pen():
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.pensize(1)
    return pen


def draw_text(pen, x: float, y: float, text: str, align: str = "left", font=("Arial", 12, "normal")):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.write(text, align=align, font=font)


def draw_rectangle(pen, x: float, y: float, width: float, height: float):
    """
    Draw rectangle from top-left corner (x, y)
    in turtle coordinate system.
    """
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.goto(x + width, y)
    pen.goto(x + width, y - height)
    pen.goto(x, y - height)
    pen.goto(x, y)


def draw_filled_cell(pen, x: float, y: float, size: float):
    """
    Draw a filled square cell from top-left corner (x, y)
    """
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.begin_fill()
    pen.goto(x + size, y)
    pen.goto(x + size, y - size)
    pen.goto(x, y - size)
    pen.goto(x, y)
    pen.end_fill()


# =========================================================
# Ex1: spatial splitting
# =========================================================
def split_region(x: int, y: int, width: int, height: int, min_size: int) -> List[Region]:
    if width <= 0 or height <= 0:
        raise ValueError("width and height must be positive")
    if min_size <= 0:
        raise ValueError("min_size must be positive")

    if width <= min_size or height <= min_size:
        return [(x, y, width, height)]

    half_w = width // 2
    half_h = height // 2

    if half_w == 0 or half_h == 0:
        return [(x, y, width, height)]

    regions = []
    regions.extend(split_region(x, y, half_w, half_h, min_size))
    regions.extend(split_region(x + half_w, y, width - half_w, half_h, min_size))
    regions.extend(split_region(x, y + half_h, half_w, height - half_h, min_size))
    regions.extend(split_region(x + half_w, y + half_h, width - half_w, height - half_h, min_size))
    return regions


def draw_split_view_turtle(pen, origin_x: float, origin_y: float, width: int, height: int, min_size: int):
    regions = split_region(0, 0, width, height, min_size)
    pen.color("black")
    for rx, ry, rw, rh in regions:
        draw_rectangle(pen, origin_x + rx, origin_y - ry, rw, rh)
    return regions


# =========================================================
# Ex2: fractal dimension
# =========================================================
def count_non_empty_boxes(binary_image: List[List[int]], size: int) -> int:
    if size <= 0:
        raise ValueError("box size must be positive")

    rows = len(binary_image)
    cols = len(binary_image[0])
    count = 0

    for r in range(0, rows, size):
        for c in range(0, cols, size):
            found = False
            for i in range(r, min(r + size, rows)):
                for j in range(c, min(c + size, cols)):
                    if binary_image[i][j] != 0:
                        found = True
                        break
                if found:
                    break
            if found:
                count += 1

    return count


def slope_of_best_fit_line(X: List[float], Y: List[float]) -> float:
    n = len(X)
    if n < 2:
        return 0.0

    sumX = sum(X)
    sumY = sum(Y)
    sumXY = sum(x * y for x, y in zip(X, Y))
    sumX2 = sum(x * x for x in X)

    denominator = n * sumX2 - sumX * sumX
    if denominator == 0:
        return 0.0

    return (n * sumXY - sumX * sumY) / denominator


def fractal_dimension(binary_image: List[List[int]], box_sizes: List[int]) -> float:
    if not binary_image or not binary_image[0]:
        raise ValueError("binary_image must not be empty")
    if not box_sizes:
        raise ValueError("box_sizes must not be empty")

    log_sizes = []
    log_counts = []

    for size in box_sizes:
        if size <= 0:
            raise ValueError("box size must be positive")
        count = count_non_empty_boxes(binary_image, size)
        if count > 0:
            log_sizes.append(math.log(1 / size))
            log_counts.append(math.log(count))

    if len(log_sizes) < 2:
        return 0.0

    return slope_of_best_fit_line(log_sizes, log_counts)


def generate_box_sizes(size: int) -> List[int]:
    box_sizes = []
    current = size
    while current >= 1:
        box_sizes.append(current)
        current //= 2
    return box_sizes


# =========================================================
# Ex3: terrain generation + artifact detection
# =========================================================
def diamond_square(
    terrain: List[List[float]],
    x1: int,
    y1: int,
    x2: int,
    y2: int,
    roughness: float,
    depth: int
) -> None:
    if depth == 0:
        return

    if x2 - x1 < 2 or y2 - y1 < 2:
        return

    xm = (x1 + x2) // 2
    ym = (y1 + y2) // 2

    center = (
        terrain[x1][y1] +
        terrain[x1][y2] +
        terrain[x2][y1] +
        terrain[x2][y2]
    ) / 4.0
    terrain[xm][ym] = center + roughness * random.uniform(-1, 1)

    terrain[x1][ym] = (terrain[x1][y1] + terrain[x1][y2]) / 2.0 + roughness * random.uniform(-1, 1)
    terrain[x2][ym] = (terrain[x2][y1] + terrain[x2][y2]) / 2.0 + roughness * random.uniform(-1, 1)
    terrain[xm][y1] = (terrain[x1][y1] + terrain[x2][y1]) / 2.0 + roughness * random.uniform(-1, 1)
    terrain[xm][y2] = (terrain[x1][y2] + terrain[x2][y2]) / 2.0 + roughness * random.uniform(-1, 1)

    diamond_square(terrain, x1, y1, xm, ym, roughness / 2, depth - 1)
    diamond_square(terrain, xm, y1, x2, ym, roughness / 2, depth - 1)
    diamond_square(terrain, x1, ym, xm, y2, roughness / 2, depth - 1)
    diamond_square(terrain, xm, ym, x2, y2, roughness / 2, depth - 1)


def generate_terrain(width: int, height: int, roughness: float, depth: int) -> List[List[float]]:
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


def detect_artifacts(terrain_grid: List[List[float]], threshold: float) -> List[Tuple[int, int]]:
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


def normalize_terrain_to_binary(terrain: List[List[float]]) -> List[List[int]]:
    """
    Convert terrain to a binary image for box-counting.
    Cells above average -> 1, else 0
    """
    rows = len(terrain)
    cols = len(terrain[0])
    values = [terrain[i][j] for i in range(rows) for j in range(cols)]
    avg = sum(values) / len(values)

    binary = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(1 if terrain[i][j] > avg else 0)
        binary.append(row)
    return binary


def draw_terrain_turtle(
    pen,
    terrain: List[List[float]],
    origin_x: float,
    origin_y: float,
    cell_size: float
):
    rows = len(terrain)
    cols = len(terrain[0])

    values = [terrain[i][j] for i in range(rows) for j in range(cols)]
    min_v = min(values)
    max_v = max(values)

    for i in range(rows):
        for j in range(cols):
            value = terrain[i][j]
            if max_v == min_v:
                gray = 0.5
            else:
                gray = (value - min_v) / (max_v - min_v)

            pen.color(gray, gray, gray)
            pen.fillcolor(gray, gray, gray)
            x = origin_x + j * cell_size
            y = origin_y - i * cell_size
            draw_filled_cell(pen, x, y, cell_size)

    pen.color("black")
    draw_rectangle(pen, origin_x, origin_y, cols * cell_size, rows * cell_size)


def draw_artifacts_turtle(
    pen,
    artifacts: List[Tuple[int, int]],
    origin_x: float,
    origin_y: float,
    cell_size: float
):
    pen.color("red")
    pen.fillcolor("red")
    for i, j in artifacts:
        x = origin_x + j * cell_size
        y = origin_y - i * cell_size
        draw_filled_cell(pen, x, y, cell_size)


# =========================================================
# Final integration
# =========================================================
def recursive_pattern_generator_simple_scenario():
    random.seed(42)

    # Screen and pens
    screen = setup_screen()
    turtle.colormode(1.0)

    terrain_pen = create_pen()
    split_pen = create_pen()
    artifact_pen = create_pen()
    text_pen = create_pen()

    # Parameters
    grid_size = 33          # use 2^n + 1 style size for terrain
    roughness = 2.0
    depth = 5
    min_size = 4
    artifact_threshold = 0.4

    # Layout
    terrain_origin_x = -380
    terrain_origin_y = 300
    cell_size = 12

    terrain_pixel_width = grid_size * cell_size
    terrain_pixel_height = grid_size * cell_size

    # -----------------------------------------------------
    # 1. User clicks "Generate Terrain" -> creates a landscape
    # -----------------------------------------------------
    terrain = generate_terrain(grid_size, grid_size, roughness, depth)
    draw_terrain_turtle(terrain_pen, terrain, terrain_origin_x, terrain_origin_y, cell_size)

    draw_text(text_pen, -380, 340, 'Step 1: "Generate Terrain" -> creates a landscape',
              font=("Arial", 12, "bold"))

    # -----------------------------------------------------
    # 2. System measures fractal dimension -> shows D = ...
    # -----------------------------------------------------
    binary_image = normalize_terrain_to_binary(terrain)
    box_sizes = generate_box_sizes(grid_size)
    D = fractal_dimension(binary_image, box_sizes)

    draw_text(text_pen, -380, -130,
              f'Step 2: Measure fractal dimension -> D = {D:.3f}',
              font=("Arial", 12, "bold"))

    # -----------------------------------------------------
    # 3. If D is too low (<1.8) or too high (>2.5), show warning
    # -----------------------------------------------------
    if D < 1.8 or D > 2.5:
        draw_text(text_pen, -380, -160,
                  "Step 3: Warning -> D is outside the normal range",
                  font=("Arial", 12, "bold"))
    else:
        draw_text(text_pen, -380, -160,
                  "Step 3: D is in a reasonable range",
                  font=("Arial", 12, "bold"))

    # -----------------------------------------------------
    # 4. User clicks "Split View" -> sees quadtree regions overlaid
    # -----------------------------------------------------
    draw_split_view_turtle(
        split_pen,
        terrain_origin_x,
        terrain_origin_y,
        terrain_pixel_width,
        terrain_pixel_height,
        min_size * cell_size
    )

    draw_text(text_pen, 80, 340,
              'Step 4: "Split View" -> quadtree regions overlaid',
              font=("Arial", 12, "bold"))

    # -----------------------------------------------------
    # 5. User clicks "Find Artifacts" -> highlights unnatural straight lines
    # -----------------------------------------------------
    artifacts = detect_artifacts(terrain, artifact_threshold)
    draw_artifacts_turtle(artifact_pen, artifacts, terrain_origin_x, terrain_origin_y, cell_size)

    draw_text(text_pen, 80, 310,
              f'Step 5: "Find Artifacts" -> {len(artifacts)} suspicious cells',
              font=("Arial", 12, "bold"))

    screen.update()
    turtle.done()


# =========================================================
# main
# =========================================================
def main():
    recursive_pattern_generator_simple_scenario()


if __name__ == "__main__":
    main()
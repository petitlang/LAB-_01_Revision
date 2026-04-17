import turtle
import random
import numpy as np


# =========================
# 1. Midpoint Displacement
# =========================

def midpoint_displacement(x1, y1, x2, y2, roughness, depth):
    if depth == 0:
        return [(x1, y1), (x2, y2)]

    xm = (x1 + x2) / 2
    ym = (y1 + y2) / 2 + roughness * random.uniform(-1, 1)

    left_points = midpoint_displacement(x1, y1, xm, ym, roughness * 0.7, depth - 1)
    right_points = midpoint_displacement(xm, ym, x2, y2, roughness * 0.7, depth - 1)

    return left_points[:-1] + right_points


def draw_polyline(t, points):
    if not points:
        return

    t.penup()
    t.goto(points[0])
    t.pendown()

    for p in points[1:]:
        t.goto(p)


# =========================
# 2. Diamond-Square Terrain
# =========================

def diamond_square(terrain, x1, y1, x2, y2, roughness, depth):
    if depth == 0:
        return

    if x2 - x1 < 2 or y2 - y1 < 2:
        return

    xm = (x1 + x2) // 2
    ym = (y1 + y2) // 2

    a = terrain[x1, y1]
    b = terrain[x1, y2]
    c = terrain[x2, y1]
    d = terrain[x2, y2]

    center = (a + b + c + d) / 4
    terrain[xm, ym] = center + roughness * random.uniform(-1, 1)

    if terrain[x1, ym] == 0:
        terrain[x1, ym] = (a + b) / 2 + roughness * random.uniform(-1, 1)
    if terrain[x2, ym] == 0:
        terrain[x2, ym] = (c + d) / 2 + roughness * random.uniform(-1, 1)
    if terrain[xm, y1] == 0:
        terrain[xm, y1] = (a + c) / 2 + roughness * random.uniform(-1, 1)
    if terrain[xm, y2] == 0:
        terrain[xm, y2] = (b + d) / 2 + roughness * random.uniform(-1, 1)

    new_roughness = roughness / 2

    diamond_square(terrain, x1, y1, xm, ym, new_roughness, depth - 1)
    diamond_square(terrain, xm, y1, x2, ym, new_roughness, depth - 1)
    diamond_square(terrain, x1, ym, xm, y2, new_roughness, depth - 1)
    diamond_square(terrain, xm, ym, x2, y2, new_roughness, depth - 1)


def generate_terrain(width, height, roughness, depth):
    terrain = np.zeros((width, height), dtype=float)

    terrain[0, 0] = 0
    terrain[0, height - 1] = 0
    terrain[width - 1, 0] = 0
    terrain[width - 1, height - 1] = 0

    diamond_square(terrain, 0, 0, width - 1, height - 1, roughness, depth)
    return terrain


# =========================
# 3. Artifact Detection
# =========================

def detect_artifacts(terrain_grid, threshold):
    artifacts = []
    rows, cols = terrain_grid.shape

    for i in range(rows - 1):
        for j in range(cols - 1):
            if (abs(terrain_grid[i, j] - terrain_grid[i + 1, j]) > threshold or
                abs(terrain_grid[i, j] - terrain_grid[i, j + 1]) > threshold):
                artifacts.append((i, j))

    return artifacts


# =========================
# 4. Better Color Mapping
# =========================

def height_to_color(h, min_h, max_h):
    if max_h == min_h:
        return "gray"

    ratio = (h - min_h) / (max_h - min_h)

    if ratio < 0.2:
        return "#1f4e79"   # dark blue
    elif ratio < 0.4:
        return "#4f81bd"   # blue
    elif ratio < 0.6:
        return "#6aa84f"   # green
    elif ratio < 0.8:
        return "#8b5a2b"   # brown
    else:
        return "#f3f3f3"   # light / snow


def draw_filled_square(t, x, y, size, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.pencolor(color)   # remove black grid effect
    t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.left(90)
    t.end_fill()


def draw_terrain(t, terrain, start_x, start_y, cell_size):
    rows, cols = terrain.shape
    min_h = np.min(terrain)
    max_h = np.max(terrain)

    for i in range(rows):
        for j in range(cols):
            color = height_to_color(terrain[i, j], min_h, max_h)
            x = start_x + j * cell_size
            y = start_y + i * cell_size
            draw_filled_square(t, x, y, cell_size, color)


def draw_artifacts(t, artifacts, start_x, start_y, cell_size):
    t.penup()
    t.color("red")

    for (i, j) in artifacts:
        x = start_x + j * cell_size + cell_size / 2
        y = start_y + i * cell_size + cell_size / 2
        t.goto(x, y)
        t.dot(max(3, cell_size * 0.4))


# =========================
# 5. Main
# =========================

def main():
    screen = turtle.Screen()
    screen.setup(width=1400, height=850)
    screen.bgcolor("white")
    screen.title("Exercise 3 - Recursive Patterns")

    screen.tracer(0)

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.pensize(2)

    # ----- midpoint displacement -----
    t.color("black")
    points = midpoint_displacement(-600, 250, -150, 250, roughness=25, depth=9)
    draw_polyline(t, points)

    # ----- terrain -----
    terrain = generate_terrain(33, 33, roughness=12, depth=5)
    draw_terrain(t, terrain, start_x=100, start_y=-260, cell_size=10)

    # ----- artifacts -----
    artifacts = detect_artifacts(terrain, threshold=15)
    draw_artifacts(t, artifacts, start_x=100, start_y=-260, cell_size=10)

    screen.update()
    turtle.done()


if __name__ == "__main__":
    main()
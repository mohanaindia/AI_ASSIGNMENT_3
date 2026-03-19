import random


def create_grid(rows, cols):
    return [[0 for _ in range(cols)] for _ in range(rows)]


def add_obstacles(grid, obstacle_probability, start, goal):
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if (i, j) != start and (i, j) != goal:
                if random.random() < obstacle_probability:
                    grid[i][j] = 1  # obstacle

    return grid


def generate_battlefield(rows, cols, density_level, start, goal):
    density_map = {
        "low": 0.10,
        "medium": 0.20,
        "high": 0.30
    }

    if density_level not in density_map:
        raise ValueError("Invalid density level. Choose low, medium, or high.")

    grid = create_grid(rows, cols)
    grid = add_obstacles(grid, density_map[density_level], start, goal)
    return grid
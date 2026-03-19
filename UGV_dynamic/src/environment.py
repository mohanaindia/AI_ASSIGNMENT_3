import random
from collections import deque


def create_empty_grid(rows, cols):
    return [[0 for _ in range(cols)] for _ in range(rows)]


def add_initial_obstacles(grid, probability, start, goal):
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            cell = (i, j)
            if cell == start or cell == goal:
                continue
            if random.random() < probability:
                grid[i][j] = 1

    return grid


def neighbors(cell, rows, cols):
    r, c = cell
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    result = []

    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            result.append((nr, nc))

    return result


def path_exists(grid, start, goal):
    rows = len(grid)
    cols = len(grid[0])

    if grid[start[0]][start[1]] == 1 or grid[goal[0]][goal[1]] == 1:
        return False

    queue = deque([start])
    visited = {start}

    while queue:
        current = queue.popleft()
        if current == goal:
            return True

        for nxt in neighbors(current, rows, cols):
            if nxt not in visited and grid[nxt[0]][nxt[1]] == 0:
                visited.add(nxt)
                queue.append(nxt)

    return False


def generate_environment(rows, cols, initial_obstacle_probability, start, goal, max_attempts=100):
    for _ in range(max_attempts):
        grid = create_empty_grid(rows, cols)
        grid = add_initial_obstacles(grid, initial_obstacle_probability, start, goal)

        if path_exists(grid, start, goal):
            return grid

    return None


def insert_dynamic_obstacle(grid, start, goal, current, remaining_path=None):
    rows = len(grid)
    cols = len(grid[0])

    reserved = {start, goal, current}

    if remaining_path is None:
        remaining_path = []

    path_candidates = [
        cell for cell in remaining_path
        if cell not in reserved and grid[cell[0]][cell[1]] == 0
    ]

    if path_candidates:
        obstacle = random.choice(path_candidates)
        grid[obstacle[0]][obstacle[1]] = 1
        return obstacle, True

    free_cells = []
    for i in range(rows):
        for j in range(cols):
            cell = (i, j)
            if cell not in reserved and grid[i][j] == 0:
                free_cells.append(cell)

    if free_cells:
        obstacle = random.choice(free_cells)
        grid[obstacle[0]][obstacle[1]] = 1
        return obstacle, False

    return None, False
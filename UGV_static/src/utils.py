def reconstruct_path(came_from, start, goal):
    path = []

    if came_from is None:
        return path

    current = goal
    path.append(current)

    while current != start:
        current = came_from[current]
        path.append(current)

    path.reverse()
    return path


def print_grid(grid, start, goal, path=None):
    path_set = set(path) if path else set()

    for i in range(len(grid)):
        row_display = ""
        for j in range(len(grid[0])):
            cell = (i, j)

            if cell == start:
                row_display += "S "
            elif cell == goal:
                row_display += "G "
            elif cell in path_set:
                row_display += "* "
            elif grid[i][j] == 1:
                row_display += "# "
            else:
                row_display += ". "

        print(row_display)


def print_measures(path, explored_nodes):
    if path:
        print("\nMeasures of Effectiveness:")
        print(f"Path Length: {len(path) - 1}")
        print(f"Nodes Explored: {explored_nodes}")
        print("Mission Status: Success")
    else:
        print("\nMeasures of Effectiveness:")
        print("Path Length: Not Available")
        print(f"Nodes Explored: {explored_nodes}")
        print("Mission Status: Failed")
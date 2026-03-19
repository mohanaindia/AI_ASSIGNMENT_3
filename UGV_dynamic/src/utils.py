def print_grid(grid, start, goal, current=None, path=None):
    path_set = set(path) if path else set()

    for i in range(len(grid)):
        row_display = ""
        for j in range(len(grid[0])):
            cell = (i, j)

            if cell == start:
                row_display += "S "
            elif cell == goal:
                row_display += "G "
            elif current is not None and cell == current:
                row_display += "U "
            elif cell in path_set:
                row_display += "* "
            elif grid[i][j] == 1:
                row_display += "# "
            else:
                row_display += ". "

        print(row_display)


def print_mission_summary(total_steps, total_repairs, total_obstacle_updates, mission_status, total_cost, total_nodes_processed):
    print("\nMission Summary:")
    print(f"Total Steps: {total_steps}")
    print(f"Total Repairs: {total_repairs}")
    print(f"Total Obstacle Updates: {total_obstacle_updates}")
    print(f"Mission Status: {mission_status}")
    print(f"Total Cost: {total_cost}")
    print(f"Total Nodes Processed: {total_nodes_processed}")
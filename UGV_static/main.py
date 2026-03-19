from src.grid import generate_battlefield
from src.astar import astar
from src.utils import reconstruct_path, print_grid, print_measures


def main():
    rows = 20
    cols = 20

    start = (0, 0)
    goal = (rows - 1, cols - 1)

    print("UGV Static Obstacle Path Planning using A*")
    print("Obstacle Density Levels: low, medium, high")

    density = input("Enter obstacle density level: ").strip().lower()

    try:
        grid = generate_battlefield(rows, cols, density, start, goal)
    except ValueError as error:
        print(error)
        return

    came_from, cost, explored_nodes = astar(grid, start, goal)

    if came_from is not None:
        path = reconstruct_path(came_from, start, goal)
        print("\nPath found successfully.\n")
        print_grid(grid, start, goal, path)
        print_measures(path, explored_nodes)
        print(f"Total Cost: {cost}")
    else:
        print("\nNo path found.\n")
        print_grid(grid, start, goal)
        print_measures(None, explored_nodes)


if __name__ == "__main__":
    main()
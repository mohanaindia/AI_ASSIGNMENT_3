import random

from src.dstar_lite import DStarLite
from src.environment import generate_environment, insert_dynamic_obstacle
from src.utils import print_grid, print_mission_summary


def get_int_input(prompt, default):
    value = input(f"{prompt} [default: {default}]: ").strip()
    if value == "":
        return default
    return int(value)


def get_float_input(prompt, default):
    value = input(f"{prompt} [default: {default}]: ").strip()
    if value == "":
        return default
    return float(value)


def main():
    random.seed(42)

    print("UGV Dynamic Obstacle Navigation using D* Lite")
    print("Press Enter to use the default value.\n")

    rows = get_int_input("Enter number of rows", 10)
    cols = get_int_input("Enter number of columns", 10)

    start = (0, 0)
    goal = (rows - 1, cols - 1)

    initial_obstacle_probability = get_float_input("Enter initial obstacle probability", 0.08)
    dynamic_obstacle_probability = get_float_input("Enter dynamic obstacle probability", 0.15)

    grid = generate_environment(
        rows=rows,
        cols=cols,
        initial_obstacle_probability=initial_obstacle_probability,
        start=start,
        goal=goal
    )

    if grid is None:
        print("Could not generate a valid initial environment.")
        return

    planner = DStarLite(grid, start, goal)
    planner.compute_shortest_path()

    current = start
    total_steps = 0
    total_repairs = 0
    total_obstacle_updates = 0
    total_cost = 0
    mission_status = "Failed"

    print("\nInitial environment:\n")
    current_path = planner.extract_path()
    print_grid(grid, start, goal, current=current, path=current_path)

    while current != goal:
        planner.compute_shortest_path()
        current_path = planner.extract_path()

        if not current_path:
            print("\nNo valid path available from current position to goal.")
            print_grid(grid, start, goal, current=current)
            break

        print("\nCurrent planned path:\n")
        print_grid(grid, start, goal, current=current, path=current_path)

        next_step = planner.get_best_next_step()
        if next_step is None:
            print("\nNo feasible next step found.")
            break

        current = next_step
        planner.update_start(current)
        total_steps += 1
        total_cost += 1

        if current == goal:
            mission_status = "Success"
            print("\nGoal reached.")
            break

        if random.random() < dynamic_obstacle_probability:
            obstacle, blocks_path = insert_dynamic_obstacle(
                grid=grid,
                start=start,
                goal=goal,
                current=current,
                remaining_path=current_path[2:]
            )

            if obstacle is not None:
                total_obstacle_updates += 1
                print(f"\nNew obstacle detected at {obstacle}.")

                planner.add_obstacle(obstacle)
                planner.compute_shortest_path()

                if blocks_path:
                    total_repairs += 1
                    print("Planned route affected. Repairing path with D* Lite...")
                else:
                    print("Map updated. D* Lite adjusted internal costs.")

    print_mission_summary(
        total_steps=total_steps,
        total_repairs=total_repairs,
        total_obstacle_updates=total_obstacle_updates,
        mission_status=mission_status,
        total_cost=total_cost,
        total_nodes_processed=planner.total_nodes_processed
    )


if __name__ == "__main__":
    main()
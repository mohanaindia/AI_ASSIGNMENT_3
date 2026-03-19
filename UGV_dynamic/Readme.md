# Question 3: UGV Navigation in a Dynamic Obstacle Environment Using D* Lite

## Description
This project simulates an Unmanned Ground Vehicle (UGV) navigating a dynamic battlefield represented as a 2D grid. The UGV starts at the top-left corner of the grid and must reach the goal at the bottom-right corner while avoiding obstacles. Unlike a static environment, this battlefield can change while the vehicle is moving, because new obstacles may appear during execution. As a result, a path that was valid earlier may suddenly become blocked. To handle this, the project uses **D* Lite**, a dynamic path-planning algorithm designed to repair paths efficiently when the map changes instead of recomputing everything from scratch.

The program first generates a valid initial environment, computes an initial path, and then simulates movement step by step. While the UGV moves, new obstacles may appear. When this happens, D* Lite updates the affected nodes, repairs the path, and allows the UGV to continue if a valid route still exists. This makes the project a practical demonstration of dynamic replanning in autonomous navigation.

## Project Structure
```text
q3_dynamic_ugv/
├── src/
│   ├── __init__.py
│   ├── dstar_lite.py
│   ├── environment.py
│   └── utils.py
├── main.py
├── README.md
└── requirements.txt
```

## How the Algorithm Works
D* Lite is an incremental heuristic search algorithm used for shortest path planning in environments that may change over time. It is closely related to A*, but instead of solving the entire problem from scratch whenever the map changes, it repairs only the affected parts of the search. This makes it well suited for robotics and autonomous systems where the agent discovers new obstacles during execution.

The algorithm maintains two values for each node:
- **g(n)**: the current best-known cost from the node to the goal
- **rhs(n)**: a one-step lookahead value used to detect whether a node is consistent

A node is:
- **consistent** if `g(n) = rhs(n)`
- **inconsistent** if `g(n) != rhs(n)`

The goal node is initialized with `rhs(goal) = 0`, and a priority queue is used to process nodes in order of importance. D* Lite works backward from the goal and updates path costs until the start node becomes consistent. The UGV then follows the best available path. If a new obstacle appears, only the affected cells are updated, the priority queue is adjusted, and the path is repaired from the UGV’s current position. This is why D* Lite is more efficient than repeatedly running A* from scratch in a dynamic environment.

## How to Run
Open a terminal inside the project folder and run:

```bash
python main.py
```

If your system uses Python 3 explicitly, run:

```bash
python3 main.py
```

On some Windows systems, you may also use:

```bash
py main.py
```

When the program starts, it will ask for:
- number of rows
- number of columns
- initial obstacle probability
- dynamic obstacle probability

You can enter your own values or just press **Enter** to use the defaults.

## Output Symbols
- `S` = Start
- `G` = Goal
- `U` = Current UGV position
- `#` = Obstacle
- `*` = Current planned path
- `.` = Free cell

## Sample Output
```text
UGV Dynamic Obstacle Navigation using D* Lite
Press Enter to use the default value.

Enter number of rows [default: 10]:
Enter number of columns [default: 10]:
Enter initial obstacle probability [default: 0.08]:
Enter dynamic obstacle probability [default: 0.15]:

Initial environment:

S * * * . . . . . .
. . . * . . . . . .
. . . * * * . . . .
. . . . . * . . . .
. . . . . * * * . .
. . . . . . . * . .
. . . . . . . * * .
. . . . . . . . * .
. . . . . . . . * .
. . . . . . . . * G

Current planned path:

S * * * . . . . . .
. . . * . . . . . .
. . . * * * . . . .
. . . . . * . . . .
. . . . . * * * . .
. . . . . . . * . .
. . . . . . . * * .
. . . . . . . . * .
. . . . . . . . * .
. . . . . . . . * G

New obstacle detected at (2, 4).
Planned route affected. Repairing path with D* Lite...

Updated planned path:

S . . . . . . . . .
U * * * . . . . . .
. . . * # . . . . .
. . . * * * . . . .
. . . . . * . . . .
. . . . . * * * . .
. . . . . . . * . .
. . . . . . . * * .
. . . . . . . . * .
. . . . . . . . * G

Goal reached.

Mission Summary:
------------------------------
Total Steps            : 18
Total Repairs          : 1
Total Obstacle Updates : 1
Mission Status         : Success
Total Cost             : 18
Total Nodes Processed  : 74
------------------------------
```



# Question 3: UGV Navigation in a Dynamic Obstacle Environment Using D* Lite

## Description
This project simulates an Unmanned Ground Vehicle (UGV) moving through a dynamic battlefield represented as a 2D grid. The UGV starts at the top-left corner of the grid and must reach the goal at the bottom-right corner while avoiding obstacles. Unlike a static environment, this battlefield can change while the UGV is already moving, because new obstacles may appear during execution. A path that is valid at one moment may become blocked in the next, so the vehicle must be able to repair its route and continue toward the goal.

To handle this, the project uses **D* Lite**, which is a dynamic path-planning algorithm designed for environments that change over time. Instead of planning once and failing when the map changes, D* Lite updates only the affected parts of the search and repairs the path efficiently. This makes it much better suited for dynamic navigation than repeatedly running a static shortest-path algorithm from scratch.

The program allows the user to enter the grid size and obstacle probabilities, generates a valid initial battlefield, computes the initial route, inserts new obstacles while the UGV is moving, repairs the path when needed, and finally prints a mission summary.

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
##How the Algorithm Works

D* Lite is an incremental heuristic search algorithm used for dynamic path planning. It is designed for situations where the environment can change after the initial path has already been planned.

The algorithm maintains two values for each node:

g(n): the current best-known path cost from the node to the goal

rhs(n): a one-step lookahead value used to detect whether the node is consistent

A node is considered:

consistent if g(n) = rhs(n)

inconsistent if g(n) != rhs(n)

The algorithm begins by setting the goal node’s rhs to 0 and inserting it into a priority queue. It then works backward through the grid, updating costs until the start node becomes locally consistent. Once this is done, the UGV can follow the best path toward the goal.

When a new obstacle appears:

The map is updated.

The affected cells are marked inconsistent.

D* Lite updates only the necessary nodes instead of recomputing everything.

The path is repaired from the UGV’s current position.

This makes D* Lite much more efficient than rerunning A* or Dijkstra from scratch every time the environment changes.

## HOW TO RUN 
python main.py or python3 main.py

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

Current planned path:

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
Total Steps: 18
Total Repairs: 1
Total Obstacle Updates: 1
Mission Status: Success
Total Cost: 18
Total Nodes Processed: 74

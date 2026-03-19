# Question 2: UGV Path Planning in a Static Obstacle Battlefield Using A* Algorithm

## Problem Statement

An Unmanned Ground Vehicle (UGV) must move from a start position to a goal position in a battlefield while avoiding obstacles. The battlefield is represented as a grid, where some cells are free and some are blocked by static obstacles. Since the obstacles are already known and do not change during execution, the task is to compute the shortest valid path from the start node to the goal node while minimizing movement cost.

This is a path-planning problem in a discrete search space. A search algorithm is required to explore possible paths, avoid blocked cells, and return the most efficient route.

## Description

This project simulates static battlefield navigation for a UGV using the A* search algorithm. The environment is modeled as a 2D grid. Each cell represents either traversable terrain or an obstacle. The UGV starts at the top-left corner of the grid and attempts to reach the bottom-right corner while avoiding blocked cells.

The project supports three obstacle density levels:
- Low density: 10% obstacles
- Medium density: 20% obstacles
- High density: 30% obstacles

The program generates the battlefield, applies the A* algorithm, reconstructs the path if a solution exists, and displays the result in a readable text-based grid along with performance metrics.

## Project Structure

```text
q2_static_ugv/
├── src/
│   ├── astar.py
│   ├── grid.py
│   └── utils.py
├── main.py
├── README.md
└── requirements.txt
```

## Project Structure Description

- `src/astar.py`  
  Contains the core A* search algorithm. It defines the heuristic function, finds valid neighboring cells, manages the priority queue, and computes the shortest path cost.

- `src/grid.py`  
  Handles battlefield generation. It creates the grid, applies obstacle density rules, and places static obstacles while ensuring that the start and goal cells remain free.

- `src/utils.py`  
  Contains helper functions such as reconstructing the path from parent pointers, printing the battlefield in a readable format, and displaying measures of effectiveness.

- `main.py`  
  Acts as the entry point of the program. It takes user input for obstacle density, generates the battlefield, runs the A* algorithm, and prints the final result.

- `requirements.txt`  
  Lists project dependencies. This project uses only standard Python libraries, so no external packages are required.

## Algorithm Used

This project uses the **A\*** algorithm.

A* is a best-first search algorithm used to find the shortest path between a start node and a goal node. It combines:
- the actual path cost from the start node to the current node
- an estimated cost from the current node to the goal

The evaluation function is:

```text
f(n) = g(n) + h(n)
```

Where:
- `g(n)` is the actual cost from the start node to node `n`
- `h(n)` is the heuristic estimate from node `n` to the goal
- `f(n)` is the total estimated cost of the path through node `n`

### Heuristic Used

The heuristic used in this project is **Manhattan distance**:

```text
h(n) = |x1 - x2| + |y1 - y2|
```

This is suitable because the UGV is restricted to four-directional movement:
- up
- down
- left
- right

### Why A* Was Chosen

A* is a better choice than plain Dijkstra’s Algorithm for this problem because the search is goal-directed. Dijkstra explores too broadly, while A* uses a heuristic to guide the search toward the goal, usually reducing the number of explored nodes.

## How the Algorithm Is Implemented

The implementation works as follows:

1. The battlefield is created as a 2D grid.
2. Obstacles are placed randomly according to the selected density level.
3. The start node is fixed at the top-left corner.
4. The goal node is fixed at the bottom-right corner.
5. The A* algorithm begins from the start node.
6. A priority queue is used to always expand the node with the lowest estimated total cost.
7. For each valid neighbor:
   - the new path cost is calculated
   - the heuristic value is added
   - the node is inserted into the priority queue if it gives a better route
8. Parent pointers are stored so the final shortest path can be reconstructed after reaching the goal.
9. If the goal is unreachable, the program reports failure.

## Movement Rules

The UGV can move only in four directions:
- Up
- Down
- Left
- Right

Each movement has a cost of 1.

Blocked cells cannot be entered.

## Output Symbols

The grid output uses the following symbols:

- `S` = Start
- `G` = Goal
- `#` = Obstacle
- `*` = Final path
- `.` = Free cell

## Measures of Effectiveness

The program reports the following:

- **Path Length**: number of steps in the final path
- **Nodes Explored**: number of nodes processed by the algorithm
- **Mission Status**: whether the UGV successfully reached the goal
- **Total Cost**: total travel cost of the final path

These values help evaluate how well the algorithm performs under different obstacle densities.

## How to Run

Open a terminal inside the `q2_static_ugv` folder and run:

```bash
python main.py
```

If your system requires Python 3 explicitly, run:

```bash
python3 main.py
```

On some Windows systems, you may also run:

```bash
py main.py
```

When the program starts, enter one of the following density levels when prompted:

```text
low
medium
high
```

## Sample Output

```text
UGV Static Obstacle Path Planning using A*
Obstacle Density Levels: low, medium, high
Enter obstacle density level: medium

Path found successfully.

S * . . # . . . . . . . . . . . . . . .
# * . . # . . . . . . . . . . . . . . .
. * * * # . . . . . . . . . . . . . . .
. . . * . . . . # . . . . . . . . . . .
. . . * . . . . # . . . . . . . . . . .
. . . * * * . . . . . . . . . . . . . .
. . . . . * . . . . # . . . . . . . . .
. . . . . * * * . . # . . . . . . . . .
. . . . . . . * . . . . . . . . . . . .
. . . . . . . * * * * . . . . . . . . .
. . . . . . . . . . * . . # . . . . . .
. . . . . . . . . . * . . # . . . . . .
. . . . . . . . . . * . . . . . . . . .
. . . . . . . . . . * . . . . . . . . .
. . . . . . . . . . * * * . . . . . . .
. . . . . . . . . . . . * . . . . . . .
. . . . . . . . . . . . * * * . . . . .
. . . . . . . . . . . . . . * . . . . .
. . . . . . . . . . . . . . * * * * * .
. . . . . . . . . . . . . . . . . . * G

Measures of Effectiveness:
Path Length: 38
Nodes Explored: 171
Mission Status: Success
Total Cost: 38
```

## Conclusion

This project demonstrates how A* can be used to solve a static grid-based battlefield navigation problem efficiently. By combining actual path cost with heuristic guidance, the algorithm finds the shortest valid path while exploring fewer unnecessary nodes than uninformed search methods. The modular structure also makes the project easy to understand, maintain, and extend.

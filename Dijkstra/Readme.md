# Question 1: Shortest Path Between Indian Cities Using Dijkstra’s Algorithm

## Overview

This project implements Dijkstra’s Algorithm to find the shortest path in a road network of Indian cities.

The problem is modeled as a weighted graph where:
- each city is a node
- each road is an edge
- each distance is the edge weight

Given a source city, the program computes:
1. the shortest distance to all other cities
2. the shortest path to a selected destination

---

## Problem Statement

When actions have different costs in a state-based search space, best-first search can be used where the evaluation function is the path cost. This is implemented as Dijkstra’s Algorithm.

This project applies Dijkstra’s Algorithm to a graph representing Indian cities and road distances.

---

## Objective

- Model cities and roads as a graph  
- Apply Dijkstra’s Algorithm  
- Compute shortest distances  
- Reconstruct shortest paths  

---

## Project Structure

q1_india_dijkstra/
│
├── data/
│   ├── cities.csv
│   └── roads.csv
│
├── src/
│   ├── dijkstra.py
│   ├── graph_loader.py
│   └── utils.py
│
├── main.py
├── README.md
└── requirements.txt

---

## File Description

data/cities.csv  
Contains list of cities

data/roads.csv  
Contains connections and distances

src/graph_loader.py  
Reads CSV files and builds the graph

src/dijkstra.py  
Implements Dijkstra’s Algorithm

src/utils.py  
Contains helper functions (path reconstruction, printing)

main.py  
Runs the program and handles user input/output

---

## Graph Representation

The graph is stored as an adjacency list.

Example:
{
  "Delhi": [("Jaipur", 281), ("Chandigarh", 244)],
  "Jaipur": [("Delhi", 281)]
}

The graph is undirected since roads are two-way.

---

## Algorithm Used: Dijkstra’s Algorithm

Dijkstra’s Algorithm finds the shortest path from one source node to all other nodes in a graph with non-negative weights.

---

## How the Algorithm Works

1. Set distance of source = 0  
2. Set all other distances = infinity  
3. Use a priority queue (min-heap)  
4. Pick node with smallest distance  
5. Update neighbors using relaxation  
6. Repeat until all nodes processed  

---

## Relaxation

If:
distance[A] + weight < distance[B]

Then:
distance[B] = distance[A] + weight  
parent[B] = A  

---

## Path Reconstruction

Parents are stored to rebuild the path.

Example:
Mumbai <- Ahmedabad <- Jaipur <- Delhi

Final path:
Delhi -> Jaipur -> Ahmedabad -> Mumbai

---

## Priority Queue

A min-heap (heapq) is used to always process the closest node first, improving efficiency.

---

## Time Complexity

O((V + E) log V)

V = number of cities  
E = number of roads  

---

## Space Complexity

O(V + E)

---

## Program Workflow

1. Load cities from CSV  
2. Load graph from CSV  
3. Display cities  
4. Take source input  
5. Run Dijkstra  
6. Display distances  
7. Take destination input  
8. Print shortest path  

---

## How to Run

Step 1:
cd q1_india_dijkstra

Step 2:
python main.py

OR

python3 main.py

OR (Windows):
py main.py

---

## Input Format

Enter city names exactly as in dataset:
Delhi  
Mumbai  
Hyderabad  

---

## Example Run

Available Cities:
Delhi, Mumbai, Chennai, Hyderabad...

Enter source city: Delhi

Shortest distances printed...

Enter destination city: Mumbai

Shortest Path:
Delhi -> Jaipur -> Ahmedabad -> Mumbai  
Total Distance: 1469 km  

---

## Design Choices

- Adjacency list used for efficiency  
- Modular design for readability  
- Separate files for logic and I/O  

---

## Limitations

- Uses a small subset of cities  
- Not a full national dataset  

---

## Future Improvements

- Use real-world large datasets  
- Add visualization  
- Compare with A*  
- Integrate maps  

---

## Conclusion

This project demonstrates how Dijkstra’s Algorithm can be applied to real-world navigation problems using graphs. It efficiently computes shortest paths and is suitable for road networks with non-negative distances.

---

## Author

Your Name

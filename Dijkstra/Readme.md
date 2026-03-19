# Question 1 - Dijkstra on Indian Cities

This project implements Dijkstra’s Algorithm to find the shortest path from a given source city to all other cities in a road network.

## Problem Statement
Model Indian cities and their road distances as a weighted graph and use Dijkstra’s Algorithm to compute the shortest path.

## Project Structure

q1_india_dijkstra/
- data/
  - cities.csv
  - roads.csv
- src/
  - dijkstra.py
  - graph_loader.py
  - utils.py
- output/
  - sample_output.txt
- main.py
- README.md
- requirements.txt

## Graph Model
- Nodes: Cities
- Edges: Roads
- Edge Weights: Distance in kilometers

## Algorithm Used
Dijkstra’s Algorithm with a priority queue (min-heap).

## Time Complexity
O((V + E) log V)

Where:
- V = number of cities
- E = number of roads

## How to Run

```bash
python main.py 
python3 main.py
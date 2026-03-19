import heapq


def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    parents = {node: None for node in graph}

    distances[start] = 0
    priority_queue = [(0, start)]  # (distance, node)

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Skip outdated queue entries
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            new_distance = current_distance + weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                parents[neighbor] = current_node
                heapq.heappush(priority_queue, (new_distance, neighbor))

    return distances, parents
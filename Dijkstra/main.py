from src.graph_loader import load_cities, load_graph
from src.dijkstra import dijkstra
from src.utils import reconstruct_path, print_all_distances, print_single_path


def main():
    cities_file = "data/cities.csv"
    roads_file = "data/roads.csv"

    cities = load_cities(cities_file)
    graph = load_graph(roads_file)

    print("Available Cities:")
    for city in cities:
        print("-", city)

    start_city = input("\nEnter the source city: ").strip()
    if start_city not in graph:
        print("Error: Source city not found in graph.")
        return

    distances, parents = dijkstra(graph, start_city)

    print_all_distances(distances, start_city)

    destination_city = input("\nEnter the destination city to view shortest path: ").strip()
    if destination_city not in graph:
        print("Error: Destination city not found in graph.")
        return

    if distances[destination_city] == float('inf'):
        print(f"No path exists from {start_city} to {destination_city}.")
        return

    path = reconstruct_path(parents, destination_city)
    print_single_path(path, distances[destination_city])


if __name__ == "__main__":
    main()
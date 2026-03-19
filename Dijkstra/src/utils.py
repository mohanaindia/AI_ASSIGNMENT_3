def reconstruct_path(parents, target):
    path = []
    current = target

    while current is not None:
        path.append(current)
        current = parents[current]

    path.reverse()
    return path


def print_all_distances(distances, start):
    print(f"\nShortest distances from {start} to all cities:\n")
    for city in sorted(distances.keys()):
        if distances[city] == float('inf'):
            print(f"{city}: Not reachable")
        else:
            print(f"{city}: {distances[city]} km")


def print_single_path(path, total_distance):
    print("\nShortest Path:")
    print(" -> ".join(path))
    print(f"Total Distance: {total_distance} km")
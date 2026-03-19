import csv
from collections import defaultdict


def load_cities(cities_file):
    cities = []
    with open(cities_file, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cities.append(row['city'].strip())
    return cities


def load_graph(roads_file):
    graph = defaultdict(list)

    with open(roads_file, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            source = row['source'].strip()
            destination = row['destination'].strip()
            distance = int(row['distance'])

            graph[source].append((destination, distance))
            graph[destination].append((source, distance))

    return graph
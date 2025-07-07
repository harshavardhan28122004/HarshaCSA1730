import itertools

# Graph distances between cities A, B, C, D
graph = {
    'A': {'B': 10, 'C': 15, 'D': 10},
    'B': {'A': 10, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30}
}

cities = list(graph.keys())
start = 'A'
min_cost = float('inf')
best_path = []

# Generate all permutations excluding the starting city
for perm in itertools.permutations(cities[1:]):
    path = [start] + list(perm) + [start]
    cost = 0

    for i in range(len(path) - 1):
        cost += graph[path[i]][path[i + 1]]

    if cost < min_cost:
        min_cost = cost
        best_path = path

# Output
print("Best path:", best_path)
print("Minimum distance:", min_cost)

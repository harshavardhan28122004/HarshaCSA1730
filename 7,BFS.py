from collections import deque

def bfs_shortest_path(graph, start, end):
    visited = set()
    queue = deque([[start]])  # queue of paths

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == end:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    return None

if __name__ == "__main__":
    graph = {
        0: [1, 2],
        1: [0, 2, 3],
        2: [0, 1, 3],
        3: [1, 2, 4],
        4: [3]
    }

    start_node = 0
    end_node = 4
    shortest_path = bfs_shortest_path(graph, start_node, end_node)

    if shortest_path:
        print("Shortest path from", start_node, "to", end_node, "is:", shortest_path)
    else:
        print("No path found.")

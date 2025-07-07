from collections import defaultdict

class MapColoring:
    def __init__(self, graph, colors):   # <-- fixed here
        self.graph = graph
        self.colors = colors
        self.assignment = {}

    def is_safe(self, node, colour):
        for neighbour in self.graph[node]:
            if neighbour in self.assignment and self.assignment[neighbour] == colour:
                return False
        return True

    def select_unassigned_node(self):
        for node in self.graph:
            if node not in self.assignment:
                return node

    def backtrack(self):
        if len(self.assignment) == len(self.graph):
            return True

        node = self.select_unassigned_node()
        for colour in self.colors:
            if self.is_safe(node, colour):
                self.assignment[node] = colour
                if self.backtrack():
                    return True
                del self.assignment[node]
        return False

# Graph as per your image
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Colors and solver
colors = ['Red', 'Green', 'Blue']
solver = MapColoring(graph, colors)

# Run CSP
if solver.backtrack():
    print("Colour Assignment:")
    print(solver.assignment)
else:
    print("No solution found.")

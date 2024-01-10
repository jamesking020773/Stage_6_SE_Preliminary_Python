class Graph:
    def __init__(self):
        self.graph = {}  # Initializes an empty dictionary to store the adjacency list.

    def add_edge(self, u, v):
        if u not in self.graph:  # Checks if the node u is not in the graph.
            self.graph[u] = []  # Initializes an empty list for node u.
        self.graph[u].append(v)  # Adds an edge from node u to node v.

# Demonstrates creating a graph and adding edges
my_graph = Graph()
my_graph.add_edge(1, 2)  # Adds an edge from 1 to 2.
my_graph.add_edge(1, 3)  # Adds an edge from 1 to 3.
my_graph.add_edge(2, 4)  # Adds an edge from 2 to 4.
my_graph.add_edge(3, 4)  # Adds an edge from 3 to 4.

# Prints the graph
print("Graph:", my_graph.graph)  # Prints the adjacency list of the graph.

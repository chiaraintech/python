import networkx as nx

def shortest_path(G, source, target):
    # Use the Dijkstra's algorithm to find the shortest path
    return nx.dijkstra_path(G, source, target)

# Create a graph
G = nx.Graph()

# Add vertices to the graph
G.add_node("A")
G.add_node("B")
G.add_node("C")
G.add_node("D")

# Add edges to the graph
G.add_edge("A", "B", weight=10)
G.add_edge("B", "C", weight=20)
G.add_edge("C", "D", weight=15)
G.add_edge("A", "D", weight=25)

# Find the shortest path
path = shortest_path(G, "A", "D")

# Print the shortest path
print(path) # ['A', 'B', 'C', 'D']

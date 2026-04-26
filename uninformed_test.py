import networkx as nx
import matplotlib.pyplot as plt
from bfs import bfs
from dfs import dfs
import importlib
id_dfs_module = importlib.import_module('id-dfs')
iddfs = id_dfs_module.iddfs

# Your graph - represents the tree diagram exactly
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

# Create directed graph
G = nx.DiGraph()

# Add edges
for node, neighbors in graph.items():
    for neighbor in neighbors:
        G.add_edge(node, neighbor)

# Manual hierarchical positions to match the diagram exactly
# A at top, B-C below, D-E-F below that, G below E
pos = {
    'A': (0, 3),
    'B': (-1, 2),
    'C': (1, 2),
    'D': (-1.5, 1),
    'E': (-0.5, 1),
    'F': (1, 1),
    'G': (-0.5, 0)
}

# Draw
plt.figure(figsize=(8, 6))

nx.draw(
    G, pos,
    with_labels=True,
    node_color='lightblue',
    node_size=2000,
    font_size=12,
    font_weight='bold',
    arrows=True,
    arrowsize=15,
    edge_color='black',
    linewidths=1,
    width=1.5
)

plt.title("Graph Representation")
plt.axis('off')  # Hide axes for cleaner look
plt.tight_layout()
plt.show()

print("BFS:", bfs(graph, 'A'))
print("DFS:", dfs(graph, 'A'))
print("IDDFS:", iddfs(graph, 'A', 3))
import networkx as nx
import matplotlib.pyplot as plt

# Define your network topology using NetworkX
G = nx.Graph()

# Add nodes (routers or devices)
G.add_node("Router1")
G.add_node("Router2")
G.add_node("Router3")
G.add_node("Router4")

# Add edges (connections between nodes)
G.add_edge("Router1", "Router2")
G.add_edge("Router2", "Router3")
G.add_edge("Router3", "Router4")
G.add_edge("Router4", "Router1")

# Visualize the network topology using Matplotlib
pos = nx.spring_layout(G)  # Layout for the graph

# You can customize the graph visualization, e.g., node size, color, etc.
nx.draw(G, pos, with_labels=True, node_size=500, node_color="skyblue", font_size=10)

# Save or display the network topology graph
plt.title("Network Topology")
plt.axis("off")
plt.savefig("network_topology.png")  # Save as an image (optional)
plt.show()

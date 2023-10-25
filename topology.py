import networkx as nx
import matplotlib.pyplot as plt

# Create a graph object
G = nx.Graph()

# Add nodes
G.add_node("Router1")
G.add_node("Router2")
G.add_node("Host1")
G.add_node("Host2")

# Add edges
G.add_edge("Router1", "Host1")
G.add_edge("Router1", "Router2")
G.add_edge("Router2", "Host2")

# Draw the graph
pos = nx.spring_layout(G)  # You can choose different layout algorithms
nx.draw(G, pos, with_labels=True, node_size=500, node_color="skyblue", font_size=10, font_color="black")
plt.show()

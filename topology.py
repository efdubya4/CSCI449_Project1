import networkx as nx
import matplotlib.pyplot as plt

# Create a graph object
G = nx.Graph()

# Add nodes
G.add_node("10.168.118.249")
G.add_node("10.126.15.32")
G.add_node("Host1")
G.add_node("Host2")

# Add edges
G.add_edge("10.106.136.245", "Host1")
G.add_edge("Router1", "Router2")
G.add_edge("Router2", "Host2")

# Draw the graph
pos = nx.spring_layout(G)  # You can choose different layout algorithms
nx.draw(G, pos, with_labels=True, node_size=500, node_color="skyblue", font_size=10, font_color="black")
plt.show()

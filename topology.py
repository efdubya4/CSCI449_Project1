import networkx as nx
import matplotlib.pyplot as plt

# Function to create a network topology diagram
def create_topology(locations_data):
    # Create a graph
    G = nx.Graph()

    for i, location in enumerate(locations_data):
        location_name = location["location"]
        routers = location["routers"]

        for j, router in enumerate(routers):
            node_label = f'{location_name}, Router {j + 1}'
            G.add_node(node_label, label=node_label)

            # Connect nodes to represent the network path within the location
            if j > 0:
                previous_node = f'{location_name}, Router {j}'
                G.add_edge(previous_node, node_label)

        # Connect the last router in this location to the first router in the next location (if any)
        if i < len(locations_data) - 1:
            last_node_current = f'{location_name}, Router {j}'
            next_location = locations_data[i + 1]
            first_node_next = f'{next_location["location"]}, Router 1'
            G.add_edge(last_node_current, first_node_next)

    # Set node positions for the plot
    pos = nx.spring_layout(G)

    # Draw the nodes and edges
    nx.draw(G, pos, with_labels=False, node_size=500, node_color='lightblue', font_size=8, font_color='black')
    labels = nx.get_node_attributes(G, 'label')
    nx.draw_networkx_labels(G, pos, labels)

    # Display the plot
    plt.axis('off')
    plt.title('Network Topology Diagram')
    plt.show()

if __name__ == "__main__":
    # Define the list of locations and associated routers
    #locations = [ "", "", ""]

    locations_data = [
        {
            "location": "Founder's Library",
            "routers": ["10.61.96.1", "10.199.4.141", "10.199.3.1", "66.44.94.195", "138.238.3.33", "138.238.3.13"],
        },
        {
            "location": "Howard Middle School",
            "routers": ["10.61.96.1", "10.199.4.141", "10.199.3.1", "66.44.94.195", "138.238.3.33", "138.238.3.13"],
        },
        {
            "location": "Math Building",
            "routers": ["Router6", "Router7", "Router8"],
        },
        {
            "location": "College of Arts and Science",
            "routers": ["Router1", "Router2", "Router3"],
        },
        {
            "location": "Blackburn Student Center",
            "routers": ["Router4", "Router5"],
        },
        {
            "location": "College of Fine Arts",
            "routers": ["Router6", "Router7", "Router8"],
        },
        {
            "location": "Douglass Hall",
            "routers": ["Router1", "Router2", "Router3"],
        },
        {
            "location": "Administration Building",
            "routers": ["Router4", "Router5"],
        },
        {
            "location": "Carnegie Hall",
            "routers": ["Router6", "Router7", "Router8"],
        },
        {
            "location": "Mackey Building",
            "routers": ["Router1", "Router2", "Router3"],
        },
        {
            "location": "School of Social Workl",
            "routers": ["Router4", "Router5"],
        },
        {
            "location": "School of Business",
            "routers": ["Router6", "Router7", "Router8"],
        },
        {
            "location": "Crampton Auditorium",
            "routers": ["Router4", "Router5"],
        },
        {
            "location": "Burr Gymnasium",
            "routers": ["Router6", "Router7", "Router8"],
        },
        {
            "location": "College of Arts and Science",
            "routers": ["Router1", "Router2", "Router3"],
        },
        {
            "location": "School of Education",
            "routers": ["Router4", "Router5"],
        },
        {
            "location": "Undergraduate Library",
            "routers": ["Router6", "Router7", "Router8"],
        },
        {
            "location": "MET Building",
            "routers": ["Router1", "Router2", "Router3"],
        },
        {
            "location": "Health Science Library",
            "routers": ["Router4", "Router5"],
        },
        
        {
            "location": "Chemistry Building",
            "routers": ["Router6", "Router7", "Router8"],
        },
    ]

    create_topology(locations_data)

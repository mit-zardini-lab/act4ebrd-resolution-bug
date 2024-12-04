import networkx as nx


# Create a 2D grid graph with integer node indices
def create_grid(m, n):
    G = nx.Graph()
    node_mapping = {}  # Map (row, col) to a unique integer
    counter = 0

    for i in range(m):
        for j in range(n):
            node_mapping[(i, j)] = counter
            counter += 1

    for i in range(m):
        for j in range(n):
            if i > 0:
                G.add_edge(node_mapping[(i, j)], node_mapping[(i - 1, j)], weight=1)
            if j > 0:
                G.add_edge(node_mapping[(i, j)], node_mapping[(i, j - 1)], weight=1)

    # Generate positions for nodes (2D grid layout)
    pos = {node_mapping[(x, y)]: (y, -x) for x, y in node_mapping.keys()}  # Flip y-coordinates for a natural grid look

    return G, node_mapping


# Create a 3x3 grid graph
G, node_mapping = create_grid(3, 3)

od_flows = {
    (1, 8): 190,
    (2, 6): 10,
}

routes = [
    (1, 2, 5, 8, 7, 6),
    (1, 2, 5, 4, 3, 6, 7, 8),
]

possible_fleet_compositions = [
    (1, 1),
    (2, 0),
    (0, 2),
    (2, 1),
    (1, 2),
    (0, 3),
    (3, 0),
]


def plot_problem_graph(G, pos, routes, od_flows):
    fig, axes = plt.subplots(len(routes), 1, figsize=(8, len(routes) * 4))

    if len(routes) == 1:
        axes = [axes]

    for ax, route in zip(axes, routes):
        nx.draw(G, pos, with_labels=True, node_color='lightblue', ax=ax)
        edges = [(route[i], route[i + 1]) for i in range(len(route) - 1)]
        nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='r', width=2, ax=ax)

        for (start, end), flow in od_flows.items():
            ax.annotate(f'Flow: {flow}', xy=pos[start], xytext=pos[end],
                        arrowprops=dict(facecolor='blue', shrink=0.05))

    plt.tight_layout()
    return fig, axes



import matplotlib.pyplot as plt

# Draw the graph
nx.draw(G, pos, with_labels=True, node_color='lightblue')

# Highlight the first route
route = routes[1]
edges = [(route[i], route[i + 1]) for i in range(len(route) - 1)]
nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='r', width=2)

# Display the plot
plt.show()

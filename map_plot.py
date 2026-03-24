import osmnx as ox

def plot_route(G, path):
    ox.plot_graph_route(G, path, route_linewidth=3)
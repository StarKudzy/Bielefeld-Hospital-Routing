from map_plot import plot_route
import math
import time
import tracemalloc
import osmnx as ox
import networkx as nx

PLACE = "Bielefeld, Germany"

print("Loading map...")
G = ox.graph_from_place(PLACE, network_type="drive")

print("Loading hospitals...")
hospitals = ox.features_from_place(PLACE, tags={"amenity": "hospital"})

hospital_nodes = []
for _, row in hospitals.iterrows():
    p = row.geometry.centroid
    node = ox.distance.nearest_nodes(G, p.x, p.y)
    hospital_nodes.append(node)

hospital_nodes = list(set(hospital_nodes))
print("Hospitals found:", len(hospital_nodes))

start_place = input("Enter start location in Bielefeld: ")
lat, lon = ox.geocode(start_place)
start_node = ox.distance.nearest_nodes(G, lon, lat)

print("Start node:", start_node)

def heuristic(a, b):
    x1, y1 = G.nodes[a]["x"], G.nodes[a]["y"]
    x2, y2 = G.nodes[b]["x"], G.nodes[b]["y"]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def run_algo(name):
    best_path = None
    best_length = float("inf")

    tracemalloc.start()
    t1 = time.perf_counter()

    for h in hospital_nodes:
        try:
            if name == "Dijkstra":
                length, path = nx.single_source_dijkstra(G, start_node, h, weight="length")
            else:
                path = nx.astar_path(G, start_node, h, heuristic=heuristic, weight="length")
                length = nx.path_weight(G, path, weight="length")

            if length < best_length:
                best_length = length
                best_path = path
        except nx.NetworkXNoPath:
            pass

    t2 = time.perf_counter()
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return best_path, best_length, t2 - t1, peak / 1024

d_path, d_len, d_time, d_mem = run_algo("Dijkstra")
a_path, a_len, a_time, a_mem = run_algo("A*")

print("\n=== Comparison Table ===")
print("{:<10} {:<15} {:<12} {:<12}".format("Algorithm", "Path Length(m)", "Runtime(s)", "Memory(KB)"))
print("-" * 55)
print("{:<10} {:<15.2f} {:<12.6f} {:<12.2f}".format("Dijkstra", d_len, d_time, d_mem))
print("{:<10} {:<15.2f} {:<12.6f} {:<12.2f}".format("A*", a_len, a_time, a_mem))

print("\nChoose algorithm to display path:")
print("A - Dijkstra")
print("B - A*")
choice = input("Enter choice (A/B): ").upper()

if choice == "A":
    print("\nAlgorithm used: Dijkstra")
    print("Path found:", d_path)
    print("Total path length:", round(d_len, 2), "meters")
    print("Runtime:", round(d_time, 6), "seconds")
    print("Memory usage:", round(d_mem, 2), "KB")
    
    plot_route(G, d_path)
    

elif choice == "B":
    print("\nAlgorithm used: A*")
    print("Path found:", a_path)
    print("Total path length:", round(a_len, 2), "meters")
    print("Runtime:", round(a_time, 6), "seconds")
    print("Memory usage:", round(a_mem, 2), "KB")
    
    plot_route(G, a_path)
    

else:
    print("Invalid choice")
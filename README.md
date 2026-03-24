# Bielefeld Emergency Hospital Routing

Shortest Path Analysis using Dijkstra and A* Algorithms

---

# 1. Project Description

This project aims to improve emergency response efficiency by computing the shortest route from any location in Bielefeld, Germany to the nearest hospital. The city is modeled as a graph using OpenStreetMap data, where:

* Nodes represent road intersections
* Edges represent roads connecting intersections
* Hospitals are mapped to the nearest nodes
* Pathfinding algorithms compute optimal routes

Two shortest path algorithms are implemented and compared:

* Dijkstra’s Algorithm
* A* Search Algorithm

The performance of both algorithms is evaluated based on:

* Path length
* Runtime
* Memory usage

---

# 2. Features

* Load Bielefeld road network automatically
* Extract hospital locations
* Convert user input location to graph node
* Compute shortest path to nearest hospital
* Compare Dijkstra and A* algorithms
* Display performance comparison table
* Visualize selected route on map

---

# 3. Project Structure

```
bielefeld-routing/
│
├── main.py        # Main program (algorithms + comparison)
├── map_plot.py    # Route visualization
└── README.md      # Project documentation
```

---

# 4. Requirements

This project requires Python 3.9+.

Install required libraries:

```
pip install osmnx networkx scikit-learn matplotlib
```

Libraries used:

* osmnx → download map data from OpenStreetMap
* networkx → graph algorithms
* scikit-learn → nearest node search
* matplotlib → route visualization

---

# 5. Installation (Step-by-Step)

### Step 1 — Clone or Download Project

```
git clone <repository-url>
cd bielefeld-routing
```

or manually download and place files in a folder.

### Step 2 — Install Dependencies

```
pip install osmnx networkx scikit-learn matplotlib
```

### Step 3 — Run Program

```
python main.py
```

---

# 6. How the Program Works

The program follows these steps:

1. Load Bielefeld road network from OpenStreetMap
2. Extract hospital locations
3. Convert hospitals into graph nodes
4. Ask user for start location
5. Convert start location to nearest node
6. Run Dijkstra algorithm
7. Run A* algorithm
8. Measure runtime and memory usage
9. Display comparison table
10. User selects algorithm
11. Display selected route
12. Plot route on map

---

# 7. Code Explanation

## 7.1 Load Road Network

```
G = ox.graph_from_place(PLACE, network_type="drive")
```

Downloads the Bielefeld road network and converts it into a graph.

---

## 7.2 Extract Hospital Locations

```
hospitals = ox.features_from_place(PLACE, tags={"amenity": "hospital"})
```

Retrieves hospital locations from OpenStreetMap.

Hospitals are mapped to nearest nodes:

```
node = ox.distance.nearest_nodes(G, p.x, p.y)
```

---

## 7.3 Convert Start Location

User enters a location:

```
lat, lon = ox.geocode(start_place)
```

Convert to graph node:

```
start_node = ox.distance.nearest_nodes(G, lon, lat)
```

---

## 7.4 Dijkstra Algorithm

```
nx.single_source_dijkstra(G, start_node, h, weight="length")
```

Computes shortest path using Dijkstra’s algorithm.

---

## 7.5 A* Algorithm

```
nx.astar_path(G, start_node, h, heuristic=heuristic, weight="length")
```

Computes shortest path using A* search.

---

## 7.6 Performance Measurement

Runtime measured using:

```
time.perf_counter()
```

Memory usage measured using:

```
tracemalloc
```

---

## 7.7 Comparison Table Output

```
Algorithm   Path Length(m)   Runtime(s)   Memory(KB)
```

Displays performance comparison between algorithms.

---

## 7.8 Route Visualization

The selected route is plotted using:

```
plot_route(G, path)
```

This displays the computed shortest path.

---

# 8. Example Run

User input:

```
Enter start location in Bielefeld:
Bielefeld Hauptbahnhof, Germany
```

Output:

```
=== Comparison Table ===
Algorithm   Path Length(m)   Runtime(s)   Memory(KB)
-----------------------------------------------------
Dijkstra    4821.37          0.4123       912.45
A*          4821.37          0.1842       650.12
```

User selects:

```
A - Dijkstra
B - A*
```

The selected route is then displayed.

---

# 9. Experimental Scenarios

The program should be executed for at least five locations:

* Bielefeld Hauptbahnhof
* Universität Bielefeld
* Jahnplatz
* Sparrenburg
* Sennestadt

Results from each scenario are used for comparison.

---

# 10. Metrics Collected

For each algorithm:

* Path found
* Total path length (meters)
* Runtime (seconds)
* Memory usage (KB)

---

# 11. Data Source

* OpenStreetMap road network data
* Hospital locations from OpenStreetMap

---


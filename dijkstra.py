import math

def dijkstra_with_table(graph, start):
    # Initialize distances
    dist = {v: math.inf for v in graph}
    dist[start] = 0
    
    # Track predecessors to reconstruct path
    pred = {v: None for v in graph}

    visited = set()
    # Column order as in your LaTeX table
    vertices = ['B','C','D','E','F','G','H','I','J','Z']

    # LaTeX table header
    header = ["Iteration", "T"] + [f"L({v})" for v in vertices] + ["Path(Z)"]
    print(" & ".join(header), end=" \\\\ \\hline\n")

    iteration = 0
    print_state(iteration, visited, vertices, dist, pred, current="-")

    while len(visited) < len(graph):
        # Select unvisited vertex with smallest distance
        current = None
        min_dist = math.inf
        for v in graph:
            if v not in visited and dist[v] < min_dist:
                min_dist = dist[v]
                current = v
        if current is None:
            break

        visited.add(current)

        # Relax edges
        for neighbor, weight in graph[current]:
            if neighbor not in visited and dist[current] + weight < dist[neighbor]:
                dist[neighbor] = dist[current] + weight
                pred[neighbor] = current

        iteration += 1
        print_state(iteration, visited, vertices, dist, pred, current)

def bellman_ford_with_table(graph, start):
    vertices = ['B','C','D','E','F','G','H','I','J','Z']
    # Convert graph to edge list
    edges = []
    for u in graph:
        for v, w in graph[u]:
            edges.append((u, v, w))

    dist = {v: math.inf for v in graph}
    dist[start] = 0
    pred = {v: None for v in graph}

    header = ["Iteration", "T"] + [f"L({v})" for v in vertices] + ["Path(Z)"]
    print(" & ".join(header), end=" \\\\ \\hline\n")

    iteration = 0
    visited_dummy = set()
    print_state(iteration, visited_dummy, vertices, dist, pred, current="-")

    for i in range(1, len(graph)):
        updated_nodes = set()
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                pred[v] = u
                updated_nodes.add(v)
        iteration += 1
        print_state(iteration, updated_nodes, vertices, dist, pred, current=",".join(sorted(updated_nodes)) if updated_nodes else "-")

    # Negative cycle detection
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            print("Negative cycle detected!")
            return

def reconstruct_path(pred, node):
    if pred[node] is None:
        return "-"
    path = []
    while node is not None:
        path.append(node)
        node = pred[node]
    return "-".join(reversed(path))


def print_state(iteration, visited, vertices, dist, pred, current):
    row = [str(iteration)]
    # Visited nodes T
    row.append(",".join(sorted(visited)) if current != "-" else current)
    # Only costs in L(node) columns
    for v in vertices:
        row.append(str(dist[v]) if dist[v] != math.inf else r"$\infty$")
    # Path to Z
    row.append(reconstruct_path(pred, "Z"))
    print(" & ".join(row), end=" \\\\ \\hline\n")


graph = {
    'A': [('B', 3), ('E', 5), ('H', 4)],
    'B': [('A', 3), ('E', 5), ('F', 7), ('C', 2)],
    'C': [('B', 2), ('F', 2), ('G', 6), ('D', 3)],
    'D': [('C', 3), ('G', 7), ('Z', 2)],
    'E': [('A', 5), ('B', 5), ('F', 4), ('H', 7)],
    'F': [('B', 7), ('E', 4), ('H', 5), ('I', 4), ('J', 3), ('G', 4), ('C', 2)],
    'G': [('D', 7), ('C', 6), ('F', 4), ('J', 4), ('Z', 6)],
    'H': [('A', 4), ('E', 7), ('F', 5), ('I', 2)],
    'I': [('F', 4), ('H', 2), ('J', 6)],
    'J': [('I', 6), ('F', 3), ('G', 4), ('Z', 5)],
    'Z': [('D', 2), ('G', 6), ('J', 5)]
}

bellman_ford_with_table(graph, 'A')
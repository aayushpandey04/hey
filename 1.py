# Undirected Graph using adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# ---------------- DFS (Recursive) ----------------
def dfs(graph, node, visited):
    print(node, end=" ")
    visited.add(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Function to ensure all vertices are covered
def dfs_all(graph):
    visited = set()
    for node in graph:
        if node not in visited:
            dfs(graph, node, visited)


# ---------------- BFS ----------------
def bfs(graph, start, visited):
    queue = []

    visited.add(start)
    queue.append(start)

    while queue:
        node = queue.pop(0)
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Function to cover all vertices
def bfs_all(graph):
    visited = set()
    for node in graph:
        if node not in visited:
            bfs(graph, node, visited)


# ---------------- Main ----------------
print("DFS Traversal (All Vertices):")
dfs_all(graph)

print("\nBFS Traversal (All Vertices):")
bfs_all(graph)

#A–B, A–C
#B–D, B–E
#C–F
#E–F

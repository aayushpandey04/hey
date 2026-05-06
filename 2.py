def aStarAlgo(start_node, stop_node):
    open_set = set([start_node])
    closed_set = set()
    g = {}
    parents = {}

    g[start_node] = 0
    parents[start_node] = start_node

    while open_set:
        n = None

        for v in open_set:
            if n is None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v

        if n == stop_node:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()
            print("Path found:", path)
            return

        for (m, weight) in Graph_nodes.get(n, []):
            if m not in open_set and m not in closed_set:
                open_set.add(m)
                parents[m] = n
                g[m] = g[n] + weight
            else:
                if g[m] > g[n] + weight:
                    g[m] = g[n] + weight
                    parents[m] = n
                    if m in closed_set:
                        closed_set.remove(m)
                        open_set.add(m)

        open_set.remove(n)
        closed_set.add(n)

    print("Path does not exist!")


Graph_nodes = {}
heuristic_values = {}

n = int(input("Enter number of nodes: "))


for i in range(n):
    node = input(f"Enter node {i+1}: ")
    Graph_nodes[node] = []

e = int(input("Enter number of edges: "))
for i in range(e):
    u = input("From node: ")
    v = input("To node: ")
    w = int(input("Weight: "))
    Graph_nodes[u].append((v, w))
    Graph_nodes[v].append((u, w))  


for node in Graph_nodes:
    heuristic_values[node] = int(input(f"Heuristic for {node}: "))


def heuristic(n):
    return heuristic_values[n]


start = input("Enter start node: ")
goal = input("Enter goal node: ")

aStarAlgo(start, goal)

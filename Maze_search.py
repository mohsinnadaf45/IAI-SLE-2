from collections import deque

# Graph representation
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['G'],
    'F': ['G'],
    'G': []
}


# ---------------- BFS ----------------
def bfs(graph, start, goal):
    queue = deque([(start, [start])])
    visited = set()
    nodes_visited = []

    while queue:
        node, path = queue.popleft()

        if node in visited:
            continue

        visited.add(node)
        nodes_visited.append(node)

        if node == goal:
            return path, nodes_visited

        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append((neighbour, path + [neighbour]))

    return None, nodes_visited


# ---------------- DFS ----------------
def dfs(graph, start, goal):
    stack = [(start, [start])]
    visited = set()
    nodes_visited = []

    while stack:
        node, path = stack.pop()

        if node in visited:
            continue

        visited.add(node)
        nodes_visited.append(node)

        if node == goal:
            return path, nodes_visited

        # Reverse order to get A -> B -> D -> G
        for neighbour in reversed(graph[node]):
            if neighbour not in visited:
                stack.append((neighbour, path + [neighbour]))

    return None, nodes_visited


# Starting and destination nodes
start = 'A'
goal = 'G'

# Run BFS
bfs_path, bfs_visited = bfs(graph, start, goal)

# Run DFS
dfs_path, dfs_visited = dfs(graph, start, goal)


# ---------------- Results ----------------
print("========== BFS ==========")
print("Start:", start)
print("Destination:", goal)
print("Search Order:", " -> ".join(bfs_visited))
print("Route Found:", " -> ".join(bfs_path))
print("Nodes Visited:", len(bfs_visited))

print()

print("========== DFS ==========")
print("Start:", start)
print("Destination:", goal)
print("Search Order:", " -> ".join(dfs_visited))
print("Route Found:", " -> ".join(dfs_path))
print("Nodes Visited:", len(dfs_visited))

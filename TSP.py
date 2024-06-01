def solve_tsp(G: list[list[int]]):
    # Get size, an array to keep track of visited nodes, and the final path.
    n = len(G)
    visited = [False] * n
    path = []
    current_node = 0
    visited[0] = True
    path.append(0)

    while len(path) < n:
        next_node = None
        min_distance = float("inf")
        # Find minimum neighbor to current_node
        for node in range(n):
            if G[current_node][node] != 0 and not visited[node]:
                if G[current_node][node] < min_distance:
                    min_distance = G[current_node][node]
                    next_node = node
        # No neighbor found, in case it is disconnected
        if next_node is None:
            break

        # Update visited nodes, and continue path forward
        visited[next_node] = True
        path.append(next_node)
        current_node = next_node

    # Return back to start
    path.append(0)
    return path

G = [
    [0, 2, 3, 20, 1],
    [2, 0, 15, 2, 20],
    [3, 15, 0, 20, 13],
    [20, 2, 20, 0, 9],
    [1, 20, 13, 9, 0],
]

print(solve_tsp(G))
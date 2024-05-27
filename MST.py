def Prims(G: list[list[int]]):
    result = []
    visited = [0]

    while len(visited) < len(G):
        edges = {}
        for node in visited:
            for neighbor in range(len(G[node])):
                if G[node][neighbor] != 0 and neighbor not in visited:
                    edges[G[node][neighbor]] = (node, neighbor)
        min_val = min(list(edges.keys()))
        min_node, min_neighbor = edges[min_val]
        result.append((min_node, min_neighbor, G[min_node][min_neighbor]))
        visited.append(min_neighbor)
    return result


input = [
    [0, 8, 5, 0, 0, 0, 0],
    [8, 0, 10, 2, 18, 0, 0],
    [5, 10, 0, 3, 0, 16, 0],
    [0, 2, 3, 0, 12, 30, 14],
    [0, 18, 0, 12, 0, 0, 4],
    [0, 0, 16, 30, 0, 0, 26],
    [0, 0, 0, 14, 4, 26, 0]
]

print(Prims(input))

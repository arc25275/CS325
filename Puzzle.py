def solve_puzzle(Board, Source, Destination):
    m, n = len(Board), len(Board[0])
    distance = [[float("inf")] * n for _ in range(m)]
    distance[Source[0]][Source[1]] = 0
    unvisited = []
    path = []
    for i in range(m):
        for j in range(n):
            if Board[i][j] == "#":
                continue
            unvisited.append((i, j))
    while len(unvisited) > 0:
        min_node = None
        for node in unvisited:
            if min_node is None:
                min_node = node
            elif distance[node[0]][node[1]] < distance[min_node[0]][min_node[1]]:
                min_node = node
        # Try all neighbors
        neighbors = []
        if min_node[0] > 0:
            neighbors.append((min_node[0] - 1, min_node[1], "U"))
        if min_node[0] < m - 1:
            neighbors.append((min_node[0] + 1, min_node[1], "D"))
        if min_node[1] > 0:
            neighbors.append((min_node[0], min_node[1] - 1, "L"))
        if min_node[1] < n - 1:
            neighbors.append((min_node[0], min_node[1] + 1, "R"))
        for neighbor in neighbors:
            if Board[neighbor[0]][neighbor[1]] == "#":
                continue
            new_distance = distance[min_node[0]][min_node[1]] + 1
            if new_distance < distance[neighbor[0]][neighbor[1]]:
                distance[neighbor[0]][neighbor[1]] = new_distance
                path.append((min_node, neighbor))
        unvisited.remove(min_node)
    if distance[Destination[0]][Destination[1]] == float("inf"):
        return None
    current = Destination
    result = []
    directions = ""
    while current != Source:
        for edge in path:
            if (edge[1][0], edge[1][1]) == current:
                result.append((edge[1][0], edge[1][1]))
                current = edge[0]
                directions += edge[1][2]
                break
    result.append(Source)
    return result[::-1], directions[::-1]


# puzzle = [
#     ["-", "-", "-", "-", "-"],
#     ["-", "-", "#", "-", "-"],
#     ["-", "-", "-", "-", "-"],
#     ["#", "-", "#", "#", "-"],
#     ["-", "#", "-", "-", "-"]
# ]
puzzle = [
    ["-", "-", "-"],
    ["-", "-", "#"],
    ["-", "#", "-"]
]

print(solve_puzzle(puzzle, (2, 2), (2, 2)))

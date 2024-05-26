def minEffort(puzzle: list[list[int]]) -> int:
    n, m = len(puzzle), len(puzzle[0])
    unvisited = []
    for i in range(n):
        for j in range(m):
            unvisited.append((i, j))
    lowest_diff = [[float("inf")] * m for _ in range(n)]
    lowest_diff[0][0] = 0

    while len(unvisited) > 0:
        min_node = None
        # Find the node with the lowest height difference currently.
        # This is the best current option, as we are trying to find
        # the shortest path to the end.
        for node in unvisited:
            if min_node is None:
                min_node = node
            elif lowest_diff[node[0]][node[1]] < lowest_diff[min_node[0]][min_node[1]]:
                min_node = node

        neighbors = []
        # Get all neighbors that are currently valid (Not off of the puzzle)
        if min_node[0] > 0:
            neighbors.append((min_node[0] - 1, min_node[1]))
        if min_node[0] < n - 1:
            neighbors.append((min_node[0] + 1, min_node[1]))
        if min_node[1] > 0:
            neighbors.append((min_node[0], min_node[1] - 1))
        if min_node[1] < m - 1:
            neighbors.append((min_node[0], min_node[1] + 1))
        # For each neighbor, see if the new distance will be better than what it currently has, and if so, update it
        for neighbor in neighbors:
            height = abs(puzzle[min_node[0]][min_node[1]] - puzzle[neighbor[0]][neighbor[1]])
            new_max = max(height, lowest_diff[min_node[0]][min_node[1]])
            # Me keeping the terminology of "short", as if it was a normal dijkstra's algorithm threw me off,
            # and I made a mistake here when evaluating the new path
            if new_max < lowest_diff[neighbor[0]][neighbor[1]]:
                lowest_diff[neighbor[0]][neighbor[1]] = new_max
        unvisited.remove(min_node)
    return lowest_diff[n - 1][m - 1]


# puzzle = [[1, 3, 5],
#           [2, 8, 3],
#           [3, 5, 6],
#           [4, 5, 7],
#           [5, 6, 8],
#           [6, 7, 9]]
# print(minEffort(puzzle))

def unbound_knapsack_recursive(items: list[tuple], x: int):
    if x == 0:
        return 0
    max_val = 0
    for i in items:
        weight, value = i
        if weight < x:
            max_val = max(max_val, value + unbound_knapsack_recursive(items, x-weight))
    return max_val

item_list = [(4,10),(9,25),(3,13),(5,20),(7,8)]
# print(unbound_knapsack_recursive(item_list, 11))


def unbound_knapsack_cache(w, n, items):
    cache = [0]*(w+1)

    for x in range(1, w + 1):

        for i in range(n):
            wi = items[i][1]
            if wi <= x:
                cache[x] = max(cache[x], cache[x - wi] + items[i][0])

    return cache[w]

def bounded_knapsack_bottomup(w, items):
    n = len(items)
    cache = [[(0, []) for _ in range(n+1)] for _ in range(w+1)]
    for x in range(1, w+1):
        for i in range(1, n+1):
            weight, value = items[i-1]
            cache[x][i] = cache[x][i-1]
            if weight <= x:
                cache[x][i] = (max(value + cache[x-weight][i-1][0], cache[x][i][0]), cache[x][i-1][1])
                if cache[x][i][0] == value + cache[x-weight][i-1][0]:
                    cache[x][i] = (cache[x][i][0], cache[x-weight][i-1][1] + [weight])

    return cache[w][n]


total_val, weights = bounded_knapsack_bottomup(20, item_list)
item_dict = dict(item_list)
final_dict = [{"Weight": key, "Value": item_dict[key]} for key in weights]
print(f"Total Value: {total_val}, With the items {final_dict}")


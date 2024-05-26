def max_independent_set(nums):
    if max(nums) < 0:
        return []
    if max(nums) == 0:
        return [0]
    n = len(nums)
    # Base case + 1 through n
    cache = [(0, [])] + [(0, [])] * n
    for i in range(1, n + 1):
        # For each number, if it is non-negative, check if previous (i-1) max is less than than (i-2) + current number
        if nums[i - 1] >= 0:
            if i == 1 or cache[i - 1][0] < cache[i - 2][0] + nums[i - 1]:
                cache[i] = (cache[i - 2][0] + nums[i - 1], cache[i - 2][1] + [nums[i - 1]])
            else:
                # If it is larger, bring previous forward
                cache[i] = cache[i - 1]
        else:
            # If negative, bring previous forward
            cache[i] = cache[i - 1]
    return cache[n][1]


# print(max_independent_set([7, 2, 0, 5, 0, 0, 8, 0, 6]))
# print(max_independent_set([-1, -1, 0]))
# print(max_independent_set([-1, -1, 1, 0, 0, 3, -2, 1]))
# print(max_independent_set([-1, -1, -10, -34]))

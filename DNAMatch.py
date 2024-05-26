# Program to Check matches in sequences in DNA.
# Has both top down and bottom up approaches.
# Made by Alex Clark (clarka8@oregonstate.edu)

def dna_match_topdown(DNA1, DNA2):
    if DNA1 == "" or DNA2 == "":
        return 0
    memo = {}
    # Use helper function to pass on i and j, and memoization
    return topdown_helper(DNA1, DNA2, len(DNA1), len(DNA2), memo)


def topdown_helper(DNA1, DNA2, i, j, memo):
    max_val = 0
    # Check if this spot has already been calculated
    if (i, j) in memo:
        return memo[(i, j)]
    if i == 0 or j == 0:
        memo[(i, j)] = 0
        return 0
    if DNA1[i - 1] == DNA2[j - 1]:
        max_val = 1 + topdown_helper(DNA1, DNA2, i-1, j-1, memo)
    else:
        max_val = max(topdown_helper(DNA1, DNA2, i, j-1, memo), topdown_helper(DNA1, DNA2, i-1, j, memo))
    # Save value to memo, so it can be checked later to save time
    memo[(i, j)] = max_val
    return max_val

def dna_match_bottomup(DNA1, DNA2):
    if DNA1 == "" or DNA2 == "":
        return 0
    n = len(DNA1)
    m = len(DNA2)
    cache = [[0 for x in range(m + 1)] for x in range(n + 1)]
    # Fill cache of values
    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                cache[i][j] = 0
            elif DNA1[i - 1] == DNA2[j - 1]:
                cache[i][j] = cache[i - 1][j - 1] + 1
            else:
                cache[i][j] = max(cache[i - 1][j], cache[i][j - 1])
    return cache[n][m]

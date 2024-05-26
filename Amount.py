# Given a collection of amount values (A) and a target sum (S), find all unique combinations in A
# where the amount values sum up to S. Return these combinations in the form of a list.
# Each amount value may be used only the number of times it occurs in list A. The solution set should not contain
# duplicate combinations. Amounts will be positive numbers. Return an empty list if no possible solution exists.
# Example: A = [11,1,3,2,6,1,5]; Target Sum = 8
# Result = [[3, 5], [2, 6], [1, 2, 5], [1, 1, 6]]


def amount(a, s):
    combinations = []
    a.sort()
    backtrack_amount(combinations, a, s, [], 0, 0)
    return combinations


def backtrack_amount(combos, a, s, current_set, set_sum, n):
    if set_sum > s:
        return
    if set_sum == s:
        combos.append(current_set[:])  # Append a copy of the current set
        return
    for i in range(n, len(a)):
        if i > n and a[i] == a[i - 1]:
            continue
        current_set.append(a[i])
        backtrack_amount(combos, a, s, current_set, set_sum + a[i], i + 1)
        current_set.pop()


# print(amount([11, 1, 3, 2, 6, 1, 5], 8))

def kthElement(l1: list, l2: list, k: int) -> int:
    n1 = len(l1)
    n2 = len(l2)

    # Base cases for end of recursion
    if n1 == 0:
        return l2[k - 1]
    if n2 == 0:
        return l1[k - 1]

    # Middle values
    mid1 = n1 // 2
    mid2 = n2 // 2

    # Find what should be the halfway in the larger sorted array
    half = mid1 + mid2 + 1

    # Compare middle values and decide which part of the arrays to eliminate. Similar to using a binary search
    if l1[mid1] <= l2[mid2]:
        if k <= half:
            return kthElement(l1, l2[:mid2], k)
        else:
            return kthElement(l1[mid1 + 1:], l2, k - (mid1 + 1))
    else:
        if k <= half:
            return kthElement(l1[:mid1], l2, k)
        else:
            return kthElement(l1, l2[mid2 + 1:], k - (mid2 + 1))
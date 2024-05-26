from binarytree import Node

def powerset_helper(input_set, subset, i, power_set, parent):
    if i >= len(input_set):
        # No more sets to look at
        power_set.append(subset[:])
        return
    subset.append(input_set[i])
    parent.left = Node(str(subset) + " Added " + str(input_set[i]))
    powerset_helper(input_set, subset, i + 1, power_set, parent.left)
    # Include element i and move on
    subset.pop()
    parent.right = Node(str(subset))
    powerset_helper(input_set, subset, i + 1, power_set, parent.right)
    # Remove element i and move on


def powerset(input_set):
    power_set = []
    root = Node(str(power_set))
    powerset_helper(input_set, [], 0, power_set, root)
    print(root)
    return power_set

#
print(powerset([1, 2, 3]))
print(powerset([]))

def block_puzzle(length):
    count_table = [0] * (length + 1)
    count_table[0] = 1  # setting the base case

    if length >= 1:
        count_table[1] = 1

    for i in range(2, length + 1):  # iterate through all possible amount values from base case
        count_table[i] = count_table[i - 1] + count_table[i-2]
    return count_table[length]


print(block_puzzle(5))


def find_ways(n, current_length=0, count=[0]):
    # If the current length is exactly equal to n, increment the counter
    if current_length == n:
        count[0] += 1
        return

    # If the current length exceeds n, stop the recursion
    if current_length > n:
        return

    # Try adding a block of length 1
    find_ways(n, current_length + 1, count)
    # Try adding a block of length 2
    find_ways(n, current_length + 2, count)

    return count[0]


# Test the function with a sample value of N
N = 5
result = find_ways(N)
print(f"The number of distinct ways to arrange blocks for length {N} is: {result}")

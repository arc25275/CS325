def permutations_backtracking(result: str, string: str):
    if len(string) == 0:
        print(result)
    for letter in string:
        permutations_backtracking(result + letter, string.replace(letter, ""))

permutations_backtracking("","ABCD")

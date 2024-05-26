def n_queens(n):
    board = [[0 for x in range(n)] for x in range(n)]
    solve_n_queens(board, 0, n, n)
    return board


def solve_n_queens(board, row, n, remaining):
    if remaining == 0:
        return True
    for col in range(n):
        if not is_attacked(row, col, board, n):
            board[row][col] = 1
            if solve_n_queens(board, row+1, n, remaining-1):
                return True
            board[row][col] = 0
    return False


def is_attacked(row, col, board, n):
    for i in range(n):
        # Row
        if board[row][i] == 1:
            return True
        # Column
        if board[i][col] == 1:
            return True
        # Diagonal Up Right
        if row + i < n and col + i < n and board[row + i][col + i] == 1:
            return True
        # Diagonal Down Right
        if row - i >= 0 and col - i >= 0 and board[row - i][col - i] == 1:
            return True
    return False


for row in n_queens(6):
    print(row)

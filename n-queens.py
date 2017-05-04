
n = 12

def try_queen(n, board, col):
    count = 0
    for line in range(n):
        board[col] = line
        if verify(board, col):
            if col + 1 == n:
                count += 1
            else:
                count += try_queen(n, board, col + 1)
    return count

def verify(all_board, col):
    # all on distinct lines
    board = all_board[:col+1]
    if len(set(board)) < len(board):
        return False
    last_line, last_col = len(board) - 1, board[-1]
    # all on distinct diagonals
    for line, col in enumerate(board[:-1]):
        if abs(last_line - line) == abs(last_col - col):
            return False
    return True

board = [None] * n
count = try_queen(n, board, 0)
print count


from __future__ import print_function

from multiprocessing import Pool

n = 12

def try_queen(n, board):
    count = 0
    for line in range(n):
        if verify(board + [line]):
            if len(board) + 1 == n:
                count += 1
            else:
                count += try_queen(n, board + [line])
    return count

def verify(board):
    # all on distinct lines
    if len(set(board)) < len(board):
        return False
    last_line, last_col = len(board) - 1, board[-1]
    # all on distinct diagonals
    for line, col in enumerate(board[:-1]):
        if abs(last_line - line) == abs(last_col - col):
            return False
    return True

if __name__ == '__main__':
    with Pool(2) as pool:
        results = [pool.apply_async(try_queen, (n, [line])) for line in range(n)]
        count = sum(res.get() for res in results)
        print(count)


#!/usr/bin/env python3

from __future__ import print_function
from multiprocessing import Pool
import sys

# board structure is represented as an array
# column = index
# line = board[index]

def try_queen(n, board):
    count = 0
    for line in range(n):
        board_new_queen = board + [line]
        if verify(board_new_queen):
            if len(board_new_queen) == n:
                count += 1
            else:
                count += try_queen(n, board_new_queen)
    return count

def verify(board):
    last_line, last_col = board[-1], len(board) - 1
    # all on distinct lines
    if len(set(board)) < len(board):
        return False
    # all on distinct diagonals
    for col, line in enumerate(board[:-1]):
        if abs(last_line - line) == abs(last_col - col):
            return False
    return True

if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 8
    with Pool(2) as pool:
        results = [pool.apply_async(try_queen, (n, [line])) for line in range(n)]
        count = sum(res.get() for res in results)
        print(count)


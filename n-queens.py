from __future__ import print_function

from multiprocessing import Process, Queue

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

def run_and_return_to_queue(q, f, *args):
    ret = f(*args)
    q.put(ret)

process_list = []
q = Queue()

for line in range(n):
    board = [line]
    p = Process(target=run_and_return_to_queue, args=(q, try_queen, n, board))
    p.start()
    process_list.append(p)

for p in process_list: 
    p.join()

count = 0
while not q.empty():
    count += q.get()
print(count)


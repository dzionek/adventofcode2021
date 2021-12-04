import numpy as np

AOC_DAY = 4

def is_board_finished(board: np.ndarray) -> bool:
    return is_row_finished(board) or is_column_finished(board)

def is_row_finished(board: np.ndarray) -> bool:
    return any(all(row) for row in board)

def is_column_finished(board: np.ndarray) -> bool:
    return any(all(col) for col in board.T)

def sum_of_unmarked(marked_board: np.ndarray, board: np.ndarray) -> int:
    return sum([
        board[j, z]
        for j in range(5) for z in range(5)
        if not marked_board[j, z]
    ])


with open(f'inputs/{AOC_DAY:02}.txt') as f:
    data = f.read().splitlines()

numbers = map(int, data[0].split(','))

boards = np.array([
    [[int(n) for n in line.split()] for line in data[i:i+5]]
    for i in range(2, len(data), 6)
])

first_finished = False
last_finished = None
marked = np.zeros((len(boards), 5, 5), dtype=bool)
not_win = set(range(len(boards)))

for n in numbers:
    for i in range(len(boards)):
        for j in range(5):
            for z in range(5):
                if boards[i, j, z] == n:
                    marked[i, j, z] = True

    new_not_win = set()
    for nw in not_win:
        if is_board_finished(marked[nw]):
            # Part 1
            if not first_finished:
                print(sum_of_unmarked(marked[nw], boards[nw]) * n)
                first_finished = True
            last_finished = nw
        else:
            new_not_win.add(nw)
    not_win = new_not_win

    # Part 2
    if not not_win:
        print(sum_of_unmarked(marked[last_finished], boards[last_finished]) * n)
        break

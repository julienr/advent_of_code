import numpy as np
import sys

boards = []
draw_order = []

with open('input') as f:
    draw_order = [int(c) for c in f.readline().split(',')]

    for line in f:
        if line.strip() == '':
            # Start new board
            board = np.zeros([5, 5], dtype=np.int32)
            for i in range(5):
                line = f.readline()
                row = np.array([int(c) for c in line.rsplit(' ') if c != ''])
                board[i, :] = row
            boards.append(board)

marks = [np.zeros((5, 5), dtype=np.bool) for board in boards]

def check_number(number, board, mark):
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            if board[i, j] == number:
                mark[i, j] = True

    # Check win status
    for i in range(board.shape[0]):
        if np.all(mark[i]):
            return True
    for j in range(board.shape[1]):
        if np.all(mark[:, j]):
            return True
    return False


def score(number, board, mark):
    score = 0
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            if not mark[i, j]:
                score += board[i, j]
    score *= number
    return score


winning_boards = []
won = np.zeros(len(boards), dtype=np.bool)

for number in draw_order:
    for i, board in enumerate(boards):
        if won[i]:
            continue
        if check_number(number, board, marks[i]):
            board_score = score(number, board, marks[i])
            winning_boards.append((i, board_score))
            won[i] = True

print(winning_boards[-1])


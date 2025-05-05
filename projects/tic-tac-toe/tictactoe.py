import math
import copy

X = "X"
O = "O"
EMPTY = None

def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    return X if x_count == o_count else O

def actions(board):
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY}

def result(board, action):
    if board[action[0]][action[1]] != EMPTY:
        raise Exception("Invalid action")

    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player(board)
    return new_board

def winner(board):
    # Rows
    for row in board:
        if row[0] is not None and row.count(row[0]) == 3:
            return row[0]

    # Columns
    for col in range(3):
        if board[0][col] is not None and \
           board[0][col] == board[1][col] == board[2][col]:
            return board[0][col]

    # Diagonals
    if board[0][0] is not None and \
       board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] is not None and \
       board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]

    return None

def terminal(board):
    return winner(board) is not None or all(cell is not EMPTY for row in board for cell in row)

def utility(board):
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0

def minimax(board):
    if terminal(board):
        return None

    current = player(board)

    if current == X:
        value, move = max_value(board)
    else:
        value, move = min_value(board)
    return move

def max_value(board):
    if terminal(board):
        return utility(board), None

    v = -math.inf
    best_move = None
    for action in actions(board):
        min_result, _ = min_value(result(board, action))
        if min_result > v:
            v = min_result
            best_move = action
    return v, best_move

def min_value(board):
    if terminal(board):
        return utility(board), None

    v = math.inf
    best_move = None
    for action in actions(board):
        max_result, _ = max_value(result(board, action))
        if max_result < v:
            v = max_result
            best_move = action
    return v, best_move
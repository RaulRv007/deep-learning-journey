from tictactoe import player, actions, result, terminal, winner, utility, minimax
X = "X"
O = "O"
EMPTY = None
board = [[X, EMPTY, EMPTY],
         [EMPTY, EMPTY, EMPTY],
         [EMPTY, EMPTY, EMPTY]]
'''print(player(board))
print(actions(board))
print(result(board, (0, 1)))
print(terminal(board))
print(winner(board))
print(utility(board))'''
print(minimax(board))


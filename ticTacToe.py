"""
a 3*3 board which we can play on
[
    ['O', 'X', '-']
    ['X', 'O', '-']
    ['-', 'X', 'O']
]
each element in the list of lists represents a square in our game board
each element needs to be able to be on three states: X, O, or -
"""


def new_board():
    return [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
#create an instance of the board
game_board = new_board()

def print_board(board):
    #format columns for board readibility and ease of play
    print("  1 2 3")
    i = 1
    for row in board:
        print(str(i) + " ", end="")
        print(*row)
        i += 1

class player:
    def __init__(self, player_piece):
        self.player_piece = player_piece
    """""
    def get_move(self):
        y = input("Enter your move's Y coordinate: ")
        x = input("Enter your move's X coordinate: ")
        game_board[x][y] = self.player_piece
        print_board(game_board)
    """

def get_move(player_piece):
    X = int(input("Enter your move's X coordinate: "))
    Y = int(input("Enter your move's Y coordinate: "))
    execute_move(X, Y, player_piece)

def execute_move(X, Y, player_piece):
    game_board[Y-1][X-1] = player_piece
    print_board(game_board)

player1 = player("X")
player2 = player("O")

print("Welcome to Tic-Tac-Toe")
print("Player one will use the 'X' piece")
print("Player two will use the 'O' piece")
print_board(game_board)

#test case
get_move(player1.player_piece)






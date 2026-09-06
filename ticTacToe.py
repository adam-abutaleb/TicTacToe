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

def get_move(board, player_piece):
    while True:
        if player_piece == 'X':
            print("Player one: ")
        else :
            print("Player two: ")
        try:
            X = int(input("Enter your move's X coordinate: "))
            Y = int(input("Enter your move's Y coordinate: "))
        except ValueError: #handles non-int inputs
            print("That is not a valid coordinate. Please enter digits 1-3 only.")
            #reprint the game board
            print_board(board)
            continue

        if X not in (1, 2, 3) or Y not in (1, 2, 3): #handles int inputs outside the range of the board
            print("That is not a valid coordinate. Please enter digits 1-3 only.")
            #reprint the game board
            print_board(board)
            continue

        if board[Y-1][X-1] != '-': #handles input where there is already a piece
            print("That square is already taken.")
            #reprint the game board
            print_board(board)
            continue

        execute_move(board, X, Y, player_piece)
        break

def execute_move(board, X, Y, player_piece):
    board[Y-1][X-1] = player_piece
    print_board(board)

def is_board_full(board):
    for row in board:
        for col in row:
            if col == '-':
                return False
    else:
        return True

def get_winner(board):
    pass

#tic-tac-toe keeps playing until; the board has no more spaces, or there is three in a row
#I will use a while loop that will run until either of these conditions are met

def play_game():
    player1 = player("X")
    player2 = player("O")
    print("Welcome to Tic-Tac-Toe")
    print("Player one will use the 'X' piece")
    print("Player two will use the 'O' piece")
    print_board(game_board)
    player_turn = 0
    while True:
        if player_turn == 0:
            get_move(game_board, player1.player_piece)
            player_turn = 1
        else:
            get_move(game_board, player2.player_piece)
            player_turn = 0
        if is_board_full(game_board):
            print("IT'S A DRAW!")
            break


play_game()
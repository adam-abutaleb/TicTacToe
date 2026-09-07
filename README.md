
# Tic-Tac-Toe (Terminal)
 
A two-player Tic-Tac-Toe game played entirely in the terminal. Built as a self-taught Python project to practice core programming fundamentals: 2D data structures, input validation, and win-condition logic.
 
## How It Works
 
- The board is represented as a 3x3 list of lists, with each cell holding `'X'`, `'O'`, or `'-'`.
- Players take turns entering the X and Y coordinates (1–3) of the square they want to play.
- After each move, the board reprints so both players can see the current state.
- The game checks for a winner after every move by scanning all rows, columns, and both diagonals, and checks for a draw when the board fills up with no winner.
## Input Validation
 
The game guards against the ways a player can break it:
- Non-numeric input (e.g. typing a letter instead of a coordinate)
- Coordinates outside the 1–3 range
- Selecting a square that's already taken
In each case, the player is prompted again instead of crashing the program.
 
## Running It
 
Requires Python 3. No external dependencies.
 
```bash
python ticTacToe.py
```
 
Player one plays `X`, player two plays `O`. Enter your move as an X coordinate (column) followed by a Y coordinate (row), both between 1 and 3.
 
## Possible Improvements
 
- Add a single-player mode with a computer opponent 
- Replace coordinate input with a numbered-square format (1–9) for faster play

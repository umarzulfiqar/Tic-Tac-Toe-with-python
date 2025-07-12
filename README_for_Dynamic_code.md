<h1></h1>


`main.py` Primary file
`main()`

-> Steps:

1. Inquires the player for board measure utilizing `check_board_initial_value()`.
2. Initializes the `tictactoe` amusement with that size.
3. Loops:

-> Shows the board utilizing `print_board()`.
-> Gets player move through `get_player_move()`.
-> Tries to apply the move with `make_move()`.
-> Checks for win with `evaluation()`, or draw with `is_draw()`.
-> Inquires for replay in the event that the amusement ends.
-> Switches to the following player otherwise.
 
________________________________________________________________________________________________________________________________________________

`tictactoe_logics.py` Business Logics File

`__init__(self, g_size)`

-> Initializes the game:
-> Sets board size
-> Makes an purge board (2D list)
-> Sets the current player to `"X"`
-> Tracks number of moves and max moves

`make_move(self, push, col)`

-> Places the current player's image at `(row, col)`
-> Raises an mistake in the event that the cell is as of now taken
-> Increases the move counter

`evaluation(self)`

-> Checks for a win condition:
-> All cells in any push are the same
-> All cells in any column are the same
-> All cells in either corner to corner are the same
-> Returns `True` on the off chance that the current player has won

`is_draw(self)`

-> Returns `True` if the overall number of moves breaks even with the whole number of cells â meaning the board is full and no winner

`switch_player(self)`

-> Switches the current player from `"X"` to `"O"` or bad habit versa

`get_board(self)`

-> Returns the current state of the board

### `get_current_player(self)`

-> Returns which player's turn it is

_________________________________________________________________________________________________________________________________________________

`ui.py` User Interface File

`print_board(board, g_size)`

-> Shows the board push by row
-> Includes push file and even dividers for clarity

`get_player_move(currentplayer, g_size)`

-> Prompts the current player to enter push and column
-> Approves input:
-> Precisely two values
-> Inside substantial range
-> Returns `(row, col)` on the off chance that input is valid

`ask_replay()`

-> Inquires the client in case they need to play again
-> Returns `True` on the off chance that the reply is `'y'`, else `False`

`check_board_initial_value()`

-> Inquires the client to enter a substantial board measure (must be >1)
-> Re-prompts on the off chance that input is invalid
-> Returns the approved board estimate as an integer
________________________________________________________________________________________________________________________
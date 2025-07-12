def print_board(board, g_size):
    index_count = 0
    for row in board:
        print(index_count, " | ".join(row))
        print("-" * 4 * g_size)
        index_count += 1

def get_player_move(currentplayer, g_size):
    while True:
        try:
            move = input(f"Player {currentplayer} (row and column: 0 1): ").split()
            if len(move) != 2:
                raise ValueError("Enter two numbers separated by a space.")
            row, col = map(int, move)

            if row not in range(g_size) or col not in range(g_size):
                raise ValueError(f"Row and column must be 0 to {g_size - 1}")
            return row, col
        except ValueError as e:
            print("Invalid input:", e)

def ask_replay():
    again = input("Do you want to play again? (yes->'y' | no->'n'): ")
    return again.lower() == 'y'

def check_board_initial_value():
    while True:
        try:
            val=int(input("Value for board: "))
            if val<=0 or val==1:
                raise ValueError("Enter value grater than 0 and 1.")
            return val
        except ValueError as e:
            print("Invalid value",e)
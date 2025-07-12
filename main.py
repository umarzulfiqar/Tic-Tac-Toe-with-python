from tictactoe_logics import tictactoe
from ui import print_board, get_player_move, ask_replay,check_board_initial_value

def main():
    g_size = check_board_initial_value()
    game = tictactoe(g_size)

    while True:
        print_board(game.get_board(), g_size)
        row, col = get_player_move(game.get_current_player(), g_size)

        try:
            game.make_move(row, col)
        except ValueError as e:
            print(e)
            continue

        if game.evaluation():
            print_board(game.get_board(), g_size)
            print(f"Player {game.get_current_player()} wins the game.")
            if ask_replay():
                main()
            return

        if game.is_draw():
            print_board(game.get_board(), g_size)
            print("Game Draw.")
            if ask_replay():
                main()
            return

        game.switch_player()

if __name__ == "__main__":
    main()
class tictactoe:
    def __init__(self,g_size):
        self.g_size = g_size
        self.board = [[" " for _ in range(g_size)] for _ in range(g_size)]
        self.currentplayer = "X"
        self.move = 0
        self.max_moves = g_size * g_size

    def print_board(self):
        index_count= 0
        for row in self.board:
            print(index_count," | ".join(row))
            print("-" * 4 * self.g_size)
            index_count+=1


    def get_player_move(self):
        while True:
            try:
                move = input(f"Player {self.currentplayer} (row and column: 0 1): ").split()
                if len(move) != 2:
                    raise ValueError("Enter two numbers separated by a space.")
                row, col = map(int, move)

                if row not in range(self.g_size) or col not in range(self.g_size):
                    raise ValueError("Row and column must be 0 to",self.g_size)
                if self.board[row][col] != " ":
                    raise ValueError("That spot is already taken.")
                return row, col
                
            except ValueError as e:
                print("Invalid input:", e)

    def evaluation(self):
        #check for row
        for row in self.board:
            if all(cell==self.currentplayer for cell in row):
                return True
            

        #check for column
        for col in range(self.g_size):
            if all(self.board[row][col]==self.currentplayer for row in range(self.g_size)):
                return True
            

        #check for diagonals
        if all(self.board[i][i] == self.currentplayer for i in range(self.g_size)):
            return True
        if all(self.board[i][self.g_size - 1 - i] == self.currentplayer for i in range(self.g_size)):
            return True
        
        else:
            return False
        
    def play_turn(self):
        row, col = self.get_player_move()
        self.board[row][col] = self.currentplayer
        self.move += 1

    def switch_player(self):
        self.currentplayer = "O" if self.currentplayer == "X" else "X"

    def is_draw(self):
        return self.move == self.max_moves



def main():
    g_size = int(input("The size of table: "))
    game = tictactoe(g_size)

    while True:
        game.print_board()
        game.play_turn()

        if game.evaluation():
            game.print_board()
            print(f"Player {game.currentplayer} wins the game.")
            again = input("Do you want to play again? (yes->'y' | no->'n'): ")
            if again.lower() == 'y':
                main()
            else:
                return

        if game.is_draw():
            game.print_board()
            print("Game Draw.")
            again = input("Do you want to play again? (yes->'y' | no->'n'): ")
            if again.lower() == 'y':
                main()
            else:
                return

        game.switch_player()

if __name__ == "__main__":
    main()

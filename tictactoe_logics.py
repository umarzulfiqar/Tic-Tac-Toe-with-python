class tictactoe:
    def __init__(self,g_size):
        self.g_size = g_size
        self.board = [[" " for _ in range(g_size)] for _ in range(g_size)]
        self.currentplayer = "X"
        self.move = 0
        self.max_moves = g_size * g_size

    def make_move(self,row,col):
        if self.board[row][col] != " ":
            raise ValueError("This spot is taken.")
        self.board[row][col] = self.currentplayer
        self.move+=1

    def evaluation(self):
        #check for row
        for row in self.board:
            if all(cell == self.currentplayer for cell in row):
                return True
        #check for column
        for col in range(self.g_size):
            if all(self.board[row][col] == self.currentplayer for row in range(self.g_size)):
                return True
        #check for diagonal
        if all(self.board[i][i] == self.currentplayer for i in range(self.g_size)):
            return True
        if all(self.board[i][self.g_size - 1 - i] == self.currentplayer for i in range(self.g_size)):
            return True

        return False
    
    def is_draw(self):
        return self.move == self.max_moves
    
    def switch_player(self):
        self.currentplayer = "O" if self.currentplayer == "X" else "X"

    def get_board(self):
        return self.board
    
    def get_current_player(self):
        return self.currentplayer
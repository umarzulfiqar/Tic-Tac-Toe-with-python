def print_board(board):
    
    index_count= 0
    for row in board:
        print(index_count," | ".join(row))
        print("-" * 15)
        index_count+=1

def get_player_move(player, board):
    while True:
        try:           #Error handling
            move = input(f"Player {player} (row and column: 0 1): ").split()   #Use to split string and add into list
            if len(move) != 2:
                raise ValueError("Enter two numbers separated by a space.")
            row, col = map(int, move)                                          #Use to perform function or each iteration

            if row not in range(3) or col not in range(3):
                raise ValueError("Row and column must be 0 ,1 to 2")
            if board[row][col] != " ":
                raise ValueError("That spot is already taken.")

            return row, col
        except ValueError as e:     #catch error and give output
            print("Invalid input:", e)


def evaluation(board,player):
    #check for row
    for row in board:
        if all(cell==player for cell in row):
            return True
            

    #check for column
    for col in range(3):
        if all(board[row][col]==player for row in range(3)):
            return True
            

    #check for diagonals
    if all(board[i][i] == player for i in range(3)):
            return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
        
    else:
        return False




def main():
    
    board = [[" " for row in range(3)] for column in range(3)]
    currentplayer = "X"
    move=0

    while move < 9:
        print_board(board)
        row,col= get_player_move(currentplayer,board)
        board[row][col]= currentplayer
        move+=1

        if evaluation(board,currentplayer):
            print_board(board)
            print(f"Player {currentplayer} wins the game.")
            return
    
        currentplayer = "O" if currentplayer == "X" else "X"


    print_board(board)
    print("Game Draw.")


if __name__ == "__main__":
    main()
def print_board(board,g_size):
    
    index_count= 0
    for row in board:
        print(index_count," | ".join(row))
        print("-" * 4 * g_size)
        index_count+=1


def get_player_move(player, board,g_size):
    while True:
        try:
            move = input(f"Player {player} (row and column: 0 1): ").split()
            if len(move) != 2:
                raise ValueError("Enter two numbers separated by a space.")
            row, col = map(int, move)

            if row not in range(g_size) or col not in range(g_size):
                raise ValueError("Row and column must be 0 to",g_size)
            if board[row][col] != " ":
                raise ValueError("That spot is already taken.")

            return row, col
        except ValueError as e:
            print("Invalid input:", e)

def evaluation(board,player,g_size):
    #check for row
    for row in board:
        if all(cell==player for cell in row):
            return True
            

    #check for column
    for col in range(g_size):
        if all(board[row][col]==player for row in range(g_size)):
            return True
            

    #check for diagonals
    if all(board[i][i] == player for i in range(g_size)):
            return True
    if all(board[i][g_size - 1 - i] == player for i in range(g_size)):
        return True
        
    else:
        return False



def main():
    input_row=int(input("The size of table: "))
    board = [[" " for _ in range(input_row)] for _ in range(input_row)]
    currentplayer="X"
    move=0

    while move < 2 * input_row:
        print_board(board,input_row)
        row,col= get_player_move(currentplayer,board,input_row)
        board[row][col]= currentplayer
        move+=1

        if evaluation(board,currentplayer,input_row):
            print_board(board,input_row)
            print(f"Player {currentplayer} wins the game.")
            again=input("Do you want to play again? (yes->'y' | no->'n') ")
            if again=='y':
                main()
            else:
                return
    
        currentplayer = "O" if currentplayer == "X" else "X"


    print_board(board,input_row)
    print("Game Draw.")

    again=input("Do you want to play again? (yes->'y' | no->no)")
    if again=='y':
        main()
    else:
        return

if __name__ == "__main__":
    main()

#Board for testing
# row=int(input("Enter no of rows: "))
# board = [[" " for _ in range(row)] for _ in range(row)]
# print_board(board,row)

# #test move
# player = "X"
# row, col = get_player_move(player, board,row)
# board[row][col] = player
# print_board(board,row)
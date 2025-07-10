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



#Board for testing
board = [[" " for row in range(3)] for column in range(3)]
print_board(board)

#Test move 
player = "X"
row, col = get_player_move(player, board)             #get 2 diamenstion value from function
board[row][col] = player                              #change index[i][i] with player Name
print_board(board)
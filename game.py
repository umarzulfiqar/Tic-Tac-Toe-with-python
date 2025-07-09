def print_board(board):
    
    index_count= 0
    for row in board:
        print(index_count," | ".join(row))
        print("-" * 15)
        index_count+=1


#Board for testing
board = [[" " for _ in range(3)] for _ in range(3)]
print_board(board)
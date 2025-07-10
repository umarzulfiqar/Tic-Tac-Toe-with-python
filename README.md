# Tic-Tac-Toe-with-python
Tic Tac Toe with Hard code 3x3

I divide my game into 4 steps:

    1). Make the board for player
    2). Take input from user (location).
    3). Looping step 3 and switching player and Evaluation Function
    4). Gather every function in main() and call it.

Explaination of 1st step: 
For loop used for for pinting the board, our function takes the arugment 'board' in which we pass 'row and column' of our board
In our case our row and columns are 3x3. We run our loop for row in range and for column in range. I also use join() method in print_board function which
which convert my list 'board[]' into single string.


Explaination of 2nd step:
I in this step i take input fro user (insert location) and check for errors with error handling technique I run while loop for make the program in runiing 
untill i did not get output of (row and column) if error occures than it raise the error message which the specific condition checking.

Rules for entering values: Value should be in the range of 0 to 3 means (0,1,2) and seprated my space. and our split() function take the move value and
split it, which means take string and add into single list. By default my player value is 'X'.



Explaination of 3rd step:
I use while loop with condition <9 because the loop have to have 0 to 8 to fill total 9 cells.
The Evaluation function check or everytime user/player enter the location of its turn because in any postion'player' it will return the value.

In this step i make evaluation function in which each row,column and diagonal entities checked with the help of condition and return the player who won or 
match draw. I take arrguments 'board and current player' and check or each row of board, column of board and diagonal entites of board. If nothing happen
true in this conditions than this function will return 'False' or Evaluation()


Explaination of 4th setep:
I define main function in which i call all my functions along with loop and return statment.
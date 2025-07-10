# Tic-Tac-Toe-with-python
I divide my game into 4 steps:

    1). Make the board for player
    2). Take input from user (location).
    3). Looping step 3 and switching player
    4). Check for winner or match draw.

Explaination of 1st step: 
For loop used for for pinting the board, our function takes the arugment 'board' in which we pass 'row and column' of our board
In our case our row and columns are 3x3. We run our loop for row in range and for column in range. I also use join() method in print_board function which
which convert my list 'board[]' into single string.


Explaination of 2nd step:
I in this step i take input fro user (insert location) and check for errors with error handling technique I run while loop for make the program in runiing 
untill i did not get output of (row and column) if error occures than it raise the error message which the specific condition checking.

Rules for entering values: Value should be in the range of 0 to 3 means (0,1,2) and seprated my space. and our split() function take the move value and
split it, which means take string and add into single list. By default my player value is 'X'.
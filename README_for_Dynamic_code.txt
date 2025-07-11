Initally I use such type of approch in which i can use dynamic approch as well.
I just have to take input from user and in print_board(board,g_size) for loop will print acooriding to the size
of user input.

In next function get_player_move() it will take the input 'g_size' and get input according to input and boar size.
Check for conditions and allow or deny user to add currentplayer value at specific place.

In evaluation() this function will also get 'g_size' along with player and board (2 diamenstion) and check for row,column and diagonal entities
and return the value for row,column and diagonal

I have change make little changes and make my game in a class and seprate bussiness logic according to me.
create class tictactoe and initilize it with constructor along with values self,g_size

I add 3 new functions in class which was prviously in the main function.
1-> player_turn() this function takes values of row and column from get_player_move function and update the table and increment in move.
2-> switch_player which is simpply work on if else statment
3-> is_draw() this function check if move value is equal to max move if yes this will call.
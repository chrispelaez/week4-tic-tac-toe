def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
    # TO DO #################################################################
    # Write code in this function that prints the game board.               #
    # The code in this function should only print, the user should NOT      #
    # interact with this function in any way.                               #
    #                                                                       #
    # Hint: you can follow the same process that was done in the textbook.  #
    #########################################################################

def checkWinner(board, player):    
    print('Checking if ' + player + ' is a winner...')
    
    return ((board['top-L'] == player and board['top-M'] == player and board['top-R'] == player) or # Checking the top row(horizontal)
            (board['mid-L'] == player and board['mid-M'] == player and board['mid-R'] == player) or #Checking the middle row(horizontal)
            (board['low-L'] == player and board['mid-M'] == player and board['mid-R'] == player) or # checking  the bottom(horizontal)
            (board['top-L'] == player and board['mid-L'] == player and board['low-L'] == player) or # Checking the down left side(vertical)
            (board['top-M'] == player and board['mid-M'] == player and board['low-M'] == player) or # Checking the down middle(vertical)
            (board['top-R'] == player and board['mid-R'] == player and board['low-R'] == player) or # checking the down right side(vertical)
            (board['top-L'] == player and board['mid-M'] == player and board['low-R'] == player) or # checking diagonal left to right 
            (board['top-R'] == player and board['mid-M'] == player and board['low-L'] == player))   # checking the diagonal right to left(inverted)
            
    
    # TO DO #################################################################
    # Write code in this function that checks the tic-tac-toe board          #
    # to determine if the player stored in variable 'player' currently      #
    # has a winning position on the board.                                  #
    # This function should return True if the player specified in           #
    # variable 'player' has won. The function should return False           #
    # if the player in the variable 'player' has not won.                   #
    #########################################################################
    
    
def startGame(startingPlayer, board):
    # TO DO #################################################################
    # Add comments to each line in this function to describe what           #
    # is happening. You do not need to modify any of the Python code        #
    #########################################################################

    turn = startingPlayer
    for i in range(9): 
        printBoard(board) # function used to print the tictactoe board
        print('Turn for ' + turn + '. Move on which space?') # used to ask player X or O to pick a space
        move = input() # ask's player to input their move
        board[move] = turn # counts players move as their turn
        if( checkWinner(board, 'X') ): #Function used to determin if player X is winning.
            print('X wins!') # informs the players that X has won.
            break # program ends when player X is the winner.
        elif ( checkWinner(board, 'O') ): # if X does not win program checks to see if O is the winner.
            print('O wins!') # Informs the players that O is the winner
            break # program ends when O is the winner
    
        if turn == 'X': # Player X has the first turn 
            turn = 'O' # Player O has the second turn
        else:
            turn = 'X' # operation inverse if player O goes first then player X is second
        
    printBoard(board)
    

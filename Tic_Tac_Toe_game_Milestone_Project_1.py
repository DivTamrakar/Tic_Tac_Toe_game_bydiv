from IPython.display import clear_output

##DISPLAY BOARD---------->>>>>>>

def display_board(board):
    clear_output()
    print(board[7]+' | '+board[8]+' | '+board[9])
    print('  |   |')
    print('---------')
    print(board[4]+' | '+board[5]+' | '+board[6])
    print('  |   |')
    print('---------')
    print(board[1]+' | '+board[2]+' | '+board[3])
    print('  |   |')

test_board = ['#','X','O','X','O','X','O','X','O','X']



## PLAYER INPUT-------->>>>>>>

def player_input():
    '''
    OUTPUT =('Player1 Marker, Player2 Marker')
    '''
    marker =''
    
    while not (marker =='X' or marker =='O'):
        marker = input('Player1:Choose X or O: ').upper()
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')



## PLAYER MARKER------>>>>>

def place_marker(board, marker, position):
    board[position] = marker  



## WIN CHECK------------>>>>>>>

def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the left side
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

win_check(test_board,'O')    
     


## Randomly decide which player goes first------->

import random

def choose_first():
    flip=random.randint(0,1)
    if flip == 0:
        return 'Player1'
    else:
        return 'Player2'


## Returns a boolean indicating whether a space on the board is freely available ------>>>>

def space_check(board, position):
    
    return board[position] == ' '


## FULL BOARD CHECK --------->>>

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

## Function that asks for a player's next position ------>>>>>
#  Player  choice------->>>>>

def player_choice(board):
    
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('choose a position: (1-9)'))
    return position   


## Asks the player if they want to play again---------->>>>>
              
def replay():
    
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')



##----------------------------------------------------------------------------------------------------##


print('WELCOME TO TIC TAC TOE!!!')

while True:

    # Reset the board------------->>>>>>

    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
    

    ##GAME PLAY------------------>>>>>>>>

    while game_on:
        if turn == 'Player 1':

            # Player1's turn.--------->
            
            #SHow the board---->
            display_board(theBoard)
            #Choose a Position----->
            position = player_choice(theBoard)
            #Place the marker on the position---->
            place_marker(theBoard, player1_marker, position)


            #Check if the won--------->
            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:

            # Player2's turn.----------->>>>>
            
            #SHow the board---->
            display_board(theBoard)
            #Choose a Position----->
            position = player_choice(theBoard)
            #Place the marker on the position---->
            place_marker(theBoard, player2_marker, position)


            #Check if the won--------->
            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
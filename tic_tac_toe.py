import random
import os

# Clears output. Used between moves for a clean board.
def clear_output():
    os.system('cls' if os.name == 'nt' else 'clear')

# Displays the 3x3 game board with borders
def display_board(the_board):
    clear_output()
    print('Here is the board! ')
    print('_____________')
    print('|',the_board[1],'|',the_board[2],'|',the_board[3],'|')
    print('_____________')
    print('|',the_board[4],'|',the_board[5],'|',the_board[6],'|')
    print('_____________')
    print('|',the_board[7],'|',the_board[8],'|',the_board[9],'|')
    print('_____________')

# Allows user to choose X or O as the Player1 marker. Returns opposite choice for Player 2.
def player_input():

    marker = ''

    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose to be X or O: ').upper()

        if marker not in ['X','O']:
            print('Sorry, invalid choice, pick X or O! ')
    
    if marker == 'X':
        return ('X','O')

    else:
        return ('O','X')

# Uses randint to choose 0 or 1. 0 makes Player 1 go first, else Player 2 goes first.
def choose_first():

    flip = random.randint(0,1)

    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

# Checks if the space is already filled    
def space_check(the_board, position):

    return the_board[position] == ' '

# Checks if all positions on the board are filled. 
def full_board_check(the_board):
    
    for i in range(1,10):
        if space_check(the_board,i):
            return False

    return True

# Input function for player choice of a spot on the board. 
def player_choice(the_board):

    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(the_board,position):
        position = int(input('Choose a position: (1-9) '))

    return position

# Input funtion asking at teh end of a game if they wish to replay. Yes returns to the beginnnig of the overall While loop.
def replay():

    choice = input('Play again? Enter yes or no ').lower()

    return choice == 'yes'

# Function to place the choice on the board from the player_choice function.
def place_marker(the_board, marker, position):
    
    the_board[position] = marker

#checks for a win across rows, columns and diagonal. 
def win_check(the_board, marker):

    return ((the_board[1] == the_board[2] == the_board[3] == marker) or
    (the_board[4] == the_board[5] == the_board[6] == marker) or
    (the_board[7] == the_board[8] == the_board[9] == marker) or
    (the_board[1] == the_board[4] == the_board[7] == marker) or
    (the_board[2] == the_board[5] == the_board[8] == marker) or
    (the_board[3] == the_board[6] == the_board[9] == marker) or
    (the_board[1] == the_board[5] == the_board[9] == marker) or
    (the_board[3] == the_board[5] == the_board[7] == marker))

###FULL GAME LOGIC BELOW###
print('Welcome to Tic Tac Toe')

while True:

    #creates board tuple for players
    the_board = [' ']*10
    player1_marker,player2_marker = player_input()

    #sets who has the first turn
    turn = choose_first()
    print('Player 1 is: ' +player1_marker)
    print('Player 2 is: ' +player2_marker)
    print(turn+ ' will go first!')

    play_game = input('Ready to play? y or n ')

    if play_game == 'y':
        game_on = True
    else:
        game_on = False
    
    while game_on:
        if turn == 'Player 1':

            clear_output()
            display_board(the_board)
            position = player_choice(the_board)

            place_marker(the_board,player1_marker,position)

            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('Player 1 has won!!!')
                game_on = False
            
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie Game!')
                    game_on = False
                else:
                    turn = 'Player 2'

        else:

            clear_output()
            display_board(the_board)
            position = player_choice(the_board)

            place_marker(the_board,player2_marker,position)

            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('Player 2 has won!!!')
                game_on = False
            
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie Game!')
                    game_on = False
                else:
                    turn = 'Player 1'



    if not replay():
        break
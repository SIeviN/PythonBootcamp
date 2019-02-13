#Milestone Project 1

#Steps
#print board
#take in user input
#place user input
#game status check, in progress, won, tie
#repeat steps until won, or tie
#play again?


from IPython.display import clear_output
import random

def display_board(board):
    clear_output()
    print('_________')
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('__|___|__')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('__|___|__')
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('__|___|__')

def player_input():
    '''
    OUTPUT = (Player1 marker, Player2 marker)
    '''
    marker = ''

    while marker != 'X' and marker != 'O':
        marker = input('Player1: Choose X or O:').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position):
    board[position] = marker

def status_check(board, mark):
    return ((board[1] == board[2] == board[3] == mark) or
    (board[4] == board[5] == board[6] == mark) or
    (board[7] == board[8] == board[9] == mark) or
    (board[1] == board[4] == board[7] == mark) or
    (board[2] == board[5] == board[8] == mark) or
    (board[3] == board[6] == board[9] == mark) or
    (board[1] == board[5] == board[9] == mark) or
    (board[3] == board[5] == board[7] == mark))

def move_first():
    return random.randint(0,1)

def blank_check(board, position):
    return ((board[position] != 'X') and (board[position] != 'O'))

def full_board(board):
    for i in range(1,10):
        if blank_check(board, i):
            return False
    return True

def player_choice(board):
    position = 0
    while position not in range(1,10) or not blank_check(board, position):
        position = int(input('Choose a position (1-9) '))
    return position

def replay():
    choice = input('Play again? Yes or No ')
    return choice == 'Yes'


print('Tic-Tac-Toe Game!')
while True:
    #set up game
    board = ['#','1','2','3','4','5','6','7','8','9']
    player1_marker, player2_marker = player_input()
    
    #player move first selection
    if move_first():
        turn = 'Player 1'
        print(turn + ' will go first')
    else:
        turn = 'Player 2'
        print(turn + ' will go first')
    run_game = True

    #begin game
    while run_game:
        if turn == 'Player 1':
            display_board(board)
            print('\nPlayer 1')
            place_marker(board, player1_marker, player_choice(board))
            #check if won or tie, else continue to player 2's turn
            if status_check(board, player1_marker):
                display_board(board)
                print('Player 1 has won!')
                run_game = False
            else:
                if full_board(board):
                    display_board(board)
                    print('Tie Game!')
                    break
                else:
                    turn = 'Player 2'

        else:
            display_board(board)
            print('\nPlayer 2') 
            place_marker(board, player2_marker, player_choice(board))
            #check if won or tie, else continue to player 1's turn
            if status_check(board, player2_marker):
                display_board(board)
                print('Player 2 has won!')
                run_game = False
            else:
                if full_board(board):
                    display_board(board)
                    print('Tie Game!')
                    break
                else:
                    turn = 'Player 1'

    #replay check
    if not replay():
        break
        
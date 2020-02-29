

def display_board(board):
    print('\n*10000000000')

    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

test_board = ['#','X','O','X','O','X','O','X','O','X']

def player_input():
    ''''output = player1 or player 2 marker'''

    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Choose X or O').upper()

    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):

    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal

import random
def choost_first():
    flip = random.randint(0,1)
    if flip == 0:
        return 'Player1 go first'
    else:
        return 'Player2 go first'

def space_check(board, position):
    return board[position] == ''

def full_board_check(board):
    for i in range(1,10):
        if space_check(the_board, i):
            return False
    return True

def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Choose a position (1-9)'))
    return position

def replay():
    choice = input("Do you want to play again? Enter Yes/No")
    return choice == 'Yes'

print('Welcome to TICTACTOE GAME - by Yossi Almog Maman')

while True:
    ##play game

    ##set the board
    the_board = ['']*10
    player1_marker, player2_marker = player_input()

    turn = choost_first()
    print(turn + 'choose first')

    play_game = input('ready to play?')

    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    ##set whos first
    ## choose markes

    ##gameplay
    while game_on:
        if turn == 'Player 1':
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board,player1_marker,position)

            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('PLAYER 1 WON CONGRATULATIONS!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('tie game!')
                    game_on = False
                else:
                    turn = 'Player 2'

        else:
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player2_marker, position)

            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('PLAYER 2 WON CONGRATULATIONS!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('tie game!')
                    game_on = False
                else:
                    turn = 'Player 1'

    if not replay():
        break


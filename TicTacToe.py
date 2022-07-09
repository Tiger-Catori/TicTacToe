def display_board(board):

    """
    A function that can print out a board.
    Set up the board as a list, where each index 1-9 corresponds with a number on a number pad,
    so you get a 3 by 3 board representation.
    """
    # clear_output()  # Remember, this only works in jupyter!

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


def player_input():
    """Write a function that can take in a player input and assign their marker as 'X' or 'O'.
     Think about using while loops to continually ask until you get a correct answer."""

    marker = ''

    # KEEP ASKING PLAYER 1 TO CHOOSE X OR O
    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O: ')

    # ASSIGN PLAYER 2, THE OPPOSITE MARKER
    player1 = marker

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    return player1, player2


def place_marker(board, marker, position):
    """A function that takes in the board list object, a marker ('X' or 'O'),
    and a desired position (number 1-9) and assigns it to the board."""

    board[position] = marker


def win_check(board, mark):
    """Write a function that takes in a board and a mark (X or O)
    & then checks to see if that mark has won. """
    # WIN Means?

    # ALL ROWS & check to see if they have the same marker?
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top

            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle

            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom

            # ALL COLUMNS & check to see if the marker matches
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle

            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle

            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side

            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal

            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal



import random

def choose_first():
    """
    Step 5: Write a function that uses the random module to randomly decide which player goes first.
    You may want to lookup random.randint() Return a string of which player went first.
    """
    flip = random.randint(0, 1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(board, position):
    """Write a function that returns a boolean indicating whether a space on the board is freely available."""
    return board[position] == ' '


def full_board_check(board):
    """Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise."""
    for i in range(1, 10):
        if space_check(board, i):
            return False
    # BOARD IS FULL IF WE RETURN TRUE
    return True


def player_choice(board):
    """Write a function that asks for a player's next position (as a number 1-9)
    & then uses the function from step 6 to check if it's a free position.
    If it is, then return the position for later use."""
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))

    return position


def replay():
    """Write a function that asks the player if they want to play again
    & returns a boolean True if they do want to play again."""
    choice = input('Play Again? Enter Yes or No. ')
    return choice == 'Yes'



# Using while loops and the functions made above to run the game!

print('Welcome to Tic Tac Toe!')

while True:
    # PLAY THE GAME

    # SET things up (BOARD , MARKER, WHOS FIRST)
    the_board = [' '] * 10

    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(turn + ' will go first.')

    play_game = input('Ready to play? y or n? ')

    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Show the board
            display_board(the_board)

            # Choose a position
            position = player_choice(the_board)

            # Place the marker on the position
            place_marker(the_board, player1_marker, position)

            # Check if they won
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('PLAYER 1 has won!!')
                game_on = False

            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME!!')
                    game_on = False
                else:
                    turn = 'Player 2'
            # Or check if There is a tie

            # No tie & win? then Next player's turn

        # Player one Turn

        else:
            # Show the board
            display_board(the_board)

            # Choose a position
            position = player_choice(the_board)

            # Place the marker on the position
            place_marker(the_board, player2_marker, position)

            # Check if they won
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('PLAYER 2 has won!!')
                game_on = False

            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME!!')
                    game_on = False
                else:
                    turn = 'Player 1'
    if not replay():
        break

    # BREAK OUT OF WHILE LOOP ON replay()
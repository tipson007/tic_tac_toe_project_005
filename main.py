#create a tic tac toe game

#steps:

# create a board
# display board
# play game
# handle turn
# check win
    #check rows
    #check columns
    #check diagonals
#check tie
# flip player

#---Global variable----

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-",]
#if game is still going
game_is_still_going = True

#who won
winner = None

def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

display_board()
def play_game():

    #display the initial board
    display_board()

    while game_is_still_going:
        handle_turn(current_player)

        check_if_game_over()

    #flip to the other player
        flip_player()

#the game has ended
if winner == "X" or winner   == "O":
    print(winner + "won")
elif winner == None:
    print("Tie")


def handle_turn(player):

    print(player + "'s turn ")
    position = input("choose a position from 1 - 9: ")

    valid = False
    while not valid:


        while osition not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
             position = input("invalid input. Choose the position from 1-9: ")

        position = int(position) - 1

        if board[position]  != "-":
            vaild = True
        else:
             print("you cnt go there. go again ")

    display_board()

def check_if_game_over():
    check_for_winner()
    check_if_tie()

def check_for_winner():

    #set up global variables
    global winner
    #check rows
    row_winner = check_rows()

    #check columns
    column_winner = check_columns()

    #check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner()
    elif column_winner:
        winner = column_winner()

    elif diagonal_winner:
        winner = diagonal_winner()

    else:
        winner = None

    return

def check_rows():
    global game_is_still_going
    #check if any of the rows have all the same  values
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        game_is_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]

    return

def check_columns():
    global game_is_still_going
    # check if any of the rows have all the same  values
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    if column_1 or column_2 or column_3:
        game_is_still_going = False
    if column_1:
        return board[0]
    elif column_2:
        return board[3]
    elif column_3:
        return board[6]
    return

def check_diagonal():
    global game_is_still_going
    # check if any of the rows have all the same  values
    diagonals_1 = board[0] == board[4] == board[8] != "-"
    diagonals_2 = board[6] == board[4] == board[2] != "-"

    if diagonals_1 or diagonals_2:
        game_is_still_going = False
    if diagonals_1:
        return board[0]
    elif diagonals_2:
        return board[6]

    return

def check_if_tie():
    global game_is_still_going
    if "-" not in board:
        game_is_still_going = False
    return

def flip_player():
    #global variables we need
    global current_player
    #if the current player was x, then change it to O
    if current_player == "X":
        current_player = "O"
        #if the current player was O, then change it to X
    elif current_player == "O":
        current_player = "O"

    return


    play_game()



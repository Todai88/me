"""
Creates and initiates the tic-tac toe mini-game.

This game requires the user to win a game of tic tac toe
to gain access to the room.

It will be running until the user either gives up (EXIT)
or wins.
"""

def init_tic():
    """
    Startar tre i rad-loopen.
    """
    given_up = False
    print("Välkommen till tre i rad!")
    while (given_up == False):
        if (tictactoe()):
            return True
        else:
            choice = input("Har du gett upp(Y/N)?\n")

            if choice.upper() in ("Yes", "Y"):
                return False
            else:
                given_up = False

def cls():
    """
    Rensar konsolen.
    """
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def calc_victory(bo, le):

    """
    Uses some of the logic found here: https://inventwithpython.com/chapter10.html
    to calculate the win-conditions.
    """


    return ((bo[0][0] == le and bo[0][1] == le and bo[0][2] == le) or # across the top
            (bo[1][0] == le and bo[1][1] == le and bo[1][2] == le) or # across the middle
            (bo[2][0] == le and bo[2][1] == le and bo[2][2] == le) or # across the bottom
            (bo[0][0] == le and bo[1][0] == le and bo[2][0] == le) or # down the left side
            (bo[0][1] == le and bo[1][1] == le and bo[2][1] == le) or # down the middle
            (bo[0][2] == le and bo[1][2] == le and bo[2][2] == le) or # down the right side
            (bo[0][0] == le and bo[1][1] == le and bo[2][2] == le) or # diagonal
            (bo[2][0] == le and bo[1][1] == le and bo[0][2] == le))

def validate_input(choice):

    """
    Validates the input!
    """

    flag = False
    while (flag == False):
        try:
            if choice.upper() == 'SAVE':
                return choice
            choice = choice.split(",")
            a = int(choice[0])
            a = a - 1
            b = int(choice[1])
            b = b - 1
            if(a > 2 or 0 > a or b > 2 or 0 > b):
                flag = False
                choice = input("The move needs to be between 1-3 and formatted like this: '1,2'\n")
            else:
                choice = [a, b]
                flag = True
        except (ValueError, IndexError, AttributeError):
            print("Incorrect input!\nPlease try again!")
            choice = input("Try again!\n")
    return choice

def ai_move(board):
    """
    Calculates the AI's move based on a set of preferred moves.
    If none of the preferred moves are available it uses a random move.
    """
    from random import randint

    PREFFERED_MOVES = [[2, 2], [1, 1], [1, 3], [3, 1], [3, 3]]
    #Checking if priority move is possible
    for move in PREFFERED_MOVES:
        if board[move[0] - 1][move[1] - 1] == "_":
            return move
    #Finding a random move.
    flag = True
    while(flag):
        low_move = [randint(1, 3), randint(1, 3)]
        if board[low_move[0]][low_move[1]] == "_":
            return low_move
    return None

def tictactoe():
    """
    Play the tictactoe game
    """
    from time import sleep # importing sleep to use


    #
    #
    #   Setting up the environment
    #
    #

    flag = True
    turn = 1
    game_list = []
    game_list = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
    print("Jag har nu skapat spelbrädet.")

    #
    #
    #   Playing the game
    #
    #

    while(flag):
        if turn != 1:
            cls()
        print("\n\n")
        print("|{}|{}|{}|".format(game_list[0][0], game_list[0][1], game_list[0][2]))
        print("|{}|{}|{}|".format(game_list[1][0], game_list[1][1], game_list[1][2]))
        print("|{}|{}|{}|".format(game_list[2][0], game_list[2][1], game_list[2][2]))
        print("\n\n")
        print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #\n")
        print("Skriv dina val som (1,2). Varje siffra mellan 1-3.")
        print("\n# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")

        #
        #
        #   GAME LOGIC
        #
        #

        if turn == 9:
            print("There are no more turns! It's a draw.")
            return False
        elif (calc_victory(game_list, "x")):
            print("You won")
            return True
        elif (calc_victory(game_list, "o")):
            print("I won")
            return False
        elif turn % 2 == 0:
            print("Calculating my move...")
            sleep(1) # using sleep to simulate thinking
            move = ai_move(game_list)
            choice = "{}, {}".format(move[0], move[1])
        else:
            choice = input("Var vill du flytta?\n")
        if flag:
            choice = validate_input(choice)


        if game_list[choice[0]][choice[1]] == "_":
            game_list[choice[0]][choice[1]] = "o" if turn % 2 == 0 else "x"
            turn += 1

    input("\nPress enter to continue...")

from GameBoard import GameBoard
from Player import *


def main():
    board = GameBoard()

    while True:
        try:
            # input the player one sign
            player1_sign = input("Enter player 1 sign: ") # get the input
            # if player enters a null string, will throw a exception
            player1_sign = player1_sign[0] # get the first symbol of player enters a longer string than 1
            break
        except IndexError:
            print("It seems that you forgot to enter the sign!")

    while True:
        try:
            # input the player one sign
            player2_sign = input("Enter player 2 sign: ")  # get the input
            # if player enters a null string, will throw a exception
            player2_sign = player2_sign[0]  # get the first symbol of player enters a longer string than 1
            break
        except IndexError:
            print("It seems that you forgot to enter the sign!")

    player_versus_computer = input("Do you want to play versus computer?(Yes, No) :")

    # if player chose to play vs computer
    # make a human and a computer player
    # and put them in the players list in order to get a turn based gameplay
    if player_versus_computer == "Yes" or player_versus_computer == "yes":
        human_player = HumanPlayer(player1_sign, board)
        computer_player = ComputerPlayer(player2_sign, board)
        players = (human_player, computer_player)
    else:
        human_player1 = HumanPlayer(player1_sign, board)
        human_player2 = HumanPlayer(player2_sign, board)
        players = (human_player1, human_player2)

    # at the beginning of the game, we assume that there is no winner
    winner = False

    # print the initial empty board
    board.print_board()

    # the restart variable to restart the game
    restart = False

    while not winner:
        if restart:
            # we 'restart' the restart :))
            restart = False
            # make another board
            board = GameBoard()
            # assign the new board to the players
            for player in players:
                player.assign_board(board)

        # until is no winner we iterate through every player in the 'players' list
        for player in players:
            # current player takes a turn
            # restart will be true if player enters 'restart'
            restart = player.take_turn()
            if restart:
                break

            # we show the board after the turn
            board.print_board()

            # we check if the player (with his sign) wins the game
            # if the function return true, a winner is found, the while loop will not continue and the game is over
            winner = board.check_for_winner(player.get_player_sign())
            # print the winenr's player symbol
            if winner:
                print()
                print("Player %s WON!!!" % player.get_player_sign())
                break
main()
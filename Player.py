import time
import random

class Player:
    def __init__(self, sign, grid):
        self.sign = sign
        self.grid = grid

    def get_player_sign(self):
        return self.sign

    # method for restarting the game
    def assign_board(self, grid):
        self.grid = grid


class HumanPlayer(Player):
    def __init__(self, sign, grid):
        self.sign = sign
        self.grid = grid

    def take_turn(self):
        print("Enter 'restart' to restart the game!")
        col = input("Please enter column number: ")
        # if player enter restart, return false, which will break the loop in main
        if col == 'restart' or col == 'Restart':
            return True
        # if is not digit, the while loop will not start
        while not col.isdigit() or int(col) < 0 or int(col) >= 7 or self.grid.check_if_col_is_full(int(col), self.sign): #check if is not digit
            col = input("Please enter another column number : ")
        self.grid.put_sign_on_col(int(col), self.sign)


class ComputerPlayer(Player):
    def __init__(self, sign, grid):
        self.sign = sign
        self.grid = grid

    def take_turn(self):
        print("Computer thinking!")
        time.sleep(1) # simulate 1 sec of computer thinking
        col = random.randint(0, 6) # get a random number from 0 to 6 for the column
        # if the selected column is full, random get another one
        while self.grid.check_if_col_is_full(int(col), self.sign):
            col = random.randint(0, 6)
        self.grid.put_sign_on_col(col, self.sign)


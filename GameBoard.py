class GameBoard:

    grid = []

    rows = 6
    columns = 7

    def __init__(self):
        # initialize the board with empty spaces
        self.empty_space = ' '

        self.grid = [[self.empty_space for x in range(self.rows)] for y in range(self.columns+1)]

    def put_sign_on_col(self, col, sign):
        # go until find an empty row in the column specified, and place the selection above that
        for i in range(self.rows):
            if self.grid[col][i] != self.empty_space:
                self.grid[col][i-1] = sign
                break

            elif i == self.rows-1:
                self.grid[col][i] = sign

    def check_if_col_is_full(self, col, sign):
        count = 0
        for i in range(self.rows):
            if self.grid[col][i] != self.empty_space:
                count += 1

        if count == self.rows:
            return True
        else:
            return False

    def print_board(self):
        for y in range(self.rows):
            for x in range(self.columns):
                if self.grid[x][y] == 0:
                    print(' ', end=" ")
                else:
                    print(self.grid[x][y], end=" ")
            print()
        print('0 1 2 3 4 5 6')

    def check_for_winner(self, sign):
        if self.win_horizontal(sign) or self.win_vertical(sign) or self.check_first_diag(sign) or self.check_second_diag(sign):
            return True

    # check for horizontal win
    def win_horizontal(self, sign):
        for i in range(self.columns):
            for e in range(4):
                if self.grid[i][e] == sign and self.grid[i][e + 1] == sign and self.grid[i][e + 2] == sign and self.grid[i][e + 3] == sign:
                    return True
        return False

    # check for vertical win
    def win_vertical(self, sign):
        for e in range(self.rows):
            for i in range(3):
                if self.grid[i][e] == sign and self.grid[i + 1][e] == sign and self.grid[i + 2][e] == sign and self.grid[i + 3][e] == sign:
                    return True
        return False

    # check diagonal from top left to bottom right
    def check_first_diag(self, sign):
        for i in range(3):
            for e in range(4):
                if self.grid[i][e] == sign and self.grid[i + 1][e + 1] == sign and self.grid[i + 2][e + 2] == sign and self.grid[i + 3][
                            e + 3] == sign:
                    return True
        return False

    # check diagonal from top right to bottom left
    def check_second_diag(self, sign):
        for i in range(3):
            for e in range(self.rows - 1, -1, -1):
                if self.grid[i][e] == sign and self.grid[i + 1][e - 1] == sign and self.grid[i + 2][e - 2] == sign and self.grid[i + 3][
                            e - 3] == sign:
                    return True
        return False
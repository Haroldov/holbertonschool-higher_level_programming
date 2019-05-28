#!/usr/bin/python3

class chess_board:

    def __init__(self, N):
        self.N = N
        self.setted_queens = N
        self.next_queen = [0, 0]

    def create_game(self):
        self.weights = []
        self.setted_queens = self.N
        for rows in range(self.N):
            self.weights.append([None] * self.N)

    def set_queen(self, position):
        self.weights[int(position[0])][int(position[1])] = 0
        self.position = position
        self.setted_queens -= 1

    def update_board(self):
        sw = 0
        actual_pos = (self.position[0] * self.N) + self.position[1]
        for row in range(self.N):
            for column in range(self.N):
                tmpRow = row - self.position[0]
                tmpCol = column - self.position[1]
                if (abs(tmpRow) == abs(tmpCol)
                    and row != self.position[0]
                    and column != self.position[1]):
                    self.weights[row][column] = -1
                elif row == self.position[0] and column == self.position[1]:
                    self.weights[row][column] = 0
                elif row == self.position[0] or column == self.position[1]:
                    self.weights[row][column] = -1
                else:
                    if (actual_pos < (row * self.N) + column and
                        self.weights[row][column] != -1 and
                        self.weights[row][column] != 0) or (
                        self.weights[row][column] == None):
                        if sw == 0:
                            sw = 1
                            self.next_queen = [row, column]
                        self.weights[row][column] = self.setted_queens


    def check_pos(self):
        for row in self.weights[:]:
            if max(row) > 0:
                return True
        return False

from sys import argv, exit, stderr

if len(argv) != 2:
    stderr.write("Usage: nqueens N\n")
    exit(1)
try:
    N = int(argv[1])
except:
    stderr.write("N must be a number\n")
    exit(1)
if type(N) is not int:
    stderr.write("N must be a number\n")
    exit(1)
elif N < 4:
    stderr.write("N must be at least 4\n")
    exit(1)

cb = chess_board(N)
cb.create_game()
for row in range(N):
    for col in range(N):
        queens_loc = []
        cb.create_game()
        cb.next_queen = [row, col]
        queens_loc.append(cb.next_queen)
        while len(queens_loc) != N:
            cb.set_queen(cb.next_queen)
            cb.update_board()
#            print(cb.weights)
            if cb.check_pos() == False:
                break
            queens_loc.append(cb.next_queen)
        print(queens_loc)

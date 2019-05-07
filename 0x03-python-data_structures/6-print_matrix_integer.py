#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for rows in matrix:
        for col, num in enumerate(rows):
            if col != len(rows) - 1:
                print("{:d}".format(num), end=" ")
            else:
                print("{:d}".format(num))

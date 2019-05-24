#!/usr/bin/python3
"""
module that prints square
"""


def print_square(size):
    """ prints square"""

    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for rows in range(size):
                print("#" * size, sep="")

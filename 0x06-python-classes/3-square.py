#!/usr/bin/python3
"""This is a module that defines a class of a Square"""


class Square:
    """This is the Square class"""

    def __init__(self, size=0):
        self.__setsize = size

    @property
    def __setsize(self):
        return self.__size

    @__setsize.setter
    def __setsize(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    """ This methods computes the area of the Square"""

    def area(self):
        return self.__size ** 2

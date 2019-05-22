#!/usr/bin/python3
"""This is a module that defines a class of a Square"""


class Square:
    """This is the Square class"""

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ This methods computes the area of the Square"""
        return self.__size ** 2

    def __eq__(self, other):
        return True if self.__size ** 2 == other.__size ** 2 else False

    def __ne__(self, other):
        return True if self.__size ** 2 != other.__size ** 2 else False

    def __lt__(self, other):
        return True if self.__size ** 2 < other.__size ** 2 else False

    def __le__(self, other):
        return True if self.__size ** 2 <= other.__size ** 2 else False

    def __gt__(self, other):
        return True if self.__size ** 2 > other.__size ** 2 else False

    def __ge__(self, other):
        return True if self.__size ** 2 >= other.__size ** 2 else False

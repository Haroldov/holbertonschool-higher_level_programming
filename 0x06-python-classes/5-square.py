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
        """This method computes the area of the Square"""
        return self.__size ** 2

    def my_print(self):
        """This method prints the square"""
        if (self.__size == 0):
            print()
        for rows in range(self.__size):
            print("#" * self.__size)

#!/usr/bin/python3
"""This is a module that defines a class of a Square"""


class Square:
    """This is the Square class"""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        if type(position) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(position[1]) is not int or type(position[0]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def area(self):
        """This method computes the area of the Square"""
        return self.__size ** 2

    def my_print(self):
        """This method prints the square"""
        if (self.__size == 0):
            print()
        else:
            print("\n" * self.__position[1], end="")
            for rows in range(self.__size):
                print("_" * self.__position[0], "#" * self.__size, sep="")

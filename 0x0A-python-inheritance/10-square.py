#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
""" doc """


class Square(Rectangle):
    """ doc """
    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return super().area()

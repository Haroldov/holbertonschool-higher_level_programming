#!/usr/bin/python3
""" mod """


BaseGeometry = __import__('7-base_geometry').BaseGeometry
class Rectangle(BaseGeometry):
    """ class of a rectangle """

    def __init__(self, width, height):
            self.integer_validator("width", width)
            self.__width = width
            self.integer_validator("height", height)
            self.__height = height

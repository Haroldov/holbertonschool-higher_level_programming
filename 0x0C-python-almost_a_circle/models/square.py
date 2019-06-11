#!/usr/bin/python3
""" square package """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ square class """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return ("[Square] ({0:d}) {1:d}/{2:d} - {3:d}".format
                (self.id, self.x, self.y, self.width))

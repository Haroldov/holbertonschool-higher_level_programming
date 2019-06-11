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

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        if len(args) > 1:
            tmpArgs = [item for item in args]
            tmpArgs.insert(1, tmpArgs[1])
        else:
            tmpArgs = args
        super().update(*tmpArgs, **kwargs)

    def to_dictionary(self):
        attrs = ["id", "x", "size", "y"]
        vals = [self.id, self.x, self.width, self.y]
        return dict(zip(attrs, vals))

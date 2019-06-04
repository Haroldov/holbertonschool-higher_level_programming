#!/usr/bin/python3
""" doc """


class MyInt(int):
    """ doc """

    def __eq__(self, other):
        return False if int(self) == int(other) else True

    def __ne__(self, other):
        return False if int(self) != int(other) else True

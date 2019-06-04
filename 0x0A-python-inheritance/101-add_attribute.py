#!/usr/bin/python3
""" doc """


def add_attribute(obj, name, value):
    """ doc """

    if "__slots__" in dir(obj) or hasattr(obj, "__dict__") == False:
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)

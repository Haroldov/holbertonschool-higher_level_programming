#!/usr/bin/python3
""" doc """


def inherits_from(obj, a_class):
    """ doc """

    if (type(obj) != a_class):
        return issubclass(type(obj), a_class)
    else:
        return False

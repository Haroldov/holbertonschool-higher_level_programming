#!/usr/bin/python3
"""
This module has a function that adds two numbers
"""


def add_integer(a, b=98):
    """ adds two integers.
    Args:
        a: the first number.
        b: the second number (if doesn't exist default is 98).
    Returns:
        the addition of both numbers.
    """

    if a != a:
        return float('NaN')
    if b != b:
        return float('NaN')
    if a is None:
        raise TypeError("a must be an integer")
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    if (a + b) == float('inf') or (a + b) == -float('inf'):
        return None
    if type(a) is float or type(b) is float:
        a = int(a)
        b = int(b)

    return a + b

#!/usr/bin/python3
"""
function to divide matrix
"""


def matrix_divided(matrix, div):
    """ does matrix division
    Args:
        matrix: the matrix to be divided.
        div: the div
    Returns:
        matrix divided by div
    """
    checkType = []
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if type(row) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        elif len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        else:
            checkType.append(all(list(map(lambda x: isinstance(x, int) or
                                          isinstance(x, float), row))))
    if all(checkType) is False:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    return list(map(lambda row: list(map(lambda elem: round(elem / div, 2),
                                         row)), matrix))

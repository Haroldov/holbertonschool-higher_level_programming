#!/usr/bin/python3
"""
module that has matrix operations
"""


def lazy_matrix_mul(m_a, m_b):
    """ matrix multiplication"""
    import numpy as np
    if type(m_a) is not list:
        raise TypeError("m_a must be a list or")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    for row in m_a:
        if type(row) is not list:
            raise TypeError("m_a must be a list of lists")
    for row in m_b:
        if type(row) is not list:
            raise TypeError("m_b must be a list of lists")
    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")
    for row in m_a:
        for elem in row:
            if type(elem) is not float and type(elem) is not int:
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for elem in row:
            if type(elem) is not float and type(elem) is not int:
                raise TypeError("m_b should contain only integers or floats")
    for row in m_a:
        if len(row) != len(m_a[0]):
            raise TypeError("each row of m_a must should be of the same size")
    for row in m_b:
        if len(row) != len(m_b[0]):
            raise TypeError("each row of m_b must should be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    return np.matrix(m_a)*np.matrix(m_b)

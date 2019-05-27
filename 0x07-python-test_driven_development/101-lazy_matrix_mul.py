#!/usr/bin/python3
"""
module that has matrix operations
"""


def lazy_matrix_mul(m_a, m_b):
    """ matrix multiplication """
    import numpy as np
    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")

    return np.matmul(np.asarray(m_a), np.asarray(m_b))

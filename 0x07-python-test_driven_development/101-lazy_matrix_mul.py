#!/usr/bin/python3
"""
module that has matrix operations
"""


def lazy_matrix_mul(m_a, m_b):
    """ matrix multiplication """
    import numpy as np
    return np.matmul(np.asarray(m_a), np.asarray(m_b))

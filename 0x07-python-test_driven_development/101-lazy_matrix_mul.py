#!/usr/bin/python3
import numpy as np
"""
function lazy_matrix_mul
parametres: m_a, m_b
Return: result matrix_mul
"""


def lazy_matrix_mul(m_a, m_b):
    """
    function lazy_matrix_mul
    """
    result = np.matmul(m_a, m_b)
    return result

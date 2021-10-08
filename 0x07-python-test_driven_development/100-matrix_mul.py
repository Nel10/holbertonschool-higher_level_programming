#!/usr/bin/python3
"""
function matrix_mul
parametres: m_a, m_b
Return matrix mul
"""


def matrix_mul(m_a, m_b):
    """
    function matrix_mul
    """
    message_m_a = "m_a should contain only integers or floats"
    message_m_b = "m_b should contain only integers or floats"
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    for row in m_a:
        if type(row) is not list:
            raise TypeError("m_a must be a list of lists")
    for j in m_b:
        if type(j) is not list:
            raise TypeError("m_b must be a list of lists")
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    else:
        if not m_a[0]:
            raise ValueError("m_a can't be empty")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    else:
        if not m_b[0]:
            raise ValueError("m_b can't be empty")
    if type(m_a[0]) is not list:
        for i in m_a[0]:
            if type(i) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")
    else:
        len_row = len(m_a[0])
        for row in m_a:
            for item in row:
                if type(item) not in [int, float]:
                    raise TypeError(message_m_a)
            if len(row) != len_row:
                raise TypeError("each row of m_a must be of the same size")
            len_row = len(row)

    if type(m_b[0]) is not list:
        for i in m_b[0]:
            if type(i) not in [float, int]:
                raise TypeError("m_b should contain only integers or floats")
    else:
        len_row = len(m_b[0])
        for row in m_b:
            for item in row:
                if type(item) not in [int, float]:
                    raise TypeError(message_m_b)
            if len(row) != len_row:
                raise TypeError("each row of m_b must be of the same size")
            len_row = len(row)

    if len(m_a[0]) == len(m_b):
        m_c = []
        for i in range(len(m_a)):
            m_c.append([])
            for j in range(len(m_b[0])):
                m_c[i].append(0)
        for i in range(len(m_a)):
            for j in range(len(m_b[0])):
                for k in range(len(m_a[0])):
                    m_c[i][j] += m_a[i][k] * m_b[k][j]
        return m_c
    else:
        raise ValueError("m_a and m_b can't be multiplied")

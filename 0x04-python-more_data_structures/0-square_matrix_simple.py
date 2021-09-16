#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    c_matrix = [list(map(lambda i: i ** 2, i)) for i in matrix]
    return (c_matrix)

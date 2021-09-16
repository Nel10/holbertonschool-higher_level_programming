#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return None
    i = []
    for  j in matrix:
        i.append([x ** 2 for x in j])
        return i

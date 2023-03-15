#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # check for empty list
    if matrix == []:
        return matrix

    new_matrix = matrix.copy()

    for i, row in enumerate(matrix):
        new_matrix[i] = list(map(lambda x: x**2, row))

    return new_matrix

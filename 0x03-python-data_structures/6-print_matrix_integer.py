#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print()

    for row in matrix:
        row_len = len(row)

        for i, integer in enumerate(row):
            if i == row_len - 1:
                print('{:d}'.format(integer))
            else:
                print('{:d}'.format(integer), end=' ')

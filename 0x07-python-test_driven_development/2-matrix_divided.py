#!/usr/bin/python3

"""Module that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """Divides all the elements of a matrix.

    Args:
        matrix: the matrix.
        div: the integer or float used for dividing the elements by.

    Raises:
        TypeError: if matrix is not a list of lists of ints or floats.
        TypeError: if the matrix's rows are not of the same length.
        TypeError: if div is not an integer or float.
        ValueError: if div is equal to 0.

    Returns:
        A new matrix with the results of the division.
    """

    if not isinstance(matrix, list):
        raise TypeError('matrix must be a matrix (list of lists) '
                        'of integers/floats')

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    new_matrix = []
    row_len = len(matrix[0])

    for i, row in enumerate(matrix):
        if not isinstance(row, list):
            raise TypeError('matrix must be a matrix (list of lists) '
                'of integers/floats')

        if row_len != len(row):
            raise TypeError('Each row of the matrix must have '
                'the same size')

        new_matrix.append([])
        for num in row:
            if not isinstance(num, int) and not isinstance(num, float):
                raise TypeError('matrix must be a matrix (list of lists) '
                                'of integers/floats')

            new_matrix[i].append(round(num / div, 2))

    return (new_matrix)


# when it comes to a matrix then it seems that it is not copied,
# but shared between name spaces(variables)
# m = [[1,2,3], [4,5,6]]
# n = m.copy()
# m[0][1] = 1
# print(m)
# print(n)

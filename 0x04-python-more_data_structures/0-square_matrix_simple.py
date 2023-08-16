#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Returns the square of all the integers of a matrix"""

    new_matrix = []
    for i in matrix:
        new_in_list = list(map((lambda x: x ** 2), i))
        new_matrix.append(new_in_list)
    return new_matrix

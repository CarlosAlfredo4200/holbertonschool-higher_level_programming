#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = []
    for row in matrix:
        square_row = []
        for num in row:
            square_row.append(num ** 2)
        result.append(square_row)
    return result

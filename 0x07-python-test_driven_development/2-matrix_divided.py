#!/usr/bin/python3
"""
This module provides a function to divide a matrix by a number.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix: A list of lists containing integers or floats.
                Each inner list represents a row of the matrix.
        div: A number (integer or float) used as the divisor.

    Raises:
        TypeError: If matrix is not a list.
        TypeError: If matrix is not a list of lists.
        TypeError: If matrix contains elements that are not numbers (int/float).
        TypeError: If the rows of the matrix are not of the same length.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is 0.

    Returns:
        new_matrix: A new matrix with all elements divided by the div.
                    The resulting values are rounded to 2 decimal places.
    """

    # Error messages
    err_matrix = "matrix must be a matrix (list of lists) of integers/floats"
    err_matrix2 = "matrix must be a matrix (list of lists) of integers/floats"

    # Check if matrix is a list
    if type(matrix) is not list:
        raise TypeError(err_matrix)

    # Check if matrix is a list of lists
    for li in matrix:
        if type(li) is not list:
            raise TypeError(err_matrix)
        else:
            # Check if matrix contains only numbers (int/float)
            for num in li:
                if not (type(num) is int or type(num) is float):
                    raise TypeError(err_matrix2)

    len_li = len(matrix[0])
    # Check if all rows in the matrix have the same length
    for li in matrix:
        if len(li) is not len_li:
            raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number
    if not (type(div) is int or type(div) is float):
        raise TypeError("div must be a number")

    # Check if div is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide each element of the matrix by div and round to 2 decimal places
    new_matrix = []
    for row in matrix:
        new_matrix.append(list(map(lambda num: round(num / div, 2), row)))

    return new_matrix

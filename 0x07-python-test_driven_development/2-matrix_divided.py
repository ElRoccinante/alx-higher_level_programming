def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.

    Args:
        matrix (list[list[int or float]]): The input matrix.
        div (int or float): The number to divide the matrix elements by.

    Returns:
        list[list[float]]: The new matrix with elements divided by div.

    Raises:
        TypeError: If matrix is not a list, or not a list of lists, or contains non-numeric elements.
        TypeError: If the rows of the matrix are not the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is 0.
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a list")

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must contain only integers or floats")

    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]
    return new_matrix

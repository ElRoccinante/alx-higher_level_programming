#!/usr/bin/python3
"""
    add_numbers module

    add_numbers supplies one function, add_numbers(num1, num2=98)
"""


def add_numbers(num1, num2=98):
    """Function that adds two numbers

    Args:
        num1: first number.
        num2: second number, default 98

    Raises:
        TypeError: if num1, num2 are not int, float

    Returns:
        The sum of num1 and num2
    """
    if type(num1) not in (int, float):
        raise TypeError("num1 must be an integer or float")
    if type(num2) not in (int, float):
        raise TypeError("num2 must be an integer or float")

    return int(num1) + int(num2)

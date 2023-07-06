#!/usr/bin/python3


def add_integer(a, b=98):

    # Check if a is not an integer or a float
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    # Check if b is not an integer or a float
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Cast a and b to integers and return their sum
    return int(a) + int(b)

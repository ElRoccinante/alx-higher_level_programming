#!/usr/bin/python3
"""Module for class BaseGeometry"""


class BaseGeometry:
    """class BaseGeometry"""
    def __init__(self):
        """new instance of BaseGeometry"""
        pass

    def area(self):
        """Calculate the area of the geometry.
        Raises:
            Exception: If the area calculation is not implemented
            for a specific geometry."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that the value is an integer.
        Args:
            name (str): The name of the parameter.
            value (int): The value to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

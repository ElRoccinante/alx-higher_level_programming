#!/usr/bin/python3
"""
Defines a base class for gemetry
"""


class BaseGeometry():
    """Represents base geometry
    """

    def area(self):
        raise Exception("area() is not implemented")

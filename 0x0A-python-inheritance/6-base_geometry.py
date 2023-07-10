#!/usr/bin/python3
"""Defines a base class for geometry."""


class BaseGeometry:
    """Represents base geometry."""

    def area(self):
        """Public instance method that raise an exception."""
        raise Exception("area() is not implemented")

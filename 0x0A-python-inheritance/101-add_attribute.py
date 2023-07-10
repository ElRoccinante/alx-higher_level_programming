#!/usr/bin/python3
"""Defines the add_attribute function to test and add attributes"""


def add_attribute(obj, name, value):
    """Test if an attribute can be added to the
    object and add it if possible.

    Args:
        obj (object): The object to which the
        attribute will be added.
        name (str): The name of the attribute.
        value (any): The value of the attribute.

    Raises:
        TypeError: If the object does not support
        attribute assignment"""
    if hasattr(obj, "__dict__"):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")

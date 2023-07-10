#!/usr/bin/python3
"""Module for function inherits_from"""


def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class that inherited
    (directly or indirectly)
    from the specified class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare against.

    Returns:
    True if obj is an instance of a class that inherited
        (directly or indirectly)
              from the specified class; False otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class

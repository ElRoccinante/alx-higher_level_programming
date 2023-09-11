#!/usr/bin/python3
"""Module for function ingerits_from"""


def inherits_from(obj, a_class):
    """
    check if the object is an instance of a class that inherited
    (directly or indirectly)
    from the specified class.

    Args:
        obj (any): The object to check.
        a_class (type): the class to compare against.

        Returns:
        True if obj is an instance of a class that ingerited
            (directly or indirectly)
                from the specified class; False otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class

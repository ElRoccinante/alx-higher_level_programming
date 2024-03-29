#!/usr/bin/python3
"""Defines a class-cheking function"""


def is_same_class(obj, a_class):
    """
    check if an object is an instance of a given class
    Args:
        obj (any):: the object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is an instance of a_class - True.
        Otherwise - False
    """
    return type(obj) is a_class

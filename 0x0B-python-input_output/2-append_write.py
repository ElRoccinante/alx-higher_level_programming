#!/usr/bin/python3
"""appends to text and returns num chars"""


def append_write(filename="", text=""):
    """function that appends a string at the end of a text file
    and returns the number of characters added
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return (f.write(text))

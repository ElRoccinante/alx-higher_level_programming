#!/usr/bin/python3
"""

writes to text & returns num chars
"""


def write_file(filename="", text=""):
    """writes to text and returns num chars"""
    with open(filename, mode="w", encoding="utf-8") as f:
        return (f.write(text))

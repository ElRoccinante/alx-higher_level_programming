#!/usr/bin/python3
"""his defines a JSON file-reading function."""
import json


def load_from_json_file(filename):
    """A function that creates an Object from a JSON file"""
    with open(filename, "r", encoding="UTF-8") as f:
        obj = json.loads(f.read())
    return obj

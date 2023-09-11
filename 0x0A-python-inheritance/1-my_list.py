#!/usr/bin/python3
"""Define an sublcass or child list class myList"""


class MyList(list):
    """class MyList that inherits from list"""

    def print_sorted(self):
        """Methode for print sorted list"""
        sorted_list = sorted(self, key=None, reverse=False)
        print(sorted_list)

#!/usr/bin/python
"""define an subclass or child list class Mylist"""


class Mylist(list):
    """class Mylist that inherits from list"""    
    

    def print_sorted(self):
        """methode for print sorted list"""
        print(sorted(self))

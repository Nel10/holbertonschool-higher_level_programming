#!/usr/bin/python3
"""
class MyList
parametres: list
Return: sorted list
"""


class MyList(list):
    """
    Public instance method
    """
    def print_sorted(self):
        print(sorted(self))

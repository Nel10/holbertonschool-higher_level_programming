#!/usr/bin/python3
"""
function: read_file
parametres: filename=""
"""


def read_file(filename=""):
    """
    function print a file
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end="")

#!/usr/bin/python3
"""
function append_write
parametres: filename, text
"""


def append_write(filename="", text=""):
    """ return the number of characters added"""
    with open(filename, 'a', encoding="utf-8") as append:
        return append.write(text)

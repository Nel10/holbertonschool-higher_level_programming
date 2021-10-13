#!/usr/bin/python3
"""
function write_file
parametres: filename, text
"""


def write_file(filename="", text=""):
    """ writes a string to a text file (UTF8) and returns the number"""
    with open(filename, 'w', encoding="utf-8") as archive:
        return archive.write(text)

#!/urs/bin/python3
"""
function: read_file
parametres: filename=""
"""


def read_file(filename=""):
    """
    function print a file
    """
    with open(filename, "r", encoding="utf-8") as archivo:
        print(archivo.read(), end="")

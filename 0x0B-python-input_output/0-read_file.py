#!/urs/bin/python3
"""
function: read_file
parametres: filename=""
"""


def read_file(filename=""):
    """
    function print a file
    """
    with open("my_file_0.txt", encoding="UTF8") as archivo:
        for line in archivo:
            print(line, end="")

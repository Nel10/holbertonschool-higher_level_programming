#!/usr/bin/python3
"""Square that defines a square"""


class Square:
    """Private instance attribute: size
    Instantiation with size (no type/value verification)
    You are not allowed to import any module"""
    def __init__(self, size):
        """Inicialises

        Args:
            size (int): size of a side of the square

        Return: None """
        self.__size = size

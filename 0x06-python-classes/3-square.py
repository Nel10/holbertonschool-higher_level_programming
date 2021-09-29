#!/usr/bin/python3
"""Define class Square"""


class Square:
    """Represent a square

    Attribute:
        __size (int):size of a side the square"""
    def __init__(self, size=0):
        """inicialisation
        Args:
            sixe (int): size of a side of the square
        Return: None"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            self.__size = size

    def area(self):
        """calculate the square area
        Return:
            the area of the square"""
        return (sel.__size) ** 2

#!/usr/bin/python3
"""Define class square"""


class Square:
    """Represent a square

    Attribute:
        __size (int): size of a side of the square"""
    def __init__(self, size=0):
        """inicialisation

        Args:
            size (int): sze of a side of the square
        Return: None"""
        self.size = size

    def area(self):
        """calculare the square area

        Return: the area of the square"""
        return (self.__size) ** 2

    @property
    def size(self):
        """getting of __size

        Return: the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """getting of __size

        Args:
            value (int): the size of the square
        Return: None"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be <= 0")
            else:
                self.__size = value

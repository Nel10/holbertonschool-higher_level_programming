#!/usr/bin/python3
"""Defines class square"""


class Square:
    """Represent a square

    Attributes:
        __size (int): size of a side the square"""
    def __init__(self, size=0):
        """inicialisation the square

        Args:
            size (int): size of a side the square
        Return: None"""
        self.size = size

    def area(self):
        """calculate square area

        Return: the area of the square"""
        return (self.__size) ** 2

    @property
    def size(self):
        """getting of __size

        Return: the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter of _size

        Args:
            value (int): size of a side the square

        Return: None"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def my_print(self):
        """printing square

        Return: None"""
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            print("".join(["#" for j in range(self.__size)]))

#!/usr/bin/python3
"""Define class a Rectangle"""


class Rectangle:
    """representation of Rectangle"""
    def __init__(self, width=0, height=0):
        """inicialisation the Rectangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """getter Private instance attribute: width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter Private instance attribute: width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter Private instance attribute: height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter Private instance attribute: height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return the area of the Rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """return the perimeter of the Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """return printable string representation of a Rectangle"""
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join("#" * self.__width
                                for i in range(self.__height))
        return string

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.__width, self.height))

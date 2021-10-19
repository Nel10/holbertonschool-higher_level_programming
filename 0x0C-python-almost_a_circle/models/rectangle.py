#!/usr/bin/python3
"""
Created base class
"""
from models.base import Base


class Rectangle(Base):
    """Define Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """iniciatialize"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width property"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height property"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x property"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y property"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ return area """
        return self.__width * self.__height

    def __str__(self):
        """return str"""
        string = "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"
        string = string.format(self.id, self.x, self.y, self.width,
                               self.height)
        return string

    def update(self, *args, **kwargs):
        """function update"""
        list = ["id", "width", "height", "x", "y"]
        if args and args[0] is not None:
            if len(list) > len(args):
                max_len = len(args)
            else:
                max_len = len(list)
            for i in range(max_len):
                setattr(self, list[i], args[i])
        elif kwargs is not None:
            for key in kwargs:
                if hasattr(self, key) is True:
                    setattr(self, key, kwargs[key])

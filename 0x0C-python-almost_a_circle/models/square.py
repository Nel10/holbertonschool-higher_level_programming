#!/usr/bin/python3
"""
class base
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class square"""
    def __init__(self, size, x=0, y=0, id=None):
        """inicialice attr"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """property size"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def __str__(self):
        """function str"""
        string = "[Square] ({:d}) {:d}/{:d} - {:d}"
        string = string.format(self.id, self.x, self.y, self.width)
        return string

    def update(self, *args, **kwargs):
        """function update"""
        list = ["id", "size", "x", "y"]
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

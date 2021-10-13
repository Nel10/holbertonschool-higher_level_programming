#!/usr/bin/python3
"""
class student
"""


class Student:
    """class student"""

    def __init__(self, first_name, last_name, age):
        """method init"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """function of class"""
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for i in attrs:
            try:
                new_dict[i] = self.__dict__[i]
            except:
                pass
        return new_dict

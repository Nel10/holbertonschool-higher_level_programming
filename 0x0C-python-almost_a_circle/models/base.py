#!/usr/bin/python3
"""
create new class Base
"""
import json


class Base:
    """class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """inicialize"""
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """retturn the string"""
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

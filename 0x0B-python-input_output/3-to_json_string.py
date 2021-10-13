#!/usr/bin/python3
import json
"""
function to_json_string
parametres: my_obj
"""


def to_json_string(my_obj):
    """returns the JSON representation of an object (string)"""
    return json.dumps(my_obj)

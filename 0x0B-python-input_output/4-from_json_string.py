#!/usr/bin/python3
"""
function from_json_string
parametres: my_str
"""

import json


def from_json_string(my_str):
    """returns an object (Python data structure) represented by a JSON str"""
    return json.loads(my_str)

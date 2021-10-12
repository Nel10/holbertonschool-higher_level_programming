#!/usr/bin/python3
"""
function inherits_from
parametres: obj, a_class
"""


def inherits_from(obj, a_class):
    """
    function inherits_from
    """
    return type(obj) != a_class and isinstance(obj, a_class)

#!/usr/bin/python3
"""
function is_same_class
parametres: obj, a_class
"""


def is_same_class(obj, a_class):
    """
    function return True or False
    """
    if type(obj) == a_class:
        return True
    else:
        return False

#!/usr/bin/python3
"""
function say_my_name
parametres: first_name, last_name
Return: My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
    function say_my_name
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))

#!/usr/bin/python3
"""
Function text_indentation
parametres: text
Return: text
"""


def text_indentation(text):
    """
    function text_indentation
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    my_list = list(text)
    for i in range(len(my_list)):
        if my_list[i] == '.' or my_list[i] == '?' or my_list[i] == ':':
            if my_list[i + 1] and my_list[i + 2]:
                my_list[i + 1] == '\n'
                my_list.insert(i + 2, '\n')
        i += 2
    my_list = "".join(my_list)
    print(my_list, end="")

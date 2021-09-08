#!/usr/bin/python3
def uppercase(str):
    newstring = ""
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            newstring += chr(ord(str[i]) - 32)
            continue
        newstring += str[i]
    print("{}".format(newstring))

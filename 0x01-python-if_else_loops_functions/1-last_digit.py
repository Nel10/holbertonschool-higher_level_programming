#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
stri = "Last digit of"
if number >= 0:
    i = number % 10
else:
    i = number % -10
if i > 5:
    print("{} {} is {} and is greater than 5".format(stri, number, i))
if i == 0:
    print("{} {} is {} and is 0".format(stri, number, i))
if i < 6 and i != 0:
    print("{} {} is {} and is less than 6 and not 0".format(stri, number, i))

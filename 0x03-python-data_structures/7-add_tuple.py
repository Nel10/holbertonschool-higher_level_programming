#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = validacion(tuple_a)
    tuple_b = validacion(tuple_b)
    return ((tuple_a[0] + tuple_b[0]), (tuple_a[1] + tuple_b[1]))


def validacion(tuple_=()):
    if len(tuple_) < 2:
        if len(tuple_) == 1:
            tuple_ = (tuple_[0], 0)
        elif len(tuple_) == 0:
            tuple_ = (0, 0)
        elif len(tuple_) > 2:
            tuple_ = (tuple_[0], tuple_[1])
            return tuple_

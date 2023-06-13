#!/usr/bin/python3

def check_tuple(tuple_x):
    if len(tuple_x) < 2:
        return tuple_x + (0,) * (2-len(tuple_x))
    elif len(tuple_x) > 2:
        return tuple_x[:2]
    else:
        return tuple_x


def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = check_tuple(tuple_a)
    tuple_b = check_tuple(tuple_b)

    first = tuple_a[0] + tuple_b[0]
    second = tuple_a[1] + tuple_b[1]

    return (first, second)

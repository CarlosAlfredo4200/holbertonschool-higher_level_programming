#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    a = tuple_a[:2] if len(tuple_a) >= 2 else (0, 0)
    b = tuple_b[:2] if len(tuple_b) >= 2 else (0, 0)

    result = (a[0] + b[0], a[1] + b[1])
    return result

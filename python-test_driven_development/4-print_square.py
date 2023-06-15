#!/usr/bin/python3
"""a function that prints a square with the character #"""


def print_square(size):
    """

    Prints a square made up of '#' characters with a size of 'size'.


    """

    if not isinstance(size, (int)):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for item in range(size):
        print("#" * size)

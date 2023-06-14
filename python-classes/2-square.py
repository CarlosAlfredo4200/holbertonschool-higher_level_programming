#!/usr/bin/python3
"""Square module.

This module contains a class Square that defines a square
sets its size
"""


class Square():
    """Define a square"""

    def __init__(self, size=0):
        """Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square.
        """
        if not isinstance(size, int):
            raise TypeError()
        elif size < 0:
            raise ValueError()
        self.__size = size

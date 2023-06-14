#!/usr/bin/python3
"""Square module.

This module contains a class Square that defines a square
sets its size
"""


class Square():
    """Define a square"""

    def __init__(self, size):
        """Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square.
        """
        self.__size = size

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

        self.__size = size

    def area(self):
        """returns the current square area """
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def my_print(self):
        for item in range(self.__size):
            print('#' * self.__size)
        if self.__size == 0:
            print('')

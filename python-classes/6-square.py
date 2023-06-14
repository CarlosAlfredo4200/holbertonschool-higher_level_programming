#!/usr/bin/python3
"""Square module.

This module contains a class Square that defines a square
sets its size
"""


class Square:
    """Define a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """returns the current square area """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    @property
    def position(self):
        """__position getter, setter with same method name
        Returns:
            __position (tuple) ((int), (int)): horizontal offset in spaces,
            vertical offset in newlines
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Args:
            value (int): tuple of two positive integers
        Attributes:
            __position (tuple) ((int), (int)): horizontal offset in spaces,
            vertical offset in newlines
        Raises:
            TypeError: if value is not a tuple of two positive ints
        """
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) is not 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        for num in value:
            if type(num) is not int or num < 0:
                raise TypeError('position must be a tuple of ' +
                                '2 positive integers')
        self.__position = value

    def area(self):
        area = self.__size * self.__size
        return area

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for item in range(0, self.__position[1]):
                print()
            for i in range(0, self.__size):
                for k in range(0, self.__position[0]):
                    print(" ", end="")
                for item in range(0, self.__size):
                    print("#", end="")
                print()

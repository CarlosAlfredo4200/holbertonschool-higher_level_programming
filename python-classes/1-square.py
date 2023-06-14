#!/usr/bin/python3
class Square:
    """
    Represents a square.

    Attributes:
        __size (int): The size of the square.

    Raises:
        TypeError: If the size is not an integer.
        ValueError: If the size is a negative value.
    """

    def __init__(self, size):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("Size must be an integer.")
        elif size < 0:
            raise ValueError("Size must be a non-negative value.")
        else:
            self.__size = size

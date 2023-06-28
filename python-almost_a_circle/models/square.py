#!/usr/bin/python3
"""class """

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This class represents a Square and inherits from
    the Rectangle class.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes an instance of the Square class.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Getter method for the size attribute
        (which is the same as width or height).
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute
        (which is the same as width or height).
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Returns a string representation of the Square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def display(self):
        """
        Prints a visual representation of the Square using the '#' character.
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(' ' * self.x + '#' * self.width)

#!/usr/bin/python3
"""class """

# models/rectangle.py

from models.base import Base


class Rectangle(Base):
    """
    This class represents a Rectangle and inherits from
    the Base class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes an instance of the Rectangle class.

        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter method for the width attribute.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the width attribute.

        """
        if isinstance(value, int) and value > 0:
            self.__width = value
        else:
            raise ValueError("Width must be a positive integer.")

    @property
    def height(self):
        """
        Getter method for the height attribute.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the height attribute.

        """
        if isinstance(value, int) and value > 0:
            self.__height = value
        else:
            raise ValueError("Height must be a positive integer.")

    @property
    def x(self):
        """
        Getter method for the x-coordinate attribute.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter method for the x-coordinate attribute.

        """
        if isinstance(value, int):
            self.__x = value
        else:
            raise ValueError("X-coordinate must be an integer.")

    @property
    def y(self):
        """
        Getter method for the y-coordinate attribute.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter method for the y-coordinate attribute.

        """
        if isinstance(value, int):
            self.__y = value
        else:
            raise ValueError("Y-coordinate must be an integer.")

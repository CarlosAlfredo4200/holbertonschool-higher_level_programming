#!/usr/bin/python3
"""Write an empty class BaseGeometry"""


class BaseGeometry:
    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if value is not None and not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value is not None and value <= 0:
            raise ValueError(f"{name} must be greater than 0")

#!/usr/bin/python3
"""Este módulo contiene una función para sumar dos números enteros."""


def add_integer(a, b=98):
    """Esta función suma dos números enteros o de punto flotante.

    Args:
        a (int o float): El primer número a sumar.
        b (int o float, opcional): El segundo número a sumar. Por defecto es 98
    Returns:
        int: La suma de los dos números.


    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)

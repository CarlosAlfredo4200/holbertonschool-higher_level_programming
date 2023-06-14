#!/usr/bin/python3
"""Este módulo contiene una función para sumar dos números enteros o de punto flotante."""

def add_integer(a, b=98):
    """Esta función suma dos números enteros o de punto flotante.

    Args:
        a (int o float): El primer número a sumar.
        b (int o float, opcional): El segundo número a sumar. Por defecto es 98.

    Returns:
        int: La suma de los dos números.

    Raises:
        TypeError: Si alguno de los argumentos no es un número entero o de punto flotante.

    Ejemplos:
        >>> add_integer(2, 3)
        5

        >>> add_integer(-5, 10)
        5

        >>> add_integer(0, 0)
        0

        >>> add_integer('a', 'b')
        Traceback (most recent call last):
            ...
        TypeError: a must be an integer
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)
    return a + b

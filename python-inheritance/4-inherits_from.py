#!/usr/bin/python3
"""object is an  instance of a class that inherited"""


def inherits_from(obj, a_class):
    """Method that return True if an object is an instance of a class"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class


# def inherits_from(obj, a_class):: Esta es la declaración de la función inherits_from. 
# Toma dos argumentos: obj y a_class. obj es el objeto que se verificará y a_class es 
# la clase con la que se verificará la instancia.


# return issubclass(type(obj), a_class) and type(obj) is not a_class: 
# Esta es la declaración de retorno de la función. 
# Comprueba si el tipo de obj es una subclase de a_class usando la función issubclass. 
# Luego, verifica si el tipo de obj no es igual a a_class para asegurarse de que obj 
# no sea exactamente una instancia directa de a_class. Si ambas condiciones son verdaderas, 
# se devuelve True. Si no, se devuelve False.

# En resumen, la función inherits_from verifica si un objeto es una instancia de una clase dada, 
# teniendo en cuenta las relaciones de herencia.
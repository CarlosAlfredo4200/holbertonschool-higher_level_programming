#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0

    roman_values = {
        'I': 1, 
        'V': 5, 
        'X': 10, 
        'L': 50,
        'C': 100, 
        'D': 500, 
        'M': 1000
        }

    result = 0
    prev_value = 0

    for char in reversed(roman_string):
        value = roman_values.get(char, 0)

        if value >= prev_value:
            result += value
        else:
            result -= value

        prev_value = value

    return result




# --------------------------------------------------


# Primero, verificamos si la entrada es una cadena de texto válida. Si no es una cadena o una cadena vacía, devolvemos 0 según lo especificado.
# Luego, definimos un diccionario roman_values que asigna cada carácter de número romano a su valor entero correspondiente.
# Inicializamos la variable result en 0, la cual almacenará el valor entero acumulado, y prev_value en 0, que guarda el valor del número romano previo.
# Iteramos a través de roman_string en orden inverso usando reversed(roman_string). Esto nos permite procesar los números romanos de derecha a izquierda, siguiendo las reglas de los números romanos.
# Para cada carácter char en roman_string invertido, usamos roman_values.get(char, 0) para obtener su valor entero correspondiente. Si el carácter no se encuentra en el diccionario roman_values, se establece el valor predeterminado en 0.
# Comparamos el valor actual con el valor previo. Si es mayor o igual, lo sumamos al result. De lo contrario, lo restamos. Esto maneja casos como "IV" (4) donde restamos el valor de "I" de "V".
# Después de procesar cada carácter, actualizamos prev_value para almacenar el valor actual para la próxima iteración.
# Finalmente, devolvemos el result, que representa el valor entero del número romano.
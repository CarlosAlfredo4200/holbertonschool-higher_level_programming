#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    divide = lambda x, y: x / y if y != 0 else 0

    result_list = []
    error_messages = []  

    for i in range(list_length):
        try:
            element_1 = my_list_1[i]
            element_2 = my_list_2[i]

            if not isinstance(element_1, (int, float)) or not isinstance(element_2, (int, float)):
                error_messages.append("wrong type")
                result_list.append(0)
                continue

            try:
                result_list.append(divide(element_1, element_2))
            except ZeroDivisionError:
                error_messages.append("division by 0")
                result_list.append(0)

        except IndexError:
            error_messages.append("out of range")
            result_list.append(0)

    # Imprimir los mensajes de error
    for message in error_messages:
        print(message)

    return result_list

#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    return list(map(lambda x: x * number, my_list))


# def multiply_list(my_list=[], number=0):
#     multiplied_list = []
#     for value in my_list:
#         multiplied_list.append(value * number)
#     return multiplied_list

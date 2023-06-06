#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return list(map(lambda item: replace if item == search else item, my_list))


# def search_replace(my_list, search, replace):
#     newList = []
#     for item in my_list:
#         if item != search:
#             newList.append(item)
#         else:
#             newList.append(replace)
#     return newList
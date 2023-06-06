#!/usr/bin/python3
def element_at(my_list, idx):
    for item in my_list:
        if idx < 0 or idx > len(my_list) -1:
            return None
        else:
            data = my_list[idx]
            return data

#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    values = []
    for key in a_dictionary:
        values.append(a_dictionary[key])

    max_value = max(values)

    best_keys = []
    for key in a_dictionary:
        if a_dictionary[key] == max_value:
            best_keys.append(key)

    return best_keys[0]




# def best_score(a_dictionary):
#     if not a_dictionary:
#         return None
    
#     values = list(map(lambda x: a_dictionary[x], a_dictionary))
#     max_value = max(values)
#     best_keys = list(filter(lambda x: a_dictionary[x] == max_value, a_dictionary))
#     return best_keys[0]

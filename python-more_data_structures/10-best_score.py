#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    
    values = list(map(lambda x: a_dictionary[x], a_dictionary))
    max_value = max(values)
    best_keys = list(filter(lambda x: a_dictionary[x] == max_value, a_dictionary))
    return best_keys[0]

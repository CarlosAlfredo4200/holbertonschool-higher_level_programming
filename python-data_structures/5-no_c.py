#!/usr/bin/env python3
def no_c(my_string):
    newString = my_string.translate({ord('c'): None, ord('C'): None})
    return newString

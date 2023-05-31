#!/usr/bin/python3
def remove_char_at(str, n):
    newStr = "".join([str[i] for i in range(len(str)) if i != n])
    return newStr

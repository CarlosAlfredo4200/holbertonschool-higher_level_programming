#!/usr/bin/python3
def uppercase(str):
    uppercase_str = ""
    for char in str:
        if 'a' <= char <= 'z':
            uppercase_char = chr(ord(char) - ord('a') + ord('A'))
        else:
            uppercase_char = char
        uppercase_str += uppercase_char
    print(uppercase_str)

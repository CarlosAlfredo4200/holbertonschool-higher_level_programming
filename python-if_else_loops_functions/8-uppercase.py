#!/usr/bin/python3
def uppercase(str):
    uppercase_str = ""
    for i in range(len(str)):
        char = ord(str[i])
        uppercase_char = chr(char - 32) if 97 <= char <= 122 else chr(char)
        uppercase_str += uppercase_char
    print(uppercase_str)

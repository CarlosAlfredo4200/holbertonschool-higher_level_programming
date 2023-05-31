#!/usr/bin/python3
def uppercase(str):
    for item in range(len(str)):
        upper = ord(str(item) - 32) if 97 <= ord(item) <= 122 else item
        print(upper, end='')
    print()

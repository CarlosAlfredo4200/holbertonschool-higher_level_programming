#!/usr/bin/python3
for item in range(99):
    if len(str(item)) == 1:
        print('0{}, '.format(item), end="")
    else:
        print('{}, '.format(item), end="")

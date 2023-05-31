#!/usr/bin/python3
for item in range(122, 96, -1):
    if item % 2 == 0:
        chart = chr(item)
    else:
        chart = chr(item - 32)
    print("{}".format(chart), end="")

#!/usr/bin/python3
import sys

def print_arguments(argv):
    num_arguments = len(argv)

    if num_arguments == 0:
        print("0 arguments.")
    else:
        print("{} argument(s):".format(num_arguments))
        for i in range(num_arguments):
            print(f"{i+1}: {argv[i]}")


if __name__ == "__main__":
    print_arguments(sys.argv[1:])

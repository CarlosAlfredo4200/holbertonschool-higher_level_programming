#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    num_arguments = len(sys.argv)-1

    if num_arguments == 0:
        print("0 arguments.")
    elif num_arguments == 0:
        print("1 argument:")
    else:
        print(f"{num_arguments} argument(s):")
    for item in range(num_arguments):
        print(f"{item+1}: {sys.argv[item+1]}")
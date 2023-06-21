#!/usr/bin/python3
"""a function that writes a string to a text file (UTF8)"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF-8) number of characters written."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
        return len(text)

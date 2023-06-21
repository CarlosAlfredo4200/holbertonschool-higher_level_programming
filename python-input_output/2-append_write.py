#!/usr/bin/python3
"""a function that writes a string to a text file (UTF8)"""


def append_write(filename="", text=""):
    """Writes a string to a text file (UTF-8) number of characters written."""
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)
        return len(text)

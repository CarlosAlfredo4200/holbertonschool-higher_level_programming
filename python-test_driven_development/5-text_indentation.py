#!/usr/bin/python3
""" a function that prints a text with 2 new lines """


def text_indentation(text):
    """Prints text add two newlines
    after each of these characters {'.', '?', ':'}.
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    punctuation_marks = ['.', '?', ':']
    lines = text.splitlines()
    for line in lines:
        for mark in punctuation_marks:
            line = line.replace(mark, mark + "\n\n")
        print(line.strip())

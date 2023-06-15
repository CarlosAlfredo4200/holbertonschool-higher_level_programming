#!/usr/bin/python3
""" a function that prints a text with 2 new lines """


def text_indentation(text):
    """Prints text with added two newlines
    after each of these characters {'.', '?', ':'}.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for caracters in ".:?":
        text = (caracters + "\n\n").join(
            [line.strip(" ") for line in text.split(caracters)])

    print("{}".format(text), end="")

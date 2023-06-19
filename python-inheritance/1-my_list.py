#!/usr/bin/python3
"""a class MyList that inherits """


class MyList(list):
    """
        Prints the list in sorted order (ascending sort).
        Returns:
        list: newList ascending sort

        """

    def print_sorted(self):
        newList = sorted(self)
        print(newList)

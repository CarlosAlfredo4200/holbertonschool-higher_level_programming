#!/usr/bin/python3
"""a class MyList that inherits from list:"""


class MyList(list):
    """
        Prints the list in sorted order (ascending sort).
        Returns:
        list: newList ascending sort

        """
    pass


    def print_sorted(self):
        newList = sorted(self)
        print(newList)

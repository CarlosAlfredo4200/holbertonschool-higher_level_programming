#!/usr/bin/python3

import sys
from typing import List
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_arguments_to_list(arguments: List[str]) -> List[str]:
    try:

        existing_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        existing_list = []

    updated_list = existing_list + arguments

    save_to_json_file(updated_list, "add_item.json")

    return updated_list


if __name__ == "__main__":

    arguments = sys.argv[1:]
    added_items = add_arguments_to_list(arguments)
    print("Items added to the list:", added_items)

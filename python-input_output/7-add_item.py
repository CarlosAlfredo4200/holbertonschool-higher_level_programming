#!/usr/bin/python3
"""a script that adds all arguments to a Python list"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

""" Load existing data from file if it exists"""
try:
    data = load_from_json_file("add_item.json")
except FileNotFoundError:
    data = []

""" Add command-line arguments to the list"""
data.extend(sys.argv[1:])

""" Save the updated data to the file"""
save_to_json_file(data, "add_item.json")

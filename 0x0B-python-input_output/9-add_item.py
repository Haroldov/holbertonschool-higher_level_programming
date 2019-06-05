#!/usr/bin/python3
import json
from sys import argv
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

try:
    l = load_from_json_file("add_item.json")
    l += argv[1:]
except:
    l = argv[1:]
save_to_json_file(l, "add_item.json")

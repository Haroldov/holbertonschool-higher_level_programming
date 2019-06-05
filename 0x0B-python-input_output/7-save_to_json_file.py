#!/usr/bin/python3
import json
""" doc """


def save_to_json_file(my_obj, filename):
    """ doc """

    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))

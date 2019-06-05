#!/usr/bin/python3
import json
""" doc """


def load_from_json_file(filename):
    """ doc """
    with open(filename, 'r') as f:
        return json.load(f)

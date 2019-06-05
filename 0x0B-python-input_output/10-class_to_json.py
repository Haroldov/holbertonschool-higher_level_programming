#!/usr/bin/python3
import json
""" doc """


def class_to_json(obj):
    """ doc """
    return json.dumps(obj.__dict__)

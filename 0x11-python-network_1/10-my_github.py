#!/usr/bin/python3
""" doc """

import requests
import sys

if __name__ == '__main__':
    url = "https://api.github.com/user"
    res = requests.get(url, auth=(sys.argv[1], sys.argv[2]))
    try:
        des = res.json()
        if len(des) == 0:
            print("No result")
        else:
            print(des.get("id"))
    except ValueError:
        print("Not a valid JSON")

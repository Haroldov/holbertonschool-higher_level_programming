#!/usr/bin/python3
""" doc """

import requests
import sys

if __name__ == '__main__':
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) == 2:
        data = {'q': sys.argv[1]}
    else:
        data = {'q': ''}
    res = requests.post(url, data=data)
    try:
        des = res.json()
        if len(des) == 0:
            print("No result")
        else:
            print("[{}] {}".format(des.get("id"), des.get("name")))
    except ValueError:
        print("Not a valid JSON")

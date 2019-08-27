#!/usr/bin/python3
""" doc """

import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    res = requests.get(url)
    try:
        res.raise_for_status()
        print(res.text)
    except:
        print("Error code: {}".format(res.status_code))

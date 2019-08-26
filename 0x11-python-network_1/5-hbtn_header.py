#!/usr/bin/python3
""" doc """

import requests
import sys

if __name__ == '__main__':
    res = requests.get(sys.argv[1])
    print(res.headers.get('X-Request-Id'))

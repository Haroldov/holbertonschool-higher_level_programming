#!/usr/bin/python3
""" doc """

from sys import argv
import urllib.request
with urllib.request.urlopen(argv[1]) as response:
    html = response.info()
    print(dict(html)['X-Request-Id'])

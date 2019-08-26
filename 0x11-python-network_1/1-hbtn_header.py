#!/usr/bin/python3
""" doc """

import sys
import urllib.request

if __name__ == '__main__':
    with urllib.request.urlopen(sys.argv[1]) as response:
        html = response.info()
        print(dict(html)['X-Request-Id'])

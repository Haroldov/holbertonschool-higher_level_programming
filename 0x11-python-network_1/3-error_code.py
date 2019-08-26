#!/usr/bin/python3
""" doc """

from urllib import request, parse, error
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    req = request.Request(url)
    try:
        with request.urlopen(req) as response:
            the_page = response.read()
            print(the_page.decode())
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))

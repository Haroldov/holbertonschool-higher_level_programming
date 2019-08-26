#!/usr/bin/python3
""" doc """

import requests

if __name__ == '__main__':
    res = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(res.text)))
    print("\t- content: {}".format(res.content.decode()))

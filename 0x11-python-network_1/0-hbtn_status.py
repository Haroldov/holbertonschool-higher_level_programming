#!/usr/bin/python3
""" doc """

import urllib.request
with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    html = response.read()
    print('Body response:')
    print('\t- type: {}'.format(type(html)))
    print('\t- content:', html)
    print('\t- utf8 content', html.decode())

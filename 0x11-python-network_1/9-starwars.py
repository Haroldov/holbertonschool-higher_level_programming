#!/usr/bin/python3
""" doc """

import requests
import sys

if __name__ == '__main__':
    url = "https://swapi.co/api/people/"
    if len(sys.argv) == 2:
        data = {'search': sys.argv[1]}
    else:
        data = {'search': ''}
    res = requests.get(url, params=data)
    try:
        des = res.json()
        if len(des) == 0:
            print("No result")
        else:
            print("Number of results: {}".format(des.get("count")))
            results = des.get("results")
            for json in results:
                print(json.get("name"))
    except ValueError:
        print("Not a valid JSON")

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
                for film in json.get("films"):
                    name = requests.get(film).json().get("title")
                    print("\t{}".format(name))
            while (des.get("next") is not None):
                des = requests.get(des.get("next")).json()
                for json in des.get("results"):
                    print(json.get("name"))
                    for film in json.get("films"):
                        name = requests.get(film).json().get("title")
                        print("\t{}".format(name))

    except ValueError:
        print("Not a valid JSON")

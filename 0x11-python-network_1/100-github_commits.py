#!/usr/bin/python3
""" doc """

import requests
import sys

if __name__ == '__main__':
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])
    res = requests.get(url)
    try:
        des = res.json()
        if len(des) == 0:
            print("No result")
        else:
            for i, info in enumerate(des):
                print("{}: {}".format(info.get("sha"),
                                      info.get("commit").get("author").
                                      get("name")))
                if i == 9:
                    break
    except ValueError:
        print("Not a valid JSON")

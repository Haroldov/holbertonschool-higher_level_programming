#!/usr/bin/python3
import signal
import sys


try:
        count = 0
        status = {}
        size = 0
        possStatus = ["200", "301", "400", "401", "403", "404", "405", "500"]
        for line in sys.stdin:
                tmpStatus = line.split(' ')[-2]
                if tmpStatus in status.keys():
                        count += 1
                        size += int(line.split(' ')[-1][:-1])
                        status.update({tmpStatus: status.get(tmpStatus) + 1})
                elif tmpStatus in possStatus:
                        count += 1
                        size += int(line.split(' ')[-1][:-1])
                        status.update({tmpStatus: 1})
                if (count == 10):
                        count = 0
                        print("File size: {}".format(size))
                        tmpDic = sorted(status.items(), key=lambda t: t[0])
                        for key, val in tmpDic:
                                print("{}: {}".format(key, val))
except KeyboardInterrupt as e:
        print("File size: {}".format(size))
        tmpDic = sorted(status.items(), key=lambda t: t[0])
        for key, val in tmpDic:
                print("{}: {}".format(key, val))
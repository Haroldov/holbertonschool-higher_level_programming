#!/usr/bin/python3
import signal
import sys


try:
        count = 0
        status = {}
        size = 0
        for line in sys.stdin:
                count += 1
                size += int(line.split(' ')[-1][:-1])
                tmpStatus = line.split(' ')[-2]
                if tmpStatus in status.keys():
                        status.update({tmpStatus: status.get(tmpStatus) + 1})
                else:
                        status.update({tmpStatus: 1})
                if (count == 10):
                        count = 0
                        print("File size: {}".format(size))
                        for key, val in status.items():
                                print("{}: {}".format(key, val))
except KeyboardInterrupt as e:
        print("File size: {}".format(size))
        for key, val in status.items():
                print("{}: {}".format(key, val))
        raise e

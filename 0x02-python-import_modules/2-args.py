#!/usr/bin/python3
from sys import argv
i = 1

if __name == "__main__":
    if len(argv) == 1:
        print("0 arguments.")
    elif len(argv) == 2:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    else:
        print("{:d} arguments:".format(len(argv) - 1))
        while i < len(argv):
            print("{:d}: {:s}".format(i, argv[i]))
            i += 1

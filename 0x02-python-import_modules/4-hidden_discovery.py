#!/usr/bin/python3

import hidden_4

if __name__ = "__main__":
    names = dir(hidden_4)
    for nh in names:
        if nh.find("_") != 0:
            print(nh)

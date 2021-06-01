#!/usr/bin/python3
"""
Module for append_after method.
"""


def append_after(filename="", search_string="", new_string=""):
    '''Method for inserting text after search string.'''
    lines = []
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()
        i = 0
        while i < len(lines):
            if search_string in lines[i]:
                lines[i:i + 1] = [lines[i], new_string]
                i += 1
            i += 1
    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(lines)

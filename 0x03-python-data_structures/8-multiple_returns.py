#!/usr/bin/python3


def multiple_returns(sentence):
    """Returns tuple with len of string and first char"""
    length = len(sentence)
    if sentence:
        first = sentence[0]
    else:
        first = None
    return (length, first)

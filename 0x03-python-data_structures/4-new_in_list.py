#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    """Makes copy of a list, replce element at certain index in copy
       while leaving originial unmodified.
    """
    if idx < 0 or idx > len(my_list) - 1:
        return my_list[:]
    else:
        new_list = my_list[:]
        new_list[idx] = element
        return new_list
    

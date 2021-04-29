#!/usr/bin/python3

if __name == "__main__":
    import sys
    argv = sys.argv[1:]
    arg_num = len(argv)
    i = 1
    if arg_num == 0:
        print("{:d} arguments.".format(arg_num))
    elif arg_num == 1:
        print("{:d} argument.".format(arg_num))
        print("{:d}: {:s}".format(i, sys.argv[1]))
    else:
        print("{:d} arguments.".format(arg_num))
        while i < arg_num:
            print("{:d}: {:s}".format(i, sys.argv[i]))
            i += 1

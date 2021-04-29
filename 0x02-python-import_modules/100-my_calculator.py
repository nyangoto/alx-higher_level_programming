#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ == '__main__':
    arg_num = len(argv) - 1
    if arg_num != 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    elif argv[2] not in '+-*/':
        print('Unknown operator. Available operators: +, -, *, and /')
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        if argv[2] == '+':
            print('{:d} + {:d} = {:d}'.format(a, b, add(a, b)))
        elif argv[2] == '-':
            print('{:d} - {:d} = {:d}'.format(a, b, sub(a, b)))
        elif argv[2] == '*':
            print('{:d} * {:d} = {:d}'.format(a, b, mul(a, b)))
        else:
            print('{:d} / {:d} = {:d}'.format(a, b, div(a, b)))

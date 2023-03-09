#!/usr/bin/python3

from calculator_1 import *
from sys import argv, exit

if __name__ == '__main__':
    operators = ['+', '-', '*', '/']

    args = argv[1:]
    arg_num = len(argv) - 1

    if arg_num != 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)

    if args[1] not in operators:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)

    a = int(args[0])
    b = int(args[2])
    op = args[1]

    if args[1] == '+':
        result = add(a, b)
    if args[1] == '-':
        result = sub(a, b)
    if args[1] == '*':
        result = mul(a, b)
    if args[1] == '/':
        result = div(a, b)

    print('{} {} {} = {}'.format(a, op, b, result))

#!/usr/bin/python3
from sys import argv

if __name__ == '__main__':
    arg_len = len(argv) 

    # special conditions for argument lengths 1, 2 or more
    if arg_len == 1:
        print('{} arguments.'.format(arg_len - 1))
    elif arg_len == 2:
        print('{} argument:'.format(arg_len - 1))
    else:
        print('{} arguments:'.format(arg_len - 1))


    for i, arg in enumerate(argv):
        if i != 0:
            print('{}: {}'.format(i, arg))

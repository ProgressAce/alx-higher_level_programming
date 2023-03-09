#!/usr/bin/python3

from sys import argv

if __name__ == '__main__':
    result = 0

    for arg in argv:
        if arg != argv[0]:
            result += int(arg)

    print(result)

#!/usr/bin/python3
def uppercase(str1):
    for letter in str1:
        code = ord(letter)
        if code >= 97 and code <= 122:
            code -= 32

        print('{:c}'.format(code), end='')

    print('')

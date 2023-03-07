#!/usr/bin/python3
def uppercase(str1):
    for letter in str1:
        code = ord(letter)
        if code >= 97 and code <= 122:
            print('{:c}'.format(code - 32), end='')
        else:
            print('{}'.format(letter), end='')
    print(f'')

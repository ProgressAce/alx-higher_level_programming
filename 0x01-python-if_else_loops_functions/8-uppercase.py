#!/usr/bin/python3
def uppercase(str1):
    for letter in str1:
        code = ord(letter)
        if code >= 97 and code <= 122:
            print(f'{chr(code - 32)}', end='')
        else:
            print(f'{letter}', end='')
    print()

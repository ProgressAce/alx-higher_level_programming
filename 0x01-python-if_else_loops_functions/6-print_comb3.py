#!/usr/bin/python3
for x in range(10):
    for y in range(10):
        if x == 8 and y == 9:
            print(f'{x}{y}')
        elif y > x:
            print(f'{x}{y}, ', end='')

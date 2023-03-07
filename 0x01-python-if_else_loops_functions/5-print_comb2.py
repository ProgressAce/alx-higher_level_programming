#!/usr/bin/python3
for num in range(100):
    if num == 99:
        print(num)
    else:
        print(f'{num:02}, ', end='')  # print width of 2 spaces

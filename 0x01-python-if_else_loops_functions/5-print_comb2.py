#!/usr/bin/python3
for num in range(100):
    if num == 99:
        print('{}'.format(num))
    else:
        print('{:02}, '.format(num), end='')  # print width of 2 spaces

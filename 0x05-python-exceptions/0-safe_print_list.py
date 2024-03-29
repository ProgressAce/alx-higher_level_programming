#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Prints x elements of a list, printed on the same line"""
    count = 0

    for i in range(x):
        try:
            print(f'{my_list[i]}', end="")
            count += 1
        except IndexError:
            break

    print()

    return (count)

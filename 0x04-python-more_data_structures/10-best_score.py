#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is {}:
        return a_dictionary

    score = 0
    name = ''

    for key, value in a_dictionary.items():
        if score < value:
            score = value
            name = key

    return name

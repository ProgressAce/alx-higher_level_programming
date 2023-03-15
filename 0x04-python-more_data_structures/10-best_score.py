#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None

    score = 0
    name = ''

    for key, value in a_dictionary.items():
        if score < value:
            score = value
            name = key

    return name

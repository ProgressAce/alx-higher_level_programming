#!/usr/bin/python3
def multiple_returns(sentence):
    sentence_len = len(sentence)

    if sentence_len == 0:
        first_char = None
    else:
        first_char = sentence[0]

    return (sentence_len, first_char)

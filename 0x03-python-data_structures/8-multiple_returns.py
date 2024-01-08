#!/usr/bin/python3

def multiple_returns(sentence):
    my_tp = ()
    if len(sentence) > 0:
        my_tp = len(sentence), sentence[0]
    else:
        my_tp = (0, "None")
    return my_tp

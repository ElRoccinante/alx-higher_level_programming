#!/usr/bin/python3
def multiple_returns(sentence):
    mult_tuple = ()
    if len(sentence) == 0:
        mult_tuple = 0, "None"
    else:
        mult_tuple = len(sentence), sentence[0]
    return mult_tuple

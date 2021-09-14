#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) is None:
        return None
    else:
        return len(sentence), sentence[0]

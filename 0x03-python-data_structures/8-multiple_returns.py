#!/usr/bin/python3
def multiple_returns(sentence):
    leng = len(sentence)
    void = None
    if sentence != "":
        void = sentence[0]
    return leng, void

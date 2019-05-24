#!/usr/bin/python3
def text_indentation(text):

    indTmp = 0
    sw = 1
    for ind, letter in enumerate(text):
        if letter not in " " and sw == 1:
            indTmp = ind
            sw = 0
        if letter in ":?.":
            print(text[indTmp:ind + 1] + '\n')
            sw = 1
    if text[indTmp] not in ":?.":
        print(text[indTmp:ind + 1], end="")

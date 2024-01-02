#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if 'a' <= char <= 'z':
            upper = chr(ord(char) - ord('a') + ord('A'))
        else:
            upper = char
        print("{}".format(upper), end='')
    print()

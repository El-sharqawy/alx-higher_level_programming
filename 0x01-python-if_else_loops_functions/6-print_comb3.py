#!/usr/bin/python3
for i in range(10):
    for j in range(i + 1, 10):
        if i != 8 or j != 9:
            print("{:02}, ".format(i * 10 + j), end='')
        else:
            print("{:02}".format(i * 10 + j))

#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list is None:
        return 0

    result = 0
    div = 0
    val = 0
    add = [element[0] * element[1] for element in my_list]
    divine = [element[1] for element in my_list]
    for item in add:
        val += item
    for item in divine:
        div += item
    result = float(val/div)
    return result

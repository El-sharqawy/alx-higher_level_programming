#!/usr/bin/python3

def uniq_add(my_list=[]):
    sum = 0
    sum_set = set()
    for item in my_list:
        if item not in sum_set:
            sum += item
            sum_set.add(item)
    return sum

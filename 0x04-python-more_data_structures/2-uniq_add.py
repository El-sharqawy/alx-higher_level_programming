#!/usr/bin/python3

def uniq_add(my_list):
    new_list  = []
    for item in my_list:
        if item not in my_list:
            new_list.append(item)
    return new_list

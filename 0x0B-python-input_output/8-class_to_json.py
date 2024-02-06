#!/usr/bin/python3
"""
Class to JSON
"""


def class_to_json(obj):
    """ a function that returns dict of obj"""
    result = if hasattr(obj, "__dict__"):
        result = obj.__dict__.copy()
    return (result)

#!/usr/bin/python3
"""
This module includes a function that prints two new lines after encountering the characters ".?:"
"""

def text_indentation(text):
    """ a function that prints two new lines after encountering the characters ".?:"

    Args:
        test: an input string

    Return:
        Nothing.

    Raises:
        TypeError: If text is not a string
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    string = text[:]
    for word in ".?:":
        text_list = string.split(word)
        string = ""
        for i in text_list:
            i = i.strip(" ")
            string = i + word if string is "" else string + "\n\n" + i + word

    print(string[:-3], end="")

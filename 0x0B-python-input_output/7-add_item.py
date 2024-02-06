#!/usr/bin/python3
"""
Load, add, save function
"""
import sys
stjf = __import__('5-save_to_json_file').save_to_json_file
lfjf = __import__('6-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    try:
        items = lfjf("add_item.json")
    except FileNotFoundError:
        items = []
    items.extend(sys.argv[1:])
    stjf(items, "add_item.json")

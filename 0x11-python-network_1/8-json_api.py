#!/usr/bin/python3
""" a Python script that takes in a letter,
    sends a POST request to url with the letter
    as parameter, then displays the body of response
"""
import sys
import requests


if __name__ == '__main__':
    val = ""
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) > 1:
        val = sys.argv[1]
    obj = {'q': val}
    response = requests.post(url, data=obj)
    try:
        jsonData = response.json()
        if jsonData:
            print(f"[{jsonData.get('id')}] {jsonData.get('name')}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")

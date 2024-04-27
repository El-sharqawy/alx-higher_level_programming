#!/usr/bin/python3
""" a Python script that fetches a given URL
    and displays the body of the response
"""
import requests
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    response = requests.get(url)
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(f"{response.text}")

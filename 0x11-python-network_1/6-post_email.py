#!/usr/bin/python3
""" a Python script that takes URL, email,
    sends a POST request and displays the
    body of the response.
"""
import requests
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}
    response = requests.post(url, data=data)
    print(response.text)

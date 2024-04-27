#!/usr/bin/python3
""" a Python script that takes URL,
    sends a request and displays the
    value of the variable X-Request-Id
"""
import requests
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    response = requests.get(url)
    request_id = response.headers.get('X-Request-Id')
    if request_id:
        print(request_id)

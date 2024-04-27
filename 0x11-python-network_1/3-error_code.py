#!/usr/bin/python3
""" a Python script that takes URL, sends
    a request to it and displays the body
    of the response (decoded in utf8)
"""
import sys
import urllib.request


if __name__ == '__main__':
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.request.HTTPError as err:
        print(f"Error code: {err.code}")

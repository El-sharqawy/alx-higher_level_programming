#!/usr/bin/python3
""" a Python script that takes URL
    sends a request to URL and display
    the value of X-Request-Id Variable found.
"""
import sys
import urllib.request

if __name__ == '__main__':
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        request_id = response.getheader('X-Request-Id')
        if request_id:
            print(request_id)

#!/usr/bin/python3
""" a Python script that takes URL and email,
    sends a POST request to the passed URL,
    with email as a parameter and display the response
"""
import sys
import urllib.parse
import urllib.request

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    request = urllib.request.Request(url, data = data, method='POST')
    with urllib.request.urlopen(request) as response:
        body = response.read().decode('utf-8')
        print(f"Your email is: {body}")

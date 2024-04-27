#!/usr/bin/python3
""" a Python script that fetches a given URL
    and displays the body of the response
"""
import requests
import sys


url = sys.argv[1]
response = requests.get(url)
response.raise_for_status()
if response.status_code >= 400:
    print(f"Error code: {response.status_code}")
else:
    print(f"{response.text}")

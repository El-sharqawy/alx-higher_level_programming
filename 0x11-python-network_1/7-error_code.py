#!/usr/bin/python3
""" a Python script that fetches a given URL
    and displays the body of the response
"""
import requests
import sys


url = sys.argv[1]
try:
    response = requests.get(url)
    response.raise_for_status()
    print(f"{response.text}")
except requests.HTTPError as err:
    print(f"Error code: {err.response.status_code}")

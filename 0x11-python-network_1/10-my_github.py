#!/usr/bin/python3
""" a Python script that takes GitHub credentials
    and uses the GitHub API to display your ID
"""
import sys
import requests


if __name__ == '__main__':
    username = sys.argv[1]
    token = sys.argv[2]

    gitHubUrl = 'https://api.github.com/user'
    response = requests.get(gitHubUrl, auth=(username, token))
    data = response.json()
    if data:
        print(f"{data.get('id')}")
    else:
        print("None")

#!/usr/bin/python3
""" a Python script that takes GitHub credentials
    and uses the GitHub API to display commits data
"""
import sys
import requests


if __name__ == '__main__':
    r = sys.argv[1]
    u = sys.argv[2]

    gitHubUrl = f"https://api.github.com/repos/{u}/{r}/commits"
    response = requests.get(gitHubUrl)
    data = response.json()
    for commit in range(10):
        print(f"{data[commit].get('sha')}: {data[commit]['commit']['author']['name']}")

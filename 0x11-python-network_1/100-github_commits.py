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
    try:
        for i in range(10):
            print("{}: {}".format(
                data[i].get("sha"),
                data[i].get("commit").get("author").get("name")))
    except IndexError:
        pass

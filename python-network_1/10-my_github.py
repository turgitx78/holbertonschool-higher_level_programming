#!/usr/bin/python3
"""
Uses GitHub API with Basic Authentication to display the user id.
"""
import sys
import requests


def main():
    username = sys.argv[1]
    token = sys.argv[2]

    r = requests.get(
        "https://api.github.com/user",
        auth=(username, token)
    )

    try:
        print(r.json().get("id"))
    except ValueError:
        print(None)


if __name__ == "__main__":
    main()


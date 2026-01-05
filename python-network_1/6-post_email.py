#!/usr/bin/python3
"""
Takes a URL and an email address, sends a POST request with the email,
and displays the response body.
"""
import sys
import requests


def main():
    url = sys.argv[1]
    email = sys.argv[2]

    data = {'email': email}
    r = requests.post(url, data=data)

    print(r.text)


if __name__ == "__main__":
    main()

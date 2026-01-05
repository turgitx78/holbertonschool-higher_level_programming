#!/usr/bin/python3
"""
Takes a URL, sends a request, and displays the response body.
If the HTTP status code is >= 400, prints the error code.
"""
import sys
import requests


def main():
    r = requests.get(sys.argv[1])
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)


if __name__ == "__main__":
    main()

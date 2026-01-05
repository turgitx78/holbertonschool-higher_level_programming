#!/usr/bin/python3
"""
Takes a URL, sends a request, and displays the value
of the X-Request-Id header from the response.
"""
import sys
import requests


def main():
    r = requests.get(sys.argv[1])
    print(r.headers.get('X-Request-Id'))


if __name__ == "__main__":
    main()

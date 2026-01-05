#!/usr/bin/python3
"""
Takes a URL, sends a request, and displays the response body.
If an HTTP error occurs, prints the error code.
"""
import sys
from urllib import request, error


def main():
    try:
        with request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))


if __name__ == "__main__":
    main()

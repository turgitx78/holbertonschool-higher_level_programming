#!/usr/bin/python3
"""
Takes a URL and an email, sends a POST request with the email as a parameter,
and displays the response body decoded in utf-8.
"""
import sys
from urllib import request, parse


def main():
    url = sys.argv[1]
    email = sys.argv[2]

    data = parse.urlencode({'email': email}).encode('utf-8')

    with request.urlopen(url, data) as response:
        print(response.read().decode('utf-8'))


if __name__ == "__main__":
    main()

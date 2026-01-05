#!/usr/bin/python3
"""
Fetches https://intranet.hbtn.io/status using requests
and displays the response body details.
"""
import requests


def main():
    r = requests.get('https://intranet.hbtn.io/status')
    body = r.text

    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))


if __name__ == "__main__":
    main()

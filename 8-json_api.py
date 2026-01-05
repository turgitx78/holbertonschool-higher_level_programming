#!/usr/bin/python3
"""
Sends a POST request with a letter to a JSON API and
displays the result based on the JSON response.
"""
import sys
import requests


def main():
    url = "http://0.0.0.0:5000/search_user"
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    r = requests.post(url, data={'q': q})

    try:
        data = r.json()
    except ValueError:
        print("Not a valid JSON")
        return

    if not data:
        print("No result")
    else:
        print("[{}] {}".format(data.get('id'), data.get('name')))


if __name__ == "__main__":
    main()

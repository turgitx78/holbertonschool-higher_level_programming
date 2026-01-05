#!/usr/bin/python3
"""
Takes a URL, sends a request, and displays the value
of the X-Request-Id header from the response.
"""
import sys
from urllib import request

with request.urlopen(sys.argv[1]) as response:
    headers = response.headers
    print(headers.get('X-Request-Id'))

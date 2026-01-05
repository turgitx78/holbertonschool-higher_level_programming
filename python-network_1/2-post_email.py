#!/usr/bin/python3
"""
Takes a URL and an email, sends a POST request with the email,
and displays the response body decoded in utf-8.
"""
import sys
from urllib import request, parse

url = sys.argv[1]
email = sys.argv[2]

data = parse.urlencode({'email': email}).encode('utf-8')

with request.urlopen(url, data) as response:
    body = response.read()

print(body.decode('utf-8'))

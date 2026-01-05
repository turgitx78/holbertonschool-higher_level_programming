#!/usr/bin/python3
"""
Fetches https://intranet.hbtn.io/status using urllib
and displays the response body details.
"""
from urllib import request

with request.urlopen('https://intranet.hbtn.io/status') as response:
    body = response.read()

print("Body response:")
print("\t- type: {}".format(type(body)))
print("\t- content: {}".format(body))
print("\t- utf8 content: {}".format(body.decode('utf-8')))

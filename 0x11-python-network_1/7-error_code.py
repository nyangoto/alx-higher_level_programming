#!/usr/bin/python3
"""Take a URL, sends requests ans analyzes HTTP status code"""

import requests
from sys import argv

if __name__ == '__main__':
    response = requests.get(argv[1])
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)

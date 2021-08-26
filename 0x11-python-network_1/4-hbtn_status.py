#!/usr/bin/python3
""" Uses requests module to fetch URL status"""

import requests

if __name__ == '__main__':
    response = requests.get('https://intranet.hbtn.io/status')
    print("Body response:\n\t- type: {}\n\t- content: {}"
          .format(type(response.text), response.text))

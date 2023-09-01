#!/usr/bin/python3
"""Sends a request to the URL and displays the body of the response.
 - Exceptions are managed with urllib.error.HTTPError"""


if __name__ == '__main__':
    from urllib import error
    from urllib import request
    from sys import argv

    try:
        with request.urlopen(argv[1]) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as e:
        print(e.code)

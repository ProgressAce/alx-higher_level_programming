#!/usr/bin/python3
"""Accepts a URL arg and sends a GET request to the URL and
prints the value of the 'X-Request-Id' header of the HTTP response"""


if __name__ == '__main__':
    from urllib import request
    from sys import argv

    with request.urlopen(argv[1]) as response:
        print(response.getheader('X-Request-Id'))

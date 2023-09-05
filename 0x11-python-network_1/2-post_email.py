#!/usr/bin/python3
"""Sends a POST Request to a URL taken as an argument.
 - with an email argument
 - display the body of the response."""


if __name__ == '__main__':
    from urllib import request, parse
    from sys import argv

    # format the data
    data = {'email': argv[2]}
    url_str = parse.urlencode(data)
    byte_data = url_str.encode('ascii')

    req = request.Request(argv[1], byte_data)
    with request.urlopen(req) as response:
        body = response.read()
        print(body.decode('utf-8'))

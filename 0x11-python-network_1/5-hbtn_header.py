#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and displays the value of
the variable X-Request-Id in the response header.
 - Uses the 'requests' and 'sys' packages.
 - the value of this variable is different with every request."""


if __name__ == '__main__':
    from sys import argv
    import requests

    r = requests.get(argv[1])
    print(r.headers['X-Request-Id'])

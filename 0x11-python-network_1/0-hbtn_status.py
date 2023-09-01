#!/usr/bin/python3
"""Py script that
 - fetches https://alx-intranet.hbtn.io/status
 - uses the urllib."""


if __name__ == '__main__':
    from urllib import request

    with request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        html = res.read()
        print('Body response:')
        print('\t- type: {}'.format(type(html)))
        print('\t- content: '.format(html))
        print('\t- utf8 content: '.format(html.decode('utf-8')))

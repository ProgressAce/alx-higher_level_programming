#!/usr/bin/python3
"""Py script that fetches https://alx-intranet.hbtn.io/status
 - Uses the 'requests' package"""


if __name__ == '__main__':
    import requests

    r = requests.get('https://alx-intranet.hbtn.io/status')
    print('Body content:')
    print('\t- type: {}'.format(type(r.text)))
    print('\t- content: {}'.format(r.text))

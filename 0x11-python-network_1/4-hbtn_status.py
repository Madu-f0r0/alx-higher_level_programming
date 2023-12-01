#!/usr/bin/python3
""" fetches `https://alx-intranet.hbtn.io/status` using `request` package """

if __name__ == '__main__':
    import requests

    r = requests.get('https://alx-intranet.hbtn.io/status')
    print('Body response')
    print('\t- type', r.text.__class__)
    print('\t- content:', r.text)

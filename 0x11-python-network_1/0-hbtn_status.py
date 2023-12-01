#!/usr/bin/python3
"""This script fetches `https://alx-intranet.hbtn.io/status`"""

if __name__ == '__main__':
    import urllib.request

    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        the_page = response.read()
        print('Body response:')
        print('\t- type:', type(the_page))
        print('\t- content:', the_page)
        print('\t- utf8 content:', the_page.decode('utf-8'))

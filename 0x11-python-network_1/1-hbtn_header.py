#!/usr/bin/python3
"""Displays the `X-Request-Id` variable found in the header of a
server response to a URL request
"""

if __name__ == '__main__':
    import sys
    import urllib.request

    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.info()['X-Request-Id'])

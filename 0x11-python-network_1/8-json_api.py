#!/usr/bin/python3
""" takes in a letter and sends a POST request to
`http://0.0.0.0:5000/search_user` with the letter as a parameter
"""

if __name__ == '__main__':
    import requests
    import sys

    url = 'http://0.0.0.0:5000/search_user'
    q = "" if len(sys.argv) < 2 else sys.argv[1]

    r = requests.post(url, data={'q': q})
    try:
        json_data = r.json()
        if json_data == {}:
            print('No result')
        else:
            print(f'[{json_data["id"]}] {json_data["name"]}')
    except requests.exceptions.JSONDecodeError:
        print('Not a valid JSON')


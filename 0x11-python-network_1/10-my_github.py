#!/usr/bin/python3
""" takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""

if __name__ == "__main__":
    import requests
    import sys
    from requests.auth import HTTPBasicAuth

    url = 'https://api.github.com/user'
    username = sys.argv[1]
    token = sys.argv[2]
    basic = HTTPBasicAuth(username, token)

    r = requests.get(url, auth=basic)
    print(r.json()['id'])

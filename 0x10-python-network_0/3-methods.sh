#!/bin/bash
# takes in a URL and displays all HTTP methods the server will accept

url=$1
curl -Is $url | grep "Allow:" | cut -d ":" -f 2 | cut -c 2- | rev | cut -c 2- | rev

#!/usr/bin/python3
""" Script that adds all arguments to a Python list and saves

them to a JSON file
"""

import json
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

argList = os.sys.argv[1:]

if not os.path.exists('add_item.json'):
    save_to_json_file(argList, 'add_item.json')

else:
    jsonList = load_from_json_file('add_item.json')
    jsonList = jsonList + argList
    save_to_json_file(jsonList, 'add_item.json')

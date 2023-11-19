#!/usr/bin/python3
"""This module contains a script that lists all states with name matching
a string passed in the CL from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states \
                WHERE name = '{}' \
                ORDER BY id ASC".
                format(argv[4]))
    all_states = cur.fetchall()
    for state in all_states:
        print(state)

    cur.close()
    db.close()

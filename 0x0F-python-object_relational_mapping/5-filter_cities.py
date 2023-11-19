#!/usr/bin/python3
"""This module lists all cities of a specified state
from database `hbtn_0e_4_usa`
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT c.name \
                FROM cities AS c \
                INNER JOIN states AS s \
                ON c.state_id = s.id \
                WHERE s.name = %s \
                ORDER BY c.id ASC", (argv[4],))
    values = cur.fetchall()
    cities = []
    for tup in values:
        cities.append(tup[0])
    cities = tuple(cities)
    print(", ".join(cities))

    cur.close()
    db.close()

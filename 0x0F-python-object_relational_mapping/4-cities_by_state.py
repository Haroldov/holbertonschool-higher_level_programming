#!/usr/bin/python3
""" doc """

import MySQLdb
from sys import argv

if __name__ == "__main__":
    if len(argv) == 4:
        db = MySQLdb.connect(user=argv[1], passwd=argv[2],
                             port=3306, host='localhost', db=argv[3])
        cursor = db.cursor()
        query = "SELECT cities.id, cities.name, states.name FROM cities\
        INNER JOIN states ON states.id = cities.state_id\
        ORDER BY cities.id;"
        cursor.execute(query)
        for row in cursor.fetchall():
            print(row)

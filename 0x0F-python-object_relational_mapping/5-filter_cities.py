#!/usr/bin/python3
""" doc """

import MySQLdb
from sys import argv

if __name__ == "__main__":
    if len(argv) == 5:
        db = MySQLdb.connect(user=argv[1], passwd=argv[2],
                             port=3306, host='localhost', db=argv[3])
        cursor = db.cursor()
        query = "SELECT cities.name FROM cities\
        INNER JOIN states ON states.id = cities.state_id\
        WHERE states.name='{}'\
        ORDER BY cities.id;".format(argv[4].split('\'')[0])
        cursor.execute(query)
        tmp = map(lambda x: x[0], cursor.fetchall())
        print(", ".join(tmp))

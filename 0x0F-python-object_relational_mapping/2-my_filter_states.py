#!/usr/bin/python3
# doc

import MySQLdb
from sys import argv

if __name__ == "__main__":
    if len(argv) == 5:
        db = MySQLdb.connect(user=argv[1], passwd=argv[2],
                             port=3306, host='localhost', db=argv[3])
        cursor = db.cursor()
        query = "SELECT * FROM states WHERE name='{}' ORDER BY id ASC".format(
            argv[4])
        cursor.execute(query)
        for row in cursor.fetchall():
            print(row)

#!/usr/bin/python3
# doc

import MySQLdb
from sys import argv

if __name__ == "__main__":
    if len(argv) == 4:
        db = MySQLdb.connect(user=argv[1], passwd=argv[2],
                             port=3306, host='localhost', db=argv[3])
        cursor = db.cursor()
        cursor.execute('SELECT * FROM states ORDER BY id ASC')
        for row in cursor.fetchall():
            print(row)

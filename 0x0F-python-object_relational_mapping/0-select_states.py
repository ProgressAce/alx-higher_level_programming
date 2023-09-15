#!/usr/bin/python3
"""Script that lists all the states of a specific database.

The script takes 3 arguments used for connecting to a MySQL database server
at localhost on port 3306: mysql username, password and database name."""

if __name__ == '__main__':
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(host='127.0.0.1', port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()

    cur.execute('SELECT * FROM states ORDER BY states.id;')
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()

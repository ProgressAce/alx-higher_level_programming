#!/usr/bin/python3
"""Script- Takes in a state as an argument and lists all cities matching it.

The script takes four arguments and connects to the database hbtn_0e_4_usa;
sorted according to cities.id in ascending order.
The args are:
    mysql username, password, database name and the state to search for."""

from sys import argv
import MySQLdb as DB

db = DB.connect(host='localhost', port=3306,
                user=argv[1], passwd=argv[2], db=argv[3])
cur = db.cursor()

cur.execute('SELECT name FROM cities WHERE state_id = \
            (SELECT id FROM states WHERE name = "{}") ORDER BY cities.id'
            .format(argv[4]))

records = cur.fetchall()
for i, rec in enumerate(records):
    if i == len(records) - 1:
        print(rec[0])
    else:
        print(rec[0], ', ', end='')

cur.close()
db.close()

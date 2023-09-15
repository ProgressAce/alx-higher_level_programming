#!/usr/bin/python3
"""Script- lists all the states from database hbtn_0e_0_usa starting with N

It takes three arguments for connecting to the mysql database server
on localhost vat port 3306.
They are:
    mysql username, password and database name."""

from sys import argv
import MySQLdb as DB

db = DB.connect(host='127.0.0.1', port=3306,
                user=argv[1], passwd=argv[2], db=argv[3])
cur = db.cursor()

cur.execute('SELECT * FROM states WHERE name LIKE "N%" ORDER BY states.id')
records = cur.fetchall()
for rec in records:
    print(rec)

cur.close()
db.close()

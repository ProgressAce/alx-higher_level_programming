#!/usr/bin/python3
"""Script- Lists all cities from the database.

The script takes three arguments and connects to the database hbtn_0e_4_usa;
sorted according to cities.id in ascending order.
The args are:
    mysql username, password, database name."""

if __name__ == '__main__':
    from sys import argv
    import MySQLdb as DB

    db = DB.connect(host='localhost', port=3306,
                    user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()

    cur.execute('SELECT * FROM cities ORDER BY cities.id')
    records = cur.fetchall()

    for rec in records:
        print(rec)

    cur.close()
    db.close()

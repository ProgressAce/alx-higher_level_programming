#!/usr/bin/python3
"""Script- takes an argument and finds all the records matching it in database

The script takes three arguments to connect to database hbtn_0e_0_usa,
on localhost at port 3306. They are:
    mysql username, password and database name."""

if __name__ == '__main__':
    from sys import argv
    import MySQLdb as DB

    db = DB.connect(host='localhost', port=3306,
                    user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()

    state = argv[4]
    cur.execute('SELECT * FROM states WHERE name="{}" ORDER BY states.id'
                .format(state))

    records = cur.fetchall()
    for rec in records:
        print(rec)

    cur.close()
    db.close()

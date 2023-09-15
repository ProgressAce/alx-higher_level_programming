#!/usr/bin/python3
"""Script- takes an argument and finds records matching the state from database

The script takes four arguments' connects to the database hbtn_0e_0_usa; and is
safe from SQL injections.
The args are:
    mysql username, password, database name and the state to search for."""

if __name__ == '__main__':
    from sys import argv
    import MySQLdb as DB

    db = DB.connect(host='localhost', port=3306,
                    user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()

    # shielding from sql injection
    if not argv[4].isalpha():
        exit()

    cur.execute('SELECT * FROM states WHERE name = "{}" ORDER BY states.id'
                .format(argv[4]))
    records = cur.fetchall()

    for rec in records:
        print(rec)

    cur.close()
    db.close()

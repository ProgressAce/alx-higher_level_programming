#!/usr/bin/python3
"""Script- lists all the states from database hbtn_0e_0_usa starting with N

It takes three arguments for connecting to the mysql database server
on localhost vat port 3306.
They are:
    mysql username, password and database name."""

if __name__ == '__main__':
    from sys import argv
    import MySQLdb as DB

    if len(argv) != 4:
        print('USAGE: ./1-filter_states.py <username> <password>',
              '<database_name>')
        exit()

    try:
        db = DB.connect(host='localhost', port=3306,
                        user=argv[1], passwd=argv[2], db=argv[3])
        cur = db.cursor()

        # SQL query uses LIKE BINARY for case sensitive selection
        cur.execute('SELECT * FROM states WHERE name LIKE BINARY "N%" \
                     ORDER BY states.id')
        records = cur.fetchall()
        for rec in records:
            print(rec)

    except DB.Error as e:
        print('MySQL errror: {}'.format(e))
    finally:
        cur.close()
        db.close()

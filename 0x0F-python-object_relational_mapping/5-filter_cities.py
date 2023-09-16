#!/usr/bin/python3
"""Script- Takes in a state as an argument and lists all cities matching it.

The script takes four arguments and connects to the database hbtn_0e_4_usa;
sorted according to cities.id in ascending order.
The args are:
    mysql username, password, database name and the state to search for."""

if __name__ == '__main__':
    from sys import argv
    import MySQLdb as DB

    if len(argv) != 5:
        print('USAGE: ./5-filter_cities.py <username> <password>',
              '<database_name> <state_name>')
        exit()

    try:
        db = DB.connect(host='localhost', port=3306,
                        user=argv[1], passwd=argv[2], db=argv[3])
        cur = db.cursor()

        # case sensitive state selection
        cur.execute('SELECT name FROM cities WHERE state_id = \
                    (SELECT id FROM states WHERE name LIKE BINARY "{}") \
                    ORDER BY cities.id'.format(argv[4]))

        records = cur.fetchall()
        for i, rec in enumerate(records):
            if i == len(records) - 1:
                print(rec[0])
            else:
                print(rec[0], ', ', end='')

        if len(records) == 0:
            print()

    except DB.Error as e:
        print('MySQL error: {}'.format(e))
    finally:
        cur.close()
        db.close()

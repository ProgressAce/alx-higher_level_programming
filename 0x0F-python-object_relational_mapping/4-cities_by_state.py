#!/usr/bin/python3
"""Script- Lists all cities from the database.

The script takes three arguments and connects to the database hbtn_0e_4_usa;
sorted according to cities.id in ascending order.
The args are:
    mysql username, password, database name."""

if __name__ == '__main__':
    from sys import argv
    import MySQLdb as DB

    if len(argv) != 4:
        print('USAGE: ./4-cities_by_state.py <username> <password>',
              '<database_name>')
        exit()

    try:
        db = DB.connect(host='localhost', port=3306,
                        user=argv[1], passwd=argv[2], db=argv[3])
    except DB.Error as e:
        print('MySQL error: {}'.format(e))
        exit()

    try:
        cur = db.cursor()

        cur.execute('SELECT c.id, c.name, s.name ' +
                    'FROM cities AS c, states AS s ' +
                    'WHERE c.state_id = s.id ' +
                    'ORDER BY c.id')

    except DB.Error as e:
        print('MySQL error: {}'.format(e))
        db.close()
        exit()

    records = cur.fetchall()

    for rec in records:
        print(rec)

    cur.close()
    db.close()

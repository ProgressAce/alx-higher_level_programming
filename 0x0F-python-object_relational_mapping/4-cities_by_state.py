#!/usr/bin/python3
"""Script that lists all cities from the database hbtn_0e_4_usa.

    Script takes 3 args, msql: username, password & database.
    Result is sorted in ascending order by cities.id"""

from sys import argv
import MySQLdb


def main():
    """Entry point for the script."""

    conn = MySQLdb.connect(host='localhost', port=3306,
                           user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()

    cur.execute('SELECT cities.id, cities.name, states.name \
                FROM states, cities \
                WHERE cities.state_id = states.id')
    for row in cur.fetchall():
        print(row)


if __name__ == '__main__':
    main()

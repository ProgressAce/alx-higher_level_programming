#!/usr/bin/python3
"""Script that displays all records of states table matching the given arg.

    Script takes 4 arguments, mysql: username, password & database to connect
    to the hbtn_0e_0_usa database, and name arg to match a state name.
    Results are sorted in ascending order by states.id"""

from sys import argv
import MySQLdb


def main():
    """Entry point of the script."""

    conn = MySQLdb.connect(host='localhost', port=3306,
                           user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()

    cur.execute('SELECT id, name FROM states WHERE name="{}"'.format(argv[4]))
    for row in cur.fetchall():
        print(row)


if __name__ == '__main__':
    main()

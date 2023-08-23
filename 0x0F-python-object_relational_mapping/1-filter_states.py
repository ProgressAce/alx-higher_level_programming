#!/usr/bin/python3
"""Script that prints all the states that start with letter 'N'.

    Script takes 3 arguments, mysql: username, password & database to connect
    to the hbtn_0e_0_usa database.
    Results are sorted in ascending order by states.id"""

from sys import argv
import MySQLdb


def main():
    """Entry point of the script."""

    conn = MySQLdb.connect(host='127.0.0.1', port=3306,
                           user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()

    cur.execute('SELECT id, name FROM states WHERE name LIKE "N%"')
    for row in cur.fetchall():
        print(row)


if __name__ == '__main__':
    main()

#!/usr/bin/python3
"""Script that accepts the name of state and lists all cities of that state.

    Script takes 4 args, msql: username, password & database to connect to
    database hbtn_0e_4_usa, and state_name acting as the chosen state name.
    Result is sorted in ascending order by cities.id"""

from sys import argv
import MySQLdb


def main():
    """Entry point for the script."""

    conn = MySQLdb.connect(host='localhost', port=3306,
                           user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()

    sql = 'SELECT name FROM cities WHERE state_id = \
           (SELECT id FROM states WHERE name = %s LIMIT 1)'
    args = [argv[4]]

    if argv[4].isalpha():
        cur.execute(sql, args)
        for i, row in enumerate(cur.fetchall()):
            if i == cur.rowcount - 1:
                print(row[0])
                continue
            print(row[0], end=', ')


if __name__ == '__main__':
    main()

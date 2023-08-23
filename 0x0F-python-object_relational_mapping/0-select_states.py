#!/usr/bin/python3
"""Script that lists all the states from the database hbtn_0e_0_usa.

 It takes 3 arguments: mysql username, mysql password and database name
 and displays results in ascending order by state.id."""

from sys import argv
import MySQLdb


def main():
    """The entry execution of the script."""

    db = MySQLdb.connect(host="127.0.0.1", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()

    cur.execute("SELECT id, name FROM states ORDER BY id")
    for row in cur.fetchall():
        print(row)


if __name__ == '__main__':
    main()

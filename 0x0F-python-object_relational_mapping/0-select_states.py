#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connnect(host="localhost", user=sys.argv[1], port=3306,
                          password=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    sql = "SELECT id, name FROM states ORDER BY id ASC"
    cursor.execute(sql)
    states = cursor.fetchall()
    if states is not None:
        for row in states:
            print("({}, '{}')".format(row[0], row[1]))
        cursor.close()
        db.close()

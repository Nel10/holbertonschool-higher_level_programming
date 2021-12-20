#!/usr/bin/python3
"""
safe from MySQL injections!
"""

import MySQLdb
from sys import argv
if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db="hbtn_0e_0_usa", charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s ORDER by id ASC",
                (argv[4],))
    query_rows = cur.fetchall()
    for row in query_rows:
        if row[1] == argv[4]:
            print(row)
    cur.close()
    conn.close()

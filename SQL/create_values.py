#In order to populate the database once created, from the SQL script:

import sqlite3
connection = sqlite3.connect('expenses_tracker.db')


def scriptexecution(filename):
    with open(filename, 'r') as s:
        sql_script = s.read()
        connection.executescript(sql_script)
    s.closed


scriptexecution('create_values.sql')
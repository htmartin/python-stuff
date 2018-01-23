#!/usr/bin/env python

import sqlite3


## Create a SQLite3 database and table

# create a new database if the database doesn't already exist
conn = sqlite3.connect("new.db")

# get a cursor object used to execute SQL commands
cursor = conn.cursor()

# create a table
cursor.execute("""CREATE TABLE population
                  (city TEXT, state TEXT, population INT)
                  """)

#close the db connection
conn.close()


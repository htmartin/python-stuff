#!/usr/bin/env python

# INSERT Command
# import the sqlite3 library
import sqlite3

# create the connection object
with sqlite3.connect("new.db") as connection:
	# get a cursor object used to execute SQL commands
	c = connection.cursor()
	# insert data
	c.execute("INSERT INTO population VALUES('New York City', \
		'NY', 8400000)")
	c.execute("INSERT INTO population VALUES('San Francisco', \
		'CA', 800000)")


# close the database connection
connection.close()


# no commit needed

#!/usr/bin/env python

import sqlite3

with sqlite3.connect('test_database.db') as connection:
	c = connection.cursor()
	c.executescript("""
		DROP TABLE IF EXISTS Roster;
		CREATE TABLE Roster(FirstName TEXT, LastName TEXT, Age INT);
		INSERT INTO Roster VALUES('Ron','Obvious','42');
""")
"""
Jason Ray M. Moslares
CPE106L B2

This program creates the database and creates tables/entities.

"""

import sqlite3

conn = sqlite3.connect('catclasses.db')

query = (''' CREATE TABLE class(ClassNum INTEGER PRIMARY KEY, ClassDescription TEXT,
        MaxNumofPeople INTEGER, Date TEXT, ClassFee INTEGER);''')

conn.execute(query)

query = (''' CREATE TABLE participants(ParticipantsNum INTEGER PRIMARY KEY,
        LastName TEXT, FirstName TEXT, Address TEXT, City TEXT, State TEXT,
        PostalCode INTEGER, PhoneNum INTEGER, DateofBirth TEXT,
        EnrolledClass INTEGER, FOREIGN KEY(EnrolledClass) REFERENCES class(ClassNum));''')

conn.execute(query)
conn.close()
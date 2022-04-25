"""
Jason Ray M. Moslares
CPE106L B2

This program retrieves data from the database according to the condition
and outputs the result.

"""
import sqlite3

conn = sqlite3.connect('catclasses.db')

conn.execute("PRAGMA foreign_keys = ON")

cursor = conn.execute("SELECT ParticipantsNum, LastName, FirstName, EnrolledClass \
    FROM participants where EnrolledClass=1")

print("Students enrolled in this class: ")
for row in cursor:
    print(row)

conn.close()
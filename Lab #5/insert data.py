"""
Jason Ray M. Moslares
CPE106L B2

This program inserts the data into the tables/entities and to the database.

"""

import sqlite3

conn = sqlite3.connect('catclasses.db')

conn.execute("PRAGMA foreign_keys = ON")

conn.execute("INSERT INTO class (ClassNum, ClassDescription, MaxNumofPeople, Date, ClassFee) \
    VALUES (1, 'Hiking', 40, 'Feb 13, 2021', 300)")

conn.execute("INSERT INTO class (ClassNum, ClassDescription, MaxNumofPeople, Date, ClassFee) \
    VALUES (2, 'Biking', 25, 'Feb 26, 2021', 350)")

conn.execute("INSERT INTO class (ClassNum, ClassDescription, MaxNumofPeople, Date, ClassFee) \
    VALUES (3, 'Paddling', 15, 'Mar 6, 2021', 150)")

conn.execute("INSERT INTO participants (ParticipantsNum, LastName, FirstName, Address, City, State, PostalCode, PhoneNum, DateofBirth, EnrolledClass) \
        VALUES (1, 'Abrams', 'Miles', 'Williamsburg', '54 Quest Ave.', 'MA', 01096, 6175556032, 'June 3, 2001', 1)")

conn.execute("INSERT INTO participants (ParticipantsNum, LastName, FirstName, Address, City, State, PostalCode, PhoneNum, DateofBirth, EnrolledClass) \
        VALUES (2, 'Boyers', 'Rita', 'Jaffrey', '140 Oakton Rd.', 'NH', 03452, 6035552134, 'Mar 4, 2001', 1)")

conn.execute("INSERT INTO participants (ParticipantsNum, LastName, FirstName, Address, City, State, PostalCode, PhoneNum, DateofBirth, EnrolledClass) \
        VALUES (3, 'Devon', 'Harley', 'Sunderland', '25 Old Ranch Rd.', 'MA', 01375, 7815557767, 'September 1, 2001', 3)")

conn.execute("INSERT INTO participants (ParticipantsNum, LastName, FirstName, Address, City, State, PostalCode, PhoneNum, DateofBirth, EnrolledClass) \
        VALUES (4, 'Gregory', 'Zach', 'Dummer', '7 Moose House Rd.', 'NH', 03588, 6035558765, 'November 4, 2001', 2)")

conn.commit()
conn.close()
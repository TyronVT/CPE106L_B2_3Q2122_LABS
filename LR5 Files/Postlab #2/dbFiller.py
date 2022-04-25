import sampledata
import random
import sqlite3

names_list = sampledata.getNames()
lastnames_list = sampledata.getlastnames()
city_list = sampledata.getcity()
state_list = sampledata.getstates()

class Person:
    def randomperson(self):
        self.given_name = random.choice(names_list)
        self.last_name = random.choice(lastnames_list)
        self.city = random.choice(city_list)
        self.state = random.choice(state_list)
        self.middleinit = random.choice(self.given_name.upper())
        self.emailaddress = self.given_name + self.last_name + "@yahoo.com"

    def __str__(self):
        return f'Person({self.given_name}, {self.last_name}, {self.city}, {self.state}, {self.middleinit}, {self.emailaddress})'

class Location:
    def randomlocation(self):
        self.locationnum = random.randint(1,8888)
        self.locname = "Location " + str(random.randint(1,232))
        self.address = "Address " + str(random.randint(1,445))
        self.city = "City " + str(random.randrange(1,23))
        self.state = "State " + str(random.randrange(1,224))
        self.postalcode = random.randrange(999,9999)
        self.unitnum = random.randrange(1,100)
        self.sqfoot = random.randrange(10000,50000)
        self.bedrooms = random.randrange(1,10)
        self.bathrooms = random.randrange(1,10)
        self.maxperson = random.randrange(1,10)
        self.baserate = random.randrange(50000,1000000)

conn = sqlite3.connect('Solmaris1.db')

person = Person()
person.randomperson()

# Insert to RENTER table
i = 0
while i < 100:
    person.randomperson()
    
    query = '''INSERT INTO RENTER
    VALUES ('{renternum}', '{given_name}', '{mi}', '{last_name}', 
    '{address}', '{city}', '{state}', '{postal}', '{telephone}', 
    '{email}');'''.format(renternum=i, given_name=person.given_name, 
    mi=person.middleinit, last_name=person.last_name, 
    address=person.city+person.state, city=person.city, 
    state=person.state, postal=random.randrange(1000, 9999), 
    telephone=random.randrange(1000, 9999), email=person.emailaddress)

    cursor = conn.execute(query)
    i += 1

# Insert to PROPERTY table
i=0
while i < 100:
    loc = Location()
    loc.randomlocation()

    query = '''INSERT INTO PROPERTY 
    VALUES ('{locnum}','{locname}','{address}',
    '{city}','{state}','{postalcode}','{unitnum}',
    {sqfoot},{bedrooms},{bathrooms},{maxperson},
    {baserate});'''.format(locnum=loc.locationnum,
    locname=loc.locname,address=loc.address,
    city=loc.city,state=loc.state,postalcode=loc.postalcode,
    unitnum=loc.unitnum,sqfoot=loc.sqfoot,bedrooms=loc.bedrooms,
    bathrooms=loc.bathrooms,maxperson=loc.maxperson,baserate=loc.baserate)

    cursor = conn.execute(query)
    i += 1

query = "SELECT * FROM PROPERTY"
cursor = conn.execute(query)
for row in cursor:
    print(row)



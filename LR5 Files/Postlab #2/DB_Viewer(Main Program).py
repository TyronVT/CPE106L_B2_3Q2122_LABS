import sqlite3
import pandas as pd
conn = sqlite3.connect('Solmaris.db')

def gethighestrenternum():
    query = "SELECT MAX(RENTER_NUM) FROM RENTER;"
    cursor = conn.execute(query)
    for row in cursor:
        max = row[0]
    return int(max)

def addToRenters(num, firstname, middleinitial, 
                lastname, address, city, state, postalcode, 
                telephone, emailaddress):

    query = '''INSERT INTO RENTER VALUES 
            ('{renternum}', '{given_name}', '{mi}', '{last_name}', '{_address}', 
            '{_city}', '{_state}', '{postal}', '{_telephone}', '{email}');
            '''.format(renternum = num, given_name = firstname, 
            mi = middleinitial, last_name = lastname, _address = address, 
            _city = city, _state = state, postal = postalcode, _telephone = telephone, 
            email = emailaddress)

    cursor = conn.execute(query)
    conn.commit()

def isinDatabase(renter_num):
    query = "SELECT RENTER_NUM FROM RENTER WHERE RENTER_NUM='{num}'"
    query = query.format(num = renter_num)
    cursor = conn.execute(query)
    if len(cursor.fetchall()) > 0:
        return True
    else:
        return False

def addRentalAgreement(renter_num,start_date,end_date,weekly_amount):
    if isinDatabase(renter_num):
        renternum_query = '''INSERT INTO RENTAL_AGREEMENT VALUES
                        ('{_renter_num}',{start},{end},
                        {weeklyamount});
                        '''.format(_renter_num = renter_num,start = start_date,
                        end = end_date,weeklyamount = weekly_amount
                        )
        cursor = conn.execute(renternum_query)
        conn.commit()
    else:
        print("This renter is current not in the database Add them first before assigning a rental agreement.")

def viewProperty(loc_num):
    query = "SELECT * FROM PROPERTY WHERE LOC_NUM={LOC};".format(LOC = loc_num)
    cursor = conn.execute(query)
    row = cursor.fetchone()
    prompt = '''
    Loc Num: {locnum}
    Loc Name: {locname}
    Address: {address}
    City: {city}
    State: {state}
    Postal Code:{postal_code}
    Unit Num: {unit_num}
    Square Footage: {sq_foot}
    Number of Bedrroms: {bedrooms}
    Number of Bathrooms: {bathrooms}
    Max Numer of Persons: {max_persons}
    Base Weekly Rate: {base_weekly_rate}
    '''.format(
        locnum = row[0],locname = row[1],address = row[2],
        city = row[3],state = row[4],postal_code = row[5],
        unit_num = row[6],sq_foot = row[7],bedrooms = row[8],
        bathrooms = row[9],max_persons = row[10],base_weekly_rate = row[11]
        )
    print(prompt)

print("1. Add to Database\n2. Add Rental Agreement\n3. View Properties\n4. View all renters")
choice = input("Choice: ")
if choice == "1":
    given_name = input("Enter your first name: ")
    mi = input("Enter your middle initial: ")
    last_name = input("Enter your last name: ")
    address = input("Address: ")
    city = input("City: ")
    state = input("State: ")
    postal_code = input("Postal Code:")
    telephone = input("Telephone Num: ")
    email = input("Email Address: ")
    num = gethighestrenternum() + 1
    addToRenters(
        num,given_name,mi,last_name,address,city,state,postal_code,telephone,email
        )
    if isinDatabase(num):
        print("Successfully Added")

elif choice == "2":
    renternum = int(input("Enter renter num: "))
    startdate = input("Enter start date (YYYY-MM-DD): ")
    enddate = input("Enter end date(YYYY-MM-DD): ")
    weekly_amount = input("Weekly Amount: ")
    addRentalAgreement(renternum,startdate,enddate,weekly_amount)

elif choice == "3":
    locnum = input("Enter location number: ")
    viewProperty(locnum)

elif choice == "4":
    query = "SELECT * FROM RENTER"
    cursor = conn.execute(query)
    datalist = []
    for row in cursor:
        row = list(row)
        datalist.append(row)
    df = pd.DataFrame(datalist, 
    columns=['RENTER_NUM','FIRST_NAME', 'MIDDLE_INITIAL', 'LAST_NAME', 'ADDRESS', 
    'CITY', 'STATE', 'POSTAL_CODE', 'TELEPHONE', 'EMAIL_ADDRESS'])
    print(df.to_string(index=False))


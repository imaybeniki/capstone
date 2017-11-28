'''
Created on Oct 19, 2017

@author: chris
'''
#!/usr/bin/python
#!/usr/bin/python

import csv
import psycopg2

bikeshare_data= csv.reader('2017-Q1-Trips-History-Data.csv')

#database = psycopg2.connect (database = "***", user="***", password="***", host="localhost", port="5432")
database = psycopg2.connect (database = "ebdb", user="capstone", password="capstone123", host="aa1immzi54ninca.cyeyzuoh6sjb.us-east-1.rds.amazonaws.com", port="5432")


cursor= database.cursor()
delete="""DROP TABLE IF EXISTS USER_PUBLIC CASCADE; DROP TABLE IF EXISTS USER_PRIVATE CASCADE; DROP TABLE IF EXISTS LOCATIONS CASCADE;"""


print(delete)


# should this be PRIMARY KEY 
mydata=cursor.execute(delete)

cursor.execute("""CREATE TABLE USER_PUBLIC(
USER_ID     SERIAL    PRIMARY KEY NOT NULL UNIQUE,
USER_NAME   CHAR(20)              NOT NULL UNIQUE, 
LAST_NAME   CHAR(20)              NOT NULL,
FIRST_NAME  CHAR(20)              NOT NULL,
GENDER      CHAR(1)              CHECK(GENDER=='F' OR GENDER=='M'),
USER_AGE    INT                           ,
USER_EMAIL  CHAR(30)              NOT NULL,
USER_POINTS INT                   NOT NULL
);""")

print "USER_PUBLIC created successfully"
#PASSWORDS SHOULD BE STORED AS A HASHCODE
cursor.execute("""CREATE TABLE USER_PRIVATE(
ID   SERIAL    NOT NULL,
USER_NAME CHAR(20)  NOT NULL,
USER_PW   CHAR(40)  NOT NULL, 

PRIMARY KEY (ID),
FOREIGN KEY (ID) REFERENCES USER_PUBLIC(USER_ID)
); """)

#AMOUNT OF SPACES THAT ARE OCCUPIED AT LOCATION
#CONSTRAINT NEEDS TO BE ADDED TO KEEP BETWEEN 0 AND 1
#need to create Float(10,6)
#LOCATION_NAME    CHAR(40)      NOT NULL, REMOVED, LOCATION NUMBER WILL BE SERIALIZED VALUE
print "USER_PRIVATE table created successfully" 
 
cursor.execute(""" CREATE TABLE LOCATIONS(

 LOCATION_NUMBER  SERIAL        NOT NULL UNIQUE,
 LOCATION_ADDRESS CHAR(60)      NOT NULL UNIQUE,
 LOCATION_CITY    CHAR(60)      NOT NULL,
 LOCATION_STATE   CHAR(2)       NOT NULL,
 LOCATION_ZIP     NUMERIC(5)    NOT NULL,
 LOCATION_LAT     NUMERIC(10,7)   NOT NULL,
 LOCATION_LONG    NUMERIC(10,7)   NOT NULL,
 CAPACITY         INT           NOT NULL CHECK(CAPACITY<=10),
 OCCUPIED         INT           NOT NULL CHECK(OCCUPIED>=0 AND OCCUPIED<=CAPACITY), 
 WEIGHT           DECIMAL(3,2)  NOT NULL 
 
 );""")


print "LOCATIONS table created successfully"

cursor.execute("""DELETE FROM USER_PUBLIC; DELETE FROM LOCATIONS;""")

cursor.close
database.commit
print "Database commits executed"
database.close





#implement following: constraints

#implement insertion of location data from csv file


# for row i

#






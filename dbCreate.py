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
delete="""DROP TABLE IF EXISTS USER_PUBLIC CASCADE; DROP TABLE IF EXISTS USER_PRIVATE; DROP TABLE IF EXISTS LOCATIONS;"""


print(delete)

# should this be PRIMARY KEY 
mydata=cursor.execute(delete)

cursor.execute("""CREATE TABLE USER_PUBLIC(
USER_ID     SERIAL    PRIMARY KEY NOT NULL,
USER_NAME   CHAR(20)              NOT NULL, 
LAST_NAME   CHAR(20)              NOT NULL,
FIRST_NAME  CHAR(20)              NOT NULL,
GENDER      CHAR(1)              ,
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
print "USER_PRIVATE table created successfully"
 
cursor.execute(""" CREATE TABLE LOCATIONS(
 LOCATION_NAME    CHAR(40)      NOT NULL,
 LOCATION_ADDRESS CHAR(60)      NOT NULL,
 LOCATION_CITY    CHAR(60)      NOT NULL,
 LOCATION_STATE   CHAR(2)       NOT NULL,
 LOCATION_LAT     NUMERIC(10)   NOT NULL,
 LOCATION_LONG    NUMERIC(10,6)   NOT NULL,
 CAPACITY         INT           NOT NULL,
 OCCUPIED         INT           NOT NULL, 
 WEIGHT           DECIMAL(3,2)  NOT NULL 
 
 );""")


print "LOCATIONS table created successfully"


cursor.execute("""INSERT INTO USER_PUBLIC (USER_NAME,LAST_NAME,fIRST_NAME,GENDER, USER_AGE, 
USER_EMAIL,USER_POINTS ) VALUES 
('ccheath','Cheatham', 'Christopher','M', 21,'chris1357@live.com', 0),
('nikimay123', 'May', 'Nicole','F', 21,'nikimay@gmail.com',3);""")

print "values inserted"


cursor.execute("""select * from user_public;""")
for record in cursor:
    print record


#implement following: triggers constraints

#implements insertion of location data from csv file

# for row in bikeshare_data:
#     cursor.execute("Insert into LOCATIONS (LOCATION_NAME, lOCATION_ADRESS, LOCATION_CITY, lOCATION_STATE) values (%s,%s,%s,%s)")
    
     






cursor.close()
database.commit()
database.close()






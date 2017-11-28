'''
Created on Oct 31, 2017

@author: christopher
'''
import psycopg2


#database = psycopg2.connect (database = "***", user="***", password="***", host="localhost", port="5432")
database = psycopg2.connect (database = "ebdb", user="capstone", password="capstone123", host="aa1immzi54ninca.cyeyzuoh6sjb.us-east-1.rds.amazonaws.com", port="5432")


cursor= database.cursor()

cursor.execute("""DELETE FROM USER_PUBLIC; DELETE FROM LOCATIONS;""")
print "DELETE FROM USER_PUBLIC; DELETE FROM LOCATIONS"
cursor.execute("""INSERT INTO USER_PUBLIC (USER_NAME,LAST_NAME,fIRST_NAME,GENDER, USER_AGE, 
USER_EMAIL,USER_POINTS ) VALUES 
('ccheath','Cheatham', 'Christopher','M', 21,'chrischeat@live.com', 0),
('nikimay123', 'May', 'Nicole','F', 21,'nikimay@gmail.com',3),
('timmay14','May','Tim','M',24,'timmay@aol.com',9);""")

print "values inserted into user_public"

cursor.execute("""select * from user_public;""")
for record in cursor:
    print record


cursor.execute("""INSERT INTO LOCATIONS( lOCATION_ADDRESS, LOCATION_CITY, lOCATION_STATE,
LOCATION_ZIP,LOCATION_LAT,LOCATION_LONG,CAPACITY,OCCUPIED,WEIGHT) VALUES
('17th & K St NW', 'WASHINGTON','DC',20036,38.9025266,-77.0393836,10,5,.5),
('Potomac & Pennsylvania Ave SE', 'WASHINGTON','DC',20003,38.8805697,-77.9858173,10,3,.3),
('Adams Mill & Columbia Road NW', 'WASHINGTON','DC',20009,38.9226795,-77.0426674,10,8,.8),
('16th & Harvard ST NW', 'WASHINGTON','DC',20009,38.9268936,-77.0364869,10,6,.6),
('11th & H ST NE', 'WASHINGTON','DC',20002,38.9002357,-77.9915310,10,2,.2),
('9th & Upshur ST NW', 'WASHINGTON','DC',20011,38.9418787,-77.00250660,10,8,.8),
('8th and O ST NW', 'WASHINGTON','DC',20001,38.9085753,-77.0229408,10,2,.2),
('Park RD & Holmead Pl NW', 'WASHINGTON','DC',20010,38.9309272,-77.0308670,10,2,.2),
('Georgia & New Hampshire Ave NW', 'WASHINGTON','DC',20010,38.9362496,-77.0242799,10,2,.2),
('14th & Girard ST NW', 'WASHINGTON','DC',20009,38.9257420,-77.0323390,10,7,.7),
('8th and O ST NW', 'WASHINGTON','DC',20001,38.9085753,-77.0229408,10,2,.2),
('11th & Kenyon ST NW', 'WASHINGTON','DC',20010,38.9296718,-77.0277415,10,3,.3),
('10th and K ST NW', 'WASHINGTON','DC',20001,38.9025300,-77.0259938,10,5,.5),
('7th & T ST NW', 'WASHINGTON','DC',20001,38.9155720,-77.0219190,10,2,.2),
('M ST & Delaware AVE NE', 'WASHINGTON','DC',20002,38.9056473,-77.0030507,10,4,.4);""")
print "VALUES INSERTED INTO LOCATIONS"

cursor.execute("""select * from LOCATIONS;""")
for record in cursor:
    print record


cursor.close
database.commit
database.close

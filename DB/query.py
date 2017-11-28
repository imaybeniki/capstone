'''
Created on Nov 12, 2017

@author: christopher
'''
import _csv
import psycopg2

database = psycopg2.connect (database = "ebdb", user="capstone", password="capstone123", host="aa1immzi54ninca.cyeyzuoh6sjb.us-east-1.rds.amazonaws.com", port="5432")
cursor=database.cursor()

#cursor.execute("""DROP TABLE USER_PUBLIC CASCADE; DROP TABLE USER_PRIVATE CASCADE; DROP TABLE LOCATIONS CASCADE;""")
cursor.execute("""select * from LOCATIONS;""")
print("locations")
for record in cursor:
    print record
colnames=[desc[0] for desc in cursor.description]
for row in colnames:
    print row
      
print("user public   ")   
  
  
 

cursor.execute("""select * from user_public""")
for record in cursor:
    print(record)
colnames=[desc[0] for desc in cursor.description]
for row in colnames:
    print row
cursor.close()
database.commit()
database.close()
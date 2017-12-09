'''
Created on Nov 12, 2017

@author: christopher
'''
import _csv
import psycopg2
from Passwords import databasePassword
dbPW= databasePassword
def printQuery():
    """
    Returns locations table values from DB
    """
    database = psycopg2.connect (database = "ebdb", user="capstone", password=dbPW, host="aa1immzi54ninca.cyeyzuoh6sjb.us-east-1.rds.amazonaws.com", port="5432")
    cursor=database.cursor()
    
    #cursor.execute("""DROP TABLE USER_PUBLIC CASCADE; DROP TABLE USER_PRIVATE CASCADE; DROP TABLE LOCATIONS CASCADE;""")
    cursor.execute("""select * from LOCATIONS;""")# where location_address='2300 Gunter Ave';""")
    print("locations")
    for record in cursor:
        print record
    
    print("all records listed")
   
      
      
     
    

    
    
def printfirstTen():
    """
    Prints first ten values from locations table. 
    """
    
    database = psycopg2.connect (database = "ebdb", user="capstone", password=dbPW, host="aa1immzi54ninca.cyeyzuoh6sjb.us-east-1.rds.amazonaws.com", port="5432")
    cursor=database.cursor()
    
    #cursor.execute("""DROP TABLE USER_PUBLIC CASCADE; DROP TABLE USER_PRIVATE CASCADE; DROP TABLE LOCATIONS CASCADE;""")
    cursor.execute("""select * from LOCATIONS;""")# where location_address='2300 Gunter Ave';""")
    print("locations")
    for record in cursor:
        print record
    colnames=[desc[0] for desc in cursor.description]
    for row in colnames:
        print row
          
    print("user public   ")   
      
      
     
    
    cursor.execute("""select * from locations where location_number<=200""")
    for record in cursor:
        print(record)
        
    cursor.close()
    database.close()
    
    
    

     
        

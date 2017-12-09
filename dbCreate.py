'''
Created on Oct 19, 2017

@author: chris
'''
#!/usr/bin/python
#!/usr/bin/python


import psycopg2
from Passwords import databasePassword
dbPassword= databasePassword


def createDB():
    """
    Drops and creates locations table for new data to be inserted into locations table.
    """
    database = psycopg2.connect (database = "ebdb", user="capstone", password=dbPassword, host="aa1immzi54ninca.cyeyzuoh6sjb.us-east-1.rds.amazonaws.com", port="5432")

    cursor= database.cursor()
    delete="""DROP TABLE IF EXISTS USER_PUBLIC CASCADE; DROP TABLE IF EXISTS USER_PRIVATE CASCADE; DROP TABLE IF EXISTS LOCATIONS CASCADE;"""
    
    
    
    cursor.execute(delete)
    print(delete)
    

    
    
     
    cursor.execute(""" CREATE TABLE LOCATIONS(
    
     LOCATION_NUMBER  SERIAL        NOT NULL UNIQUE,
     LOCATION_ADDRESS CHAR(80)      NOT NULL UNIQUE,
     LOCATION_CITY    CHAR(60)      NOT NULL,
     LOCATION_STATE   CHAR(2)       NOT NULL,
     LOCATION_ZIP     NUMERIC(5)    NOT NULL,
     LOCATION_LAT     NUMERIC(10,7)   NOT NULL,
     LOCATION_LONG    NUMERIC(10,7)   NOT NULL,
     CAPACITY         INT           NOT NULL CHECK(CAPACITY<=10),
     OCCUPIED         INT           NOT NULL CHECK(OCCUPIED>=0 AND OCCUPIED<=CAPACITY),
     WEIGHT           DECIMAL(3,2)  NOT NULL,
     FLAG   CHAR(15) NOT NULL,
     CONSTRAINT CHECK_FLAG CHECK(FLAG IN ('G','Y','R'))
     
     
     );""")
    

    
    print "LOCATIONS table created successfully"
    
    cursor.execute(""" DELETE FROM LOCATIONS;""")
    cursor.execute("""select * from LOCATIONS""")
    

    
    
    
    
    cursor.close()
    database.commit()
    #cursor.execute("""DELETE FROM USER_PUBLIC cascade;""")
    print "Database commits executed"
    database.close()











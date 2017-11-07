'''
Created on Oct 30, 2017

@author: christopher
'''

import psycopg2
import csv

from geopy.geocoders import Nominatim




# def add_user(user_name,first_name,last_name,gender,user_age,user_email):
# 
# 
#     sq1= """INSERT INTO USER_PUBLIC(USER_NAME,FIRST_NAME,LAST_NAME,GENDER,USER_AGE,USER_EMAIL,USER_POINTS)
#             VALUES(%S,%S,%S,%S,%S,%S,0)"""
#     
#     database=None
#     try:
#     
#         #database = psycopg2.connect (database = "***", user="***", password="***", host="localhost", port="5432")
#         database = psycopg2.connect (database = "ebdb", user="capstone", 
#                                      password="capstone123", host="aa1immzi54ninca.cyeyzuoh6sjb.us-east-1.rds.amazonaws.com", port="5432")
# 
#         cursor=database.cursor()
#         
#         cursor.execute(sq1,(user_name,first_name,last_name,gender,user_age,user_email))
#         print "new user added to table"
#         
#     except(Exception, psycopg2.DatabaseError) as error:
#          print(error)
#     finally:
#         if database is not None:
#             database.close()
#             
            
def populate_locations_Capital_bikeshare():
    sq1= "INSERT INTO LOCATIONS" #finish sql statement statement
    
    
    
    output=[] # will hold location values stored in csv file
    #fileData=open('2017-Q1-Trips-History-Data.csv','rb') 
    fileData=open('testcsv.csv','rb')
    #reader=csv.reader(fileData, dlimiter=",")
    for line in fileData:
        cell=line.split(",")
        output.appaned(cell[3])
    fileData.close()
    print output
    print "values"
    
    
    
    # using geolocator to generate latitude and longitude to populate  tables from adresses of table
    geolocator=Nominatim()

    location=geolocator.geocode("17th & K ST NW")

    print(location.address)


    print(location.latitude)
    print (location.longitude)
    
    
    
    database=None
    try:
        #database = psycopg2.connect (database = "***", user="***", password="***", host="localhost", port="5432")
        database = psycopg2.connect (database = "ebdb", user="capstone", 
                                     password="capstone123", host="aa1immzi54ninca.cyeyzuoh6sjb.us-east-1.rds.amazonaws.com", port="5432")

        cursor=database.cursor()
    
    #using statement to push values for locations
     
            
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if database is not None:
            database.close()  
            
def main():
    populate_locations_Capital_bikeshare()
    

                
            


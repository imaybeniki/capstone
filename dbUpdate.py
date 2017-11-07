'''
Created on Oct 30, 2017

@author: christopher
'''

import psycopg2
import csv
import random

from geopy.geocoders import Nominatim

geolocator = Nominatim()
# location=geolocator.geocode("5th St & Massachusetts Ave NW")
# 
# try:
#     print(location.address)
#     
# except: 
#     print("location is not accepted or has already been used. skipping to next value")


prevAddr=[]
with open('/home/christopher/Downloads/2017-Q1-Trips-History-Data.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    k=1
    for row in readCSV:

        # occupied spaces
        occ = random.randrange(0, 11)
        # capacity of bikerack
        cap = 10.0
        # percentage of bike rack full
        weight = occ / cap
        
        flag = "N/A"
        if(weight < .33):
            flag = 'G'
        if((weight > .33) & (weight < .66)):
            flag = 'Y'
        if((weight > .66) & (weight <= 1.00)):
            flag = "R"
        if(weight > 1.0):
            print("value not less than or equal to 10")
        
    
             
        location = geolocator.geocode(row[4])
        
       
        if not location:#((location.address is None) or (location.longitude is None) or (location.latitude is  None)):
            print("null location. skipping value")
            continue
        #if location:
        longe = float(location.longitude)
        lat=float(location.latitude)
        
        #simple address values to be used for database insertion
        retAddr=row[4]
        
        theAddr = location.address
        addCopy=theAddr
#         print(theAddr)
        sp=addCopy.split(',')
        theLength=len(sp)-1
        city=sp[theLength-3]
        print(city)
        
        state=sp[theLength-2]
        print(state)
        zipCode=sp[theLength-1]
        #converting the zipcode to an integer for insertion into the database
        intZip=int(zipCode)  
        
        if(state==' District of Columbia'):
            state='DC'
        elif(state==' Maryland'):
            state='MD'
        elif(state==' Virginia'):
            state='VA'
        else:
            print('state out of index')
            continue
         
             
          
         
             
        if location in prevAddr:
            print(row[4], "address already used, skipping value")
            continue
        prevAddr.append(location)
         
       # print("INSERT INTO LOCATIONS( lOCATION_ADDRESS, LOCATION_CITY, lOCATION_STATE,LOCATION_ZIP,LOCATION_LAT,LOCATION_LONG,CAPACITY,OCCUPIED,WEIGHT) VALUES")    
        print(k,row[4],city,state,intZip, lat, longe, occ, cap, weight, flag)
        k=k+1     
         
         
        #open database connection
        database = psycopg2.connect (database = "ebdb", user="capstone", password="capstone123", host="aa1immzi54ninca.cyeyzuoh6sjb.us-east-1.rds.amazonaws.com", port="5432")   
              
        cursor=database.cursor()
        statement= "INSERT INTO LOCATIONS( lOCATION_ADDRESS, LOCATION_CITY, lOCATION_STATE,LOCATION_ZIP,LOCATION_LAT,LOCATION_LONG,CAPACITY,OCCUPIED,WEIGHT,FLAG) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        data=(retAddr,city,state,intZip,lat,longe,cap,occ,weight,flag) 
        cursor.execute(statement,data)
        print(retAddr, "added to db") 
         
        cursor.close
        database.commit
        database.close
            
        # except:
            # print("location is not accepted or has already been used. skipping to next value")
            
        
        


























        
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
            
# def populate_locations_Capital_bikeshare():
#     print "values"
#     sq1= "INSERT INTO LOCATIONS" #finish sql statement statement
#     
#     
#     
#     output=[] # will hold location values stored in csv file
#     #fileData=open('2017-Q1-Trips-History-Data.csv','rb') 
#     fileData=open('testcsv.csv','rb')
#     #reader=csv.reader(fileData, dlimiter=",")
#     for line in fileData:
#         cell=line.split(",")
#         output.appaned(cell[3])
#     fileData.close()
#     print output
#     print "values"
#     
#     
#     
#     # using geolocator to generate latitude and longitude to populate  tables from adresses of table
#     geolocator=Nominatim()
# 
#     location=geolocator.geocode("17th & K ST NW")
# 
#     print(location.address)
# 
# 
#     print(location.latitude)
#     print (location.longitude)
#     
#     
#     
#     database=None
#     try:
#         #database = psycopg2.connect (database = "***", user="***", password="***", host="localhost", port="5432")
#         database = psycopg2.connect (database = "ebdb", user="capstone", 
#                                      password="capstone123", host="aa1immzi54ninca.cyeyzuoh6sjb.us-east-1.rds.amazonaws.com", port="5432")
# 
#         cursor=database.cursor()
#         
#     
#     #using statement to push values for locations
#      
#             
#     except(Exception, psycopg2.DatabaseError) as error:
#         print(error)
#     finally:
#         if database is not None:
#             database.close()  
            
def main():
    print "something"
#    populate_locations_Capital_bikeshare()
    

                
            



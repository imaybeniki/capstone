'''
Created on Nov 13, 2017

@author: christopher
'''

import psycopg2
from psycopg2._psycopg import IntegrityError
import csv
import random
from geopy import geocoders
from geopy.geocoders import GoogleV3


geolocator= geocoders.GoogleV3('AIzaSyCXrGjSj0fcuCRm8d2r2u5s1MEI1v_Kpu4')


values=[]

#change to method

with open('/home/christopher/uhaulTest.csv') as csvfile:
     with open('/home/christopher/UhaulFormatted.csv','w') as csvWrite:
        writer=csv.writer(csvWrite,delimiter=",")
    
        readCSV = csv.reader(csvfile, delimiter=',')
        k=1
        #row nhmbers of latitude and longitude
        rowLat=1
        rowLong=0
        prevLocations=[]
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
                flag = 'R'
            if(weight > 1.0):
                print("value not less than or equal to 10")
            
            lat=row[rowLat]
            longe=row[rowLong]
            
            latVal=str(lat)
            longVal=str(longe)
           
            coordinate=(latVal+","+longVal)
            
            print(coordinate)
            
            
            #Skip insertion of coordinate into tables if values already exist
            if(prevLocations.__contains__(coordinate)):
                print("Location already used. Skipping to next value")
                continue
            
            
            prevLocations.append(coordinate)
            
                
            location=geolocator.reverse(coordinate)
            location=location[0];
            if location:
            
                print(location.address)
                fullAddress=location.address
                fullAddress=fullAddress.split(",")
                retAddress=fullAddress[0]
                city=fullAddress[len(fullAddress)-3]
                print(city)
                stateAndZip=fullAddress[len(fullAddress)-2]
                print(stateAndZip)
                stateAndZip=stateAndZip.split(" ")
                state=stateAndZip[1]
                zipCode=stateAndZip[2]
                print("state: ",state)
                print("zip: ",zipCode)
                longe=location.longitude
                lat=location.latitude
                
                try:
                            
                    database = psycopg2.connect (database = "ebdb", user="capstone", password="capstone123", host="aa1immzi54ninca.cyeyzuoh6sjb.us-east-1.rds.amazonaws.com", port="5432")   
                    
                    cursor=database.cursor()
                    statement= "INSERT INTO LOCATIONS( lOCATION_ADDRESS, LOCATION_CITY, lOCATION_STATE,LOCATION_ZIP,LOCATION_LAT,LOCATION_LONG,CAPACITY,OCCUPIED,WEIGHT,FLAG) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
                    data=(retAddress,city,state,zipCode,lat,longe,cap,occ,weight,flag) 
                    cursor.execute(statement,data)
                    print(retAddress, "added to db") 
               
                    cursor.close()
                    database.commit()
                    database.close()
                except IntegrityError:
                    print("Location is not accepted or has already been used. skipping to next value.")
    #             
    #             
                writedata=(retAddress,city,state,str(zipCode),str(lat),str(longe),str(cap),str(occ),str(weight),flag)
                writer.writerow(writedata)       
                
            
           
            if not location:#((location.address is None) or (location.longitude is None) or (location.latitude is  None)):
                print("null location. skipping value")
                continue
        
        
        
        
        
        
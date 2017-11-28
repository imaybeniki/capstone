'''
Created on Nov 14, 2017

@author: christopher
'''
import string
from psycopg2._psycopg import IntegrityError
'''
Created on Oct 30, 2017

@author: christopher
'''

import psycopg2
import csv
import random
from geopy import geocoders

from geopy.geocoders import GoogleV3

geolocator= geocoders.GoogleV3('AIzaSyCXrGjSj0fcuCRm8d2r2u5s1MEI1v_Kpu4')
# location=geolocator.geocode("5th St & Massachusetts Ave NW")
# 
# try:
#     print(location.address)
#     
# except: 
#     print("location is not accepted or has already been used. skipping to next value")


prevAddr=[]
values=[]

#change to method
with open('/home/christopher/RedboxTest.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    #counter
    with open('/home/christopher/RedboxFormatted.csv','w') as csvWrite:
        writer=csv.writer(csvWrite,delimiter=",")
        k=1
        rowNumber=3
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
            
            
            tempAddress=(row[rowNumber])
            if tempAddress in prevAddr:
                print(row[rowNumber], "address already used, skipping value")
                continue
            prevAddr.append(tempAddress)
            
            #print(tempAddress.replace("214", "this wont work"))
            tempAddress=str(tempAddress)
            adress=tempAddress.replace("\n", " ")
            print("replace:", adress)
            neededAddress=tempAddress.split('\n')
            neededAddress=neededAddress[0]
            #print(type(tempAddress))
            print("Needed addess::" +neededAddress)
            print(tempAddress)
            
            
           
        
            
                 
            location = geolocator.geocode(adress)
            print("location:")
            print(location)
    
             
            
            if not location:#((location.address is None) or (location.longitude is None) or (location.latitude is  None)):
                print("null location. skipping value")
                continue
            if location:
                longe = float(location.longitude)
                lat=float(location.latitude)
                print("latitude:",lat)
                print("longitude",longe)
                
            
             
    
             
            theAddr = location.address
            addCopy=theAddr
            print(theAddr)
            sp=addCopy.split(',')
            theLength=len(sp)-1
            city=sp[theLength-2]
            print(type(city))
            print("city:" ,city)
             
            state=sp[theLength-1]
            stZip=state.split(" ")
            state=stZip[len(stZip)-2]
            zipCode=stZip[len(stZip)-1]
            print("state: " ,state)
            print("Zip: ", zipCode)
    
    
            intZip=int(zipCode)  
            
            
             
                 
             
             
                 
            
             
            print("INSERT INTO LOCATIONS( lOCATION_ADDRESS, LOCATION_CITY, lOCATION_STATE,LOCATION_ZIP,LOCATION_LAT,LOCATION_LONG,CAPACITY,OCCUPIED,WEIGHT) VALUES")    
            print(k,neededAddress,city,state,intZip, lat, longe, occ, cap, weight, flag)
            k=k+1     
             
             
            #open database connection
            try:
                database = psycopg2.connect (database = "ebdb", user="capstone", password="capstone123", host="aa1immzi54ninca.cyeyzuoh6sjb.us-east-1.rds.amazonaws.com", port="5432")   
                    
                cursor=database.cursor()
                statement= "INSERT INTO LOCATIONS( lOCATION_ADDRESS, LOCATION_CITY, lOCATION_STATE,LOCATION_ZIP,LOCATION_LAT,LOCATION_LONG,CAPACITY,OCCUPIED,WEIGHT,FLAG) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
                data=(neededAddress,city,state,intZip,lat,longe,cap,occ,weight,flag) 
                cursor.execute(statement,data)
                print(neededAddress, "added to db") 
               
                cursor.close()
                database.commit()
                database.close()
            except IntegrityError:
                print("Location is not accepted or has already been used. skipping to next value.")
                continue

            writedata=(neededAddress,city,state,str(intZip),str(lat),str(longe),str(cap),str(occ),str(weight),flag)
            writer.writerow(writedata)

            
                
        
                    











            

    

                
            

